from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "audit_word_equations.py"
SPEC = importlib.util.spec_from_file_location("audit_word_equations", SCRIPT)
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = AUDIT
SPEC.loader.exec_module(AUDIT)


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
O_NS = "urn:schemas-microsoft-com:office:office"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PACKAGE_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
MC_NS = "http://schemas.openxmlformats.org/markup-compatibility/2006"
U_NS = "urn:unsupported-equation-choice"


def document_xml(body: str) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{W_NS}" xmlns:m="{M_NS}" xmlns:o="{O_NS}" xmlns:r="{R_NS}" xmlns:mc="{MC_NS}" xmlns:u="{U_NS}">
  <w:body>{body}</w:body>
</w:document>
"""


def write_docx(
    path: Path,
    body: str,
    embeddings: tuple[bytes, ...] = (),
    media: tuple[bytes, ...] = (),
    relationships: tuple[tuple[str, str, str], ...] = (),
) -> None:
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(
            "[Content_Types].xml",
            "<Types xmlns=\"http://schemas.openxmlformats.org/package/2006/content-types\"/>",
        )
        archive.writestr("word/document.xml", document_xml(body))
        if relationships:
            relationship_nodes = "".join(
                f'<Relationship Id="{relationship_id}" Type="{relationship_type}" Target="{target}"/>'
                for relationship_id, relationship_type, target in relationships
            )
            archive.writestr(
                "word/_rels/document.xml.rels",
                f'<Relationships xmlns="{PACKAGE_REL_NS}">{relationship_nodes}</Relationships>',
            )
        for index, payload in enumerate(embeddings, start=1):
            archive.writestr(f"word/embeddings/object{index}.bin", payload)
        for index, payload in enumerate(media, start=1):
            archive.writestr(f"word/media/image{index}.png", payload)


class AuditWordEquationsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_native_equation_number_and_field_chain(self) -> None:
        path = self.root / "native.docx"
        write_docx(
            path,
            """
<w:p>
  <w:r><w:t>由式（</w:t></w:r>
  <w:fldSimple w:instr=" REF eq1 "><w:r><w:t>1</w:t></w:r></w:fldSimple>
  <w:r><w:t>）可知。</w:t></w:r>
</w:p>
<w:p>
  <w:pPr><w:tabs><w:tab w:val="center" w:pos="4000"/></w:tabs></w:pPr>
  <w:r><w:tab/></w:r>
  <m:oMath><m:r><m:t>x=1</m:t></m:r></m:oMath>
  <w:r><w:tab/><w:t>(</w:t></w:r>
  <w:bookmarkStart w:id="1" w:name="eq1"/>
  <w:fldSimple w:instr=" SEQ Equation "><w:r><w:t>1</w:t></w:r></w:fldSimple>
  <w:bookmarkEnd w:id="1"/>
  <w:r><w:t>)</w:t></w:r>
</w:p>
""",
        )

        result = AUDIT.load_audit(path)

        self.assertEqual(result.native_math_count, 1)
        self.assertEqual(result.displayed_math_count, 1)
        self.assertEqual([record.number for record in result.numbers], ["1"])
        self.assertEqual([record.field_type for record in result.fields], ["REF", "SEQ"])
        self.assertIn("eq1", result.bookmarks)
        self.assertFalse(
            any(issue.code == "dangling-ref-field" for issue in result.issues)
        )

    def test_inline_equation_followed_by_year_is_not_numbered(self) -> None:
        path = self.root / "inline.docx"
        write_docx(
            path,
            """
<w:p>
  <w:r><w:t>该模型</w:t></w:r>
  <m:oMath><m:r><m:t>x</m:t></m:r></m:oMath>
  <w:r><w:t>沿用既有定义（2024）</w:t></w:r>
</w:p>
""",
        )

        result = AUDIT.load_audit(path)

        self.assertEqual(result.inline_math_count, 1)
        self.assertEqual(result.numbers, [])

    def test_ole_preview_is_not_reported_as_drawing_only_equation(self) -> None:
        path = self.root / "ole.docx"
        write_docx(
            path,
            """
<w:p>
  <w:r><w:tab/></w:r>
  <w:object><w:pict/><o:OLEObject r:id="rId1"/></w:object>
  <w:r><w:tab/><w:t>(1)</w:t></w:r>
</w:p>
""",
            embeddings=(b"ole-object", b"preview"),
            relationships=(
                (
                    "rId1",
                    "http://schemas.openxmlformats.org/officeDocument/2006/relationships/oleObject",
                    "embeddings/object1.bin",
                ),
            ),
        )

        result = AUDIT.load_audit(path)

        self.assertEqual(result.embedded_object_count, 1)
        self.assertEqual(result.embedding_part_count, 2)
        self.assertEqual(len(result.embedded_relationships), 1)
        self.assertEqual([record.number for record in result.numbers], ["1"])
        self.assertTrue(any(issue.code == "embedded-object" for issue in result.issues))
        self.assertFalse(
            any(
                issue.code == "drawing-equation-candidate"
                for issue in result.issues
            )
        )

    def test_semantic_change_fails_comparison(self) -> None:
        before_path = self.root / "before.docx"
        after_path = self.root / "after.docx"
        write_docx(
            before_path,
            "<w:p><m:oMath><m:r><m:t>x+1</m:t></m:r></m:oMath></w:p>",
        )
        write_docx(
            after_path,
            "<w:p><m:oMath><m:r><m:t>x-1</m:t></m:r></m:oMath></w:p>",
        )

        issues = AUDIT.compare_audits(
            AUDIT.load_audit(before_path), AUDIT.load_audit(after_path)
        )

        self.assertTrue(
            any(issue.code == "comparison-semantic-math" for issue in issues)
        )

    def test_raw_tex_detection_handles_commands_left_division_and_currency(self) -> None:
        tex_path = self.root / "tex.docx"
        epsilon_path = self.root / "epsilon.docx"
        division_path = self.root / "division.docx"
        currency_path = self.root / "currency.docx"
        write_docx(
            tex_path,
            r"<w:p><m:oMath><m:r><m:t>\\frac{x}{y}</m:t></m:r></m:oMath></w:p>",
        )
        write_docx(
            epsilon_path,
            r"<w:p><m:oMath><m:r><m:t>\epsilon</m:t></m:r></m:oMath></w:p>",
        )
        write_docx(
            division_path,
            r"<w:p><m:oMath><m:r><m:t>A\B</m:t></m:r></m:oMath></w:p>",
        )
        write_docx(
            currency_path,
            r"<w:p><m:oMath><m:r><m:t>C=$5</m:t></m:r></m:oMath></w:p>",
        )

        tex_result = AUDIT.load_audit(tex_path)
        epsilon_result = AUDIT.load_audit(epsilon_path)
        division_result = AUDIT.load_audit(division_path)
        currency_result = AUDIT.load_audit(currency_path)

        self.assertTrue(any(issue.code == "raw-tex-in-omml" for issue in tex_result.issues))
        self.assertTrue(
            any(issue.code == "raw-tex-in-omml" for issue in epsilon_result.issues)
        )
        self.assertFalse(
            any(issue.code == "raw-tex-in-omml" for issue in division_result.issues)
        )
        self.assertFalse(
            any(issue.code == "raw-tex-in-omml" for issue in currency_result.issues)
        )

    def test_math_script_style_is_part_of_semantic_signature(self) -> None:
        before_path = self.root / "double-struck.docx"
        after_path = self.root / "roman.docx"
        write_docx(
            before_path,
            """
<w:p><m:oMath><m:r><m:rPr><m:scr m:val="double-struck"/></m:rPr><m:t>R</m:t></m:r></m:oMath></w:p>
""",
        )
        write_docx(
            after_path,
            """
<w:p><m:oMath><m:r><m:rPr><m:scr m:val="roman"/></m:rPr><m:t>R</m:t></m:r></m:oMath></w:p>
""",
        )

        issues = AUDIT.compare_audits(
            AUDIT.load_audit(before_path), AUDIT.load_audit(after_path)
        )

        self.assertTrue(
            any(issue.code == "comparison-semantic-math" for issue in issues)
        )

    def test_inline_to_display_change_is_reported(self) -> None:
        inline_path = self.root / "inline-role.docx"
        display_path = self.root / "display-role.docx"
        write_docx(
            inline_path,
            "<w:p><m:oMath><m:r><m:t>x</m:t></m:r></m:oMath></w:p>",
        )
        write_docx(
            display_path,
            "<w:p><m:oMathPara><m:oMath><m:r><m:t>x</m:t></m:r></m:oMath></m:oMathPara></w:p>",
        )

        issues = AUDIT.compare_audits(
            AUDIT.load_audit(inline_path), AUDIT.load_audit(display_path)
        )

        self.assertTrue(
            any(issue.code == "comparison-equation-roles" for issue in issues)
        )
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                str(inline_path),
                "--compare",
                str(display_path),
                "--strict",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 1)
        self.assertIn("comparison-equation-roles", completed.stdout)

    def test_removed_ole_reference_fails_even_when_binary_part_remains(self) -> None:
        before_path = self.root / "ole-before.docx"
        after_path = self.root / "ole-after.docx"
        relationships = (
            (
                "rId1",
                "http://schemas.openxmlformats.org/officeDocument/2006/relationships/oleObject",
                "embeddings/object1.bin",
            ),
        )
        write_docx(
            before_path,
            '<w:p><w:object><o:OLEObject r:id="rId1"/></w:object></w:p>',
            embeddings=(b"ole-object",),
            relationships=relationships,
        )
        write_docx(
            after_path,
            "<w:p/>",
            embeddings=(b"ole-object",),
            relationships=relationships,
        )

        issues = AUDIT.compare_audits(
            AUDIT.load_audit(before_path), AUDIT.load_audit(after_path)
        )

        self.assertTrue(
            any(issue.code == "comparison-embedded-count" for issue in issues)
        )
        self.assertTrue(
            any(
                issue.code == "comparison-embedded-relationships" for issue in issues
            )
        )

    def test_text_box_equation_is_not_counted_twice(self) -> None:
        path = self.root / "textbox.docx"
        write_docx(
            path,
            """
<w:p><w:r><w:drawing><w:txbxContent>
  <w:p><m:oMath><m:r><m:t>x</m:t></m:r></m:oMath></w:p>
</w:txbxContent></w:drawing></w:r></w:p>
""",
        )

        result = AUDIT.load_audit(path)

        self.assertEqual(result.native_math_count, 1)

    def test_visible_reference_without_number_is_reported(self) -> None:
        path = self.root / "missing-number.docx"
        write_docx(path, "<w:p><w:r><w:t>由式（1）可知。</w:t></w:r></w:p>")

        result = AUDIT.load_audit(path)

        self.assertTrue(
            any(
                issue.code == "unresolved-visible-equation-reference"
                for issue in result.issues
            )
        )

    def test_appendix_number_in_adjacent_table_cell_is_linked(self) -> None:
        path = self.root / "table-number.docx"
        write_docx(
            path,
            """
<w:tbl><w:tr>
  <w:tc><w:p><m:oMath><m:r><m:t>x=1</m:t></m:r></m:oMath></w:p></w:tc>
  <w:tc><w:p><w:r><w:t>(A.1)</w:t></w:r></w:p></w:tc>
</w:tr></w:tbl>
""",
        )

        result = AUDIT.load_audit(path)

        self.assertEqual([record.number for record in result.numbers], ["A.1"])
        self.assertEqual(result.equations[0].number, "A.1")
        self.assertEqual(result.equations[0].role, "display-candidate")

    def test_table_data_year_is_not_linked_as_equation_number(self) -> None:
        path = self.root / "table-data.docx"
        write_docx(
            path,
            """
<w:tbl><w:tr>
  <w:tc><w:p><w:r><w:t>模型</w:t></w:r><m:oMath><m:r><m:t>x</m:t></m:r></m:oMath></w:p></w:tc>
  <w:tc><w:p><w:r><w:t>(2024)</w:t></w:r></w:p></w:tc>
</w:tr></w:tbl>
""",
        )

        result = AUDIT.load_audit(path)

        self.assertEqual(result.numbers, [])
        self.assertEqual(result.equations[0].role, "inline")

    def test_ref_bookmark_rebound_to_another_equation_fails_comparison(self) -> None:
        before_path = self.root / "bookmark-before.docx"
        after_path = self.root / "bookmark-after.docx"
        reference = """
<w:p><w:r><w:t>由式（</w:t></w:r><w:fldSimple w:instr=" REF eq1 "><w:r><w:t>1</w:t></w:r></w:fldSimple><w:r><w:t>）可知。</w:t></w:r></w:p>
"""
        equation_one_before = """
<w:p><w:r><w:tab/></w:r><w:bookmarkStart w:id="1" w:name="eq1"/><m:oMath><m:r><m:t>x=1</m:t></m:r></m:oMath><w:bookmarkEnd w:id="1"/><w:r><w:tab/><w:t>(1)</w:t></w:r></w:p>
"""
        equation_one_after = """
<w:p><w:r><w:tab/></w:r><m:oMath><m:r><m:t>x=1</m:t></m:r></m:oMath><w:r><w:tab/><w:t>(1)</w:t></w:r></w:p>
"""
        equation_two_before = """
<w:p><w:r><w:tab/></w:r><m:oMath><m:r><m:t>y=2</m:t></m:r></m:oMath><w:r><w:tab/><w:t>(2)</w:t></w:r></w:p>
"""
        equation_two_after = """
<w:p><w:r><w:tab/></w:r><w:bookmarkStart w:id="1" w:name="eq1"/><m:oMath><m:r><m:t>y=2</m:t></m:r></m:oMath><w:bookmarkEnd w:id="1"/><w:r><w:tab/><w:t>(2)</w:t></w:r></w:p>
"""
        write_docx(
            before_path, reference + equation_one_before + equation_two_before
        )
        write_docx(after_path, reference + equation_one_after + equation_two_after)

        issues = AUDIT.compare_audits(
            AUDIT.load_audit(before_path), AUDIT.load_audit(after_path)
        )

        self.assertTrue(
            any(
                issue.code == "comparison-equation-bookmark-bindings"
                for issue in issues
            )
        )

    def test_visible_reference_change_is_reported(self) -> None:
        before_path = self.root / "reference-before.docx"
        after_path = self.root / "reference-after.docx"
        equations = """
<w:p><w:r><w:tab/></w:r><m:oMath><m:r><m:t>x=1</m:t></m:r></m:oMath><w:r><w:tab/><w:t>(1)</w:t></w:r></w:p>
<w:p><w:r><w:tab/></w:r><m:oMath><m:r><m:t>y=2</m:t></m:r></m:oMath><w:r><w:tab/><w:t>(2)</w:t></w:r></w:p>
"""
        write_docx(
            before_path,
            equations + "<w:p><w:r><w:t>由式（1）可知。</w:t></w:r></w:p>",
        )
        write_docx(
            after_path,
            equations + "<w:p><w:r><w:t>由式（2）可知。</w:t></w:r></w:p>",
        )

        issues = AUDIT.compare_audits(
            AUDIT.load_audit(before_path), AUDIT.load_audit(after_path)
        )

        self.assertTrue(
            any(
                issue.code == "comparison-visible-equation-references"
                for issue in issues
            )
        )

    def test_equation_paragraph_move_is_reported(self) -> None:
        before_path = self.root / "location-before.docx"
        after_path = self.root / "location-after.docx"
        equation = "<w:p><m:oMath><m:r><m:t>x</m:t></m:r></m:oMath></w:p>"
        write_docx(before_path, equation)
        write_docx(after_path, "<w:p/>" + equation)

        issues = AUDIT.compare_audits(
            AUDIT.load_audit(before_path), AUDIT.load_audit(after_path)
        )

        self.assertTrue(
            any(issue.code == "comparison-equation-locations" for issue in issues)
        )

    def test_removed_drawing_equation_candidate_fails_comparison(self) -> None:
        before_path = self.root / "drawing-before.docx"
        after_path = self.root / "drawing-after.docx"
        write_docx(
            before_path,
            "<w:p><w:r><w:tab/><w:drawing/><w:tab/><w:t>(1)</w:t></w:r></w:p>",
        )
        write_docx(after_path, "<w:p/>")

        issues = AUDIT.compare_audits(
            AUDIT.load_audit(before_path), AUDIT.load_audit(after_path)
        )

        self.assertTrue(
            any(
                issue.code == "comparison-drawing-equation-candidates"
                for issue in issues
            )
        )

    def test_drawing_equation_binary_change_fails_comparison(self) -> None:
        before_path = self.root / "drawing-binary-before.docx"
        after_path = self.root / "drawing-binary-after.docx"
        body = "<w:p><w:r><w:tab/><w:drawing r:embed=\"rId1\"/><w:tab/><w:t>(1)</w:t></w:r></w:p>"
        relationships = (
            (
                "rId1",
                "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image",
                "media/image1.png",
            ),
        )
        write_docx(
            before_path,
            body,
            media=(b"formula-image-before",),
            relationships=relationships,
        )
        write_docx(
            after_path,
            body,
            media=(b"formula-image-after",),
            relationships=relationships,
        )

        issues = AUDIT.compare_audits(
            AUDIT.load_audit(before_path), AUDIT.load_audit(after_path)
        )

        self.assertTrue(
            any(
                issue.code == "comparison-drawing-equation-candidates"
                for issue in issues
            )
        )

    def test_alternate_content_counts_choice_not_fallback(self) -> None:
        path = self.root / "alternate-content.docx"
        write_docx(
            path,
            """
<w:p><w:r><w:tab/>
  <mc:AlternateContent>
    <mc:Choice Requires="w"><w:drawing/></mc:Choice>
    <mc:Fallback><w:pict/></mc:Fallback>
  </mc:AlternateContent>
  <w:tab/><w:t>(1)</w:t>
</w:r></w:p>
""",
        )

        result = AUDIT.load_audit(path)

        self.assertEqual(result.drawing_count, 1)
        self.assertEqual(len(result.drawing_equation_candidates), 1)

    def test_alternate_content_uses_fallback_for_unsupported_choice(self) -> None:
        before_path = self.root / "alternate-fallback-before.docx"
        after_path = self.root / "alternate-fallback-after.docx"

        def alternate(fallback_value: str) -> str:
            return f"""
<w:p><mc:AlternateContent>
  <mc:Choice Requires="u"><m:oMath><m:r><m:t>x=choice</m:t></m:r></m:oMath></mc:Choice>
  <mc:Fallback><m:oMath><m:r><m:t>{fallback_value}</m:t></m:r></m:oMath></mc:Fallback>
</mc:AlternateContent></w:p>
"""

        write_docx(before_path, alternate("x=1"))
        write_docx(after_path, alternate("x=2"))

        before = AUDIT.load_audit(before_path)
        after = AUDIT.load_audit(after_path)
        issues = AUDIT.compare_audits(before, after)

        self.assertEqual(before.equations[0].math_text, "x=1")
        self.assertTrue(
            any(issue.code == "comparison-semantic-math" for issue in issues)
        )

    def test_table_number_bookmark_rebinding_fails_comparison(self) -> None:
        before_path = self.root / "table-bookmark-before.docx"
        after_path = self.root / "table-bookmark-after.docx"
        reference = """
<w:p><w:r><w:t>由式（</w:t></w:r><w:fldSimple w:instr=" REF eq1 "><w:r><w:t>1</w:t></w:r></w:fldSimple><w:r><w:t>）可知。</w:t></w:r></w:p>
"""

        def row(symbol: str, number: int, bookmarked: bool) -> str:
            start = (
                '<w:bookmarkStart w:id="1" w:name="eq1"/>' if bookmarked else ""
            )
            end = '<w:bookmarkEnd w:id="1"/>' if bookmarked else ""
            return f"""
<w:tbl><w:tr>
  <w:tc><w:p><m:oMath><m:r><m:t>{symbol}={number}</m:t></m:r></m:oMath></w:p></w:tc>
  <w:tc><w:p>{start}<w:r><w:t>({number})</w:t></w:r>{end}</w:p></w:tc>
</w:tr></w:tbl>
"""

        write_docx(before_path, reference + row("x", 1, True) + row("y", 2, False))
        write_docx(after_path, reference + row("x", 1, False) + row("y", 2, True))

        issues = AUDIT.compare_audits(
            AUDIT.load_audit(before_path), AUDIT.load_audit(after_path)
        )

        self.assertTrue(
            any(
                issue.code == "comparison-equation-bookmark-bindings"
                for issue in issues
            )
        )

    def test_corrupt_member_is_a_clear_input_error(self) -> None:
        path = self.root / "corrupt.docx"
        write_docx(
            path,
            "<w:p><m:oMath><m:r><m:t>x=1</m:t></m:r></m:oMath></w:p>",
        )
        payload = bytearray(path.read_bytes())
        marker = payload.find(b"x=1")
        self.assertGreaterEqual(marker, 0)
        payload[marker] = ord("y")
        path.write_bytes(payload)

        with self.assertRaisesRegex(ValueError, "cannot read DOCX member"):
            AUDIT.load_audit(path)
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), str(path)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 2)
        self.assertIn("cannot read DOCX member", completed.stderr)


if __name__ == "__main__":
    unittest.main()
