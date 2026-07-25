#!/usr/bin/env python3
"""Report heuristic Chinese academic-style findings without rewriting text."""

from __future__ import annotations

import argparse
import bisect
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    line: int
    column: int
    match: str
    excerpt: str
    message: str
    offset: int

    def public_dict(self) -> dict[str, object]:
        data = asdict(self)
        data.pop("offset")
        return data


LITERAL_RULES = (
    (
        "empty-emphasis",
        "suggestion",
        (
            "值得注意的是",
            "需要指出的是",
            "必须强调的是",
            "不容忽视的是",
            "毋庸置疑",
            "显而易见",
        ),
        "核对该强调语是否承载信息；若无，请直接陈述证据或结论。",
    ),
    (
        "subjective-framing",
        "suggestion",
        ("我认为", "我觉得", "我个人认为", "在我看来"),
        "正式学术正文通常应说明判断依据；引语或质性材料中的原话除外。",
    ),
    (
        "absolute-claim",
        "warning",
        ("彻底解决", "完全证明", "必然导致", "无可争议", "绝对优于"),
        "检查证据是否支持绝对断言，并保留适用条件和不确定性。",
    ),
)

INITIAL_TRANSITION_RE = re.compile(
    r"(^|[。！？!?]\s*|\n\s*)(首先|其次|再次|最后|此外|另外|综上所述|总之)(?=[，,:：\s])",
    re.MULTILINE,
)
STATISTICAL_CLAIM_RE = re.compile(
    r"显著(?:地)?(?:提高|提升|改善|降低|优于|高于|低于|增强|减少|增加|差异)"
)
STATISTICAL_SUPPORT_RE = re.compile(
    r"(?:[pP]\s*[<=>≤≥]\s*0?\.\d+|置信区间|显著性检验|统计检验|"
    r"[tT]\s*检验|卡方检验|方差分析|秩和检验)"
)
NOVELTY_RE = re.compile(r"(?:首次提出|首创|填补(?:了)?(?:国内|国际|领域)?空白)")
SENTENCE_RE = re.compile(r".+?(?:[。！？!?]|\n\s*\n|\Z)", re.DOTALL)
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")


def mask_match(match: re.Match[str]) -> str:
    return "".join("\n" if char == "\n" else " " for char in match.group(0))


def mask_non_prose(text: str) -> str:
    """Mask common code, comment, and math regions while preserving offsets."""

    patterns = (
        re.compile(r"^\s*```.*?^\s*```[^\n]*$", re.MULTILINE | re.DOTALL),
        re.compile(
            r"\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|lstlisting|verbatim)\}"
            r".*?\\end\{\1\}",
            re.DOTALL,
        ),
        re.compile(r"\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$", re.DOTALL),
        re.compile(r"(?<!\\)\$(?!\$).*?(?<!\\)\$", re.DOTALL),
        re.compile(r"(?<!\\)%[^\n]*"),
    )

    masked = text
    for pattern in patterns:
        masked = pattern.sub(mask_match, masked)
    return masked


def line_starts(text: str) -> list[int]:
    starts = [0]
    starts.extend(match.end() for match in re.finditer(r"\n", text))
    return starts


def locate(starts: list[int], offset: int) -> tuple[int, int]:
    line_index = bisect.bisect_right(starts, offset) - 1
    return line_index + 1, offset - starts[line_index] + 1


def make_excerpt(text: str, start: int, end: int, radius: int = 28) -> str:
    left = max(0, start - radius)
    right = min(len(text), end + radius)
    excerpt = " ".join(text[left:right].split())
    if left > 0:
        excerpt = "..." + excerpt
    if right < len(text):
        excerpt += "..."
    return excerpt


def make_finding(
    text: str,
    starts: list[int],
    rule_id: str,
    severity: str,
    start: int,
    end: int,
    message: str,
) -> Finding:
    line, column = locate(starts, start)
    return Finding(
        rule_id=rule_id,
        severity=severity,
        line=line,
        column=column,
        match=text[start:end],
        excerpt=make_excerpt(text, start, end),
        message=message,
        offset=start,
    )


def iter_literal_findings(
    text: str, analysis_text: str, starts: list[int]
) -> Iterable[Finding]:
    for rule_id, severity, phrases, message in LITERAL_RULES:
        for phrase in phrases:
            search_from = 0
            while True:
                start = analysis_text.find(phrase, search_from)
                if start < 0:
                    break
                end = start + len(phrase)
                yield make_finding(
                    text, starts, rule_id, severity, start, end, message
                )
                search_from = end


def iter_transition_findings(
    text: str, analysis_text: str, starts: list[int]
) -> Iterable[Finding]:
    for match in INITIAL_TRANSITION_RE.finditer(analysis_text):
        start, end = match.span(2)
        yield make_finding(
            text,
            starts,
            "mechanical-transition",
            "suggestion",
            start,
            end,
            "确认该词是否表达真实顺序或逻辑；不要仅为连接句子而保留或替换。",
        )


def iter_sentence_findings(
    text: str,
    analysis_text: str,
    starts: list[int],
    long_sentence: int,
) -> Iterable[Finding]:
    for sentence_match in SENTENCE_RE.finditer(analysis_text):
        sentence = sentence_match.group(0)
        if not sentence.strip():
            continue

        original_sentence = text[sentence_match.start() : sentence_match.end()]

        if long_sentence > 0:
            cjk_count = len(CJK_RE.findall(sentence))
            if cjk_count > long_sentence:
                leading = len(sentence) - len(sentence.lstrip())
                start = sentence_match.start() + leading
                end = min(sentence_match.end(), start + 1)
                yield make_finding(
                    text,
                    starts,
                    "long-sentence",
                    "suggestion",
                    start,
                    end,
                    f"该句约含 {cjk_count} 个汉字，超过 {long_sentence} 的审阅阈值；检查修饰层级和主干，勿机械拆句。",
                )

        if not STATISTICAL_SUPPORT_RE.search(original_sentence):
            for claim_match in STATISTICAL_CLAIM_RE.finditer(sentence):
                start = sentence_match.start() + claim_match.start()
                end = sentence_match.start() + claim_match.end()
                yield make_finding(
                    text,
                    starts,
                    "statistical-significance",
                    "warning",
                    start,
                    end,
                    "“显著”可能构成统计断言；核对检验方法和结果，或改为有数据依据的幅度描述。",
                )

        for novelty_match in NOVELTY_RE.finditer(sentence):
            start = sentence_match.start() + novelty_match.start()
            end = sentence_match.start() + novelty_match.end()
            yield make_finding(
                text,
                starts,
                "novelty-claim",
                "warning",
                start,
                end,
                "核对检索范围和文献依据，并限定“首次”或“填补空白”的适用范围。",
            )


def analyze(text: str, long_sentence: int) -> list[Finding]:
    analysis_text = mask_non_prose(text)
    starts = line_starts(text)
    findings = [
        *iter_literal_findings(text, analysis_text, starts),
        *iter_transition_findings(text, analysis_text, starts),
        *iter_sentence_findings(text, analysis_text, starts, long_sentence),
    ]
    return sorted(findings, key=lambda item: (item.offset, item.rule_id))


def read_input(path_value: str) -> tuple[str, str]:
    if path_value == "-":
        return sys.stdin.read(), "<stdin>"

    path = Path(path_value)
    if path.suffix.lower() in {".docx", ".pdf"}:
        raise ValueError(
            f"{path.suffix} is not plain text; extract it with format-aware tooling first"
        )
    try:
        return path.read_text(encoding="utf-8"), str(path)
    except FileNotFoundError as exc:
        raise ValueError(f"file not found: {path}") from exc
    except UnicodeDecodeError as exc:
        raise ValueError(f"file is not valid UTF-8 text: {path}") from exc
    except OSError as exc:
        raise ValueError(f"cannot read {path}: {exc}") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Report heuristic Chinese academic-style findings. "
            "Findings require contextual review and are never automatic errors."
        )
    )
    parser.add_argument("path", help="UTF-8 text, Markdown, or LaTeX file; use - for stdin")
    parser.add_argument("--json", action="store_true", help="emit structured JSON")
    parser.add_argument(
        "--long-sentence",
        type=int,
        default=60,
        metavar="N",
        help="flag sentences with more than N Chinese characters; use 0 to disable",
    )
    parser.add_argument(
        "--fail-on-findings",
        action="store_true",
        help="exit with status 1 when any finding is reported",
    )
    return parser


def print_human(source: str, findings: list[Finding], long_sentence: int) -> None:
    counts = Counter(finding.severity for finding in findings)
    print(f"Checked: {source}")
    print(
        f"Findings: {len(findings)} "
        f"(warning={counts['warning']}, suggestion={counts['suggestion']})"
    )
    print(f"Long-sentence review threshold: {long_sentence or 'disabled'}")
    print("Note: findings are review prompts; zero findings do not prove quality or journal compliance.")
    for finding in findings:
        print(
            f"L{finding.line}:C{finding.column} "
            f"[{finding.severity}] {finding.rule_id}: {finding.match}"
        )
        print(f"  {finding.message}")
        print(f"  {finding.excerpt}")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.long_sentence < 0:
        parser.error("--long-sentence must be 0 or a positive integer")

    try:
        text, source = read_input(args.path)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    findings = analyze(text, args.long_sentence)
    if args.json:
        counts = Counter(finding.severity for finding in findings)
        payload = {
            "schema_version": 1,
            "source": source,
            "options": {"long_sentence": args.long_sentence},
            "summary": {
                "total": len(findings),
                "by_severity": dict(sorted(counts.items())),
                "interpretation": (
                    "Heuristic review prompts only; zero findings do not establish "
                    "writing quality or journal compliance."
                ),
            },
            "findings": [finding.public_dict() for finding in findings],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print_human(source, findings, args.long_sentence)

    if args.fail_on_findings and findings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
