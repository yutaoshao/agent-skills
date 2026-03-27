# Agent Skills

[English](./README.md) | [中文](./README_CN.md)

这是本仓库的技能总览入口。根目录的中英文 README 是唯一的总览文档；各个技能目录以 `SKILL.md` 作为唯一权威说明，不再依赖各自的 `README.md`。

## 仓库结构

```text
agent-skills/
├── README.md
├── README_CN.md
├── glm-skills/
│   ├── ASR/
│   ├── TTS/
│   ├── LLM/
│   ├── VLM/
│   ├── image-generation/
│   ├── video-generation/
│   ├── web-search/
│   ├── web-reader/
│   ├── canvas-design/
│   ├── frontend-design/
│   └── document-skills/
│       ├── docx/
│       ├── xlsx/
│       ├── pptx/
│       └── pdf/
├── paper-writer/
├── paper-polish/
└── project-analyzer/
```

## 约定

- 每个可安装 skill 都必须包含 `SKILL.md`。
- `SKILL.md` 是触发条件、工作流、引用资料和脚本说明的权威来源。
- 仓库级的发现方式、安装说明和维护规范统一放在根目录这对 README 中。
- `references/`、`scripts/`、`assets/`、`modules/`、`plan-template/` 等可选目录，只在会影响执行时由 `SKILL.md` 说明即可。

## 技能索引

### 研究与开发类 Skills

| Skill | 作用 |
|------|------|
| `paper-writer` | 面向 CS/ML/AI 项目的论文全流程写作，从仓库分析到投稿与返修 |
| `paper-polish` | 面向 LaTeX 论文的润色、去 AI 痕迹、补充引用、图表核查和投稿前检查 |
| `project-analyzer` | 面向陌生代码库的上手分析、架构梳理、依赖检查、风险识别和报告生成 |
| `sync-context` | 使用 `CONTEXT.md`、镜像指令文件与 git/hook 校验的跨 Agent 交接工作流 |

### GLM Skills

| Skill | 作用 |
|------|------|
| `ASR` | 基于 `z-ai-web-dev-sdk` 的语音转文本工作流 |
| `TTS` | 多音色、可调参数的文本转语音工作流 |
| `LLM` | 对话补全与聊天应用工作流 |
| `VLM` | 图像理解与多模态对话 |
| `image-generation` | 文生图能力 |
| `video-generation` | 文生视频 / 图生视频的异步生成流程 |
| `web-search` | 网络搜索与结果检索 |
| `web-reader` | 网页正文抽取与内容读取 |
| `canvas-design` | 静态视觉设计与海报类创作 |
| `frontend-design` | 以 design token 为核心的前端实现与界面质量指导 |
| `docx` | Word 文档创建、编辑与审阅 |
| `xlsx` | 表格创建、分析与保公式编辑 |
| `pptx` | 演示文稿创建与编辑 |
| `pdf` | PDF 抽取、生成、表单填写与文档处理 |

## 安装方式

### Claude Code

如果是个人安装，把目标技能目录复制到 `~/.claude/skills/<skill-name>`：

```bash
cp -R /path/to/agent-skills/paper-writer ~/.claude/skills/paper-writer
```

如果是项目级安装，则复制到目标仓库的 `.claude/skills/<skill-name>`。

安装完成后，重启 Claude Code 或重新加载 skills 以使新技能生效。

### Codex

把目标技能目录复制到 `~/.codex/skills/<skill-name>`：

```bash
cp -R /path/to/agent-skills/paper-writer ~/.codex/skills/paper-writer
```

安装完成后，重启 Codex 以加载新技能。

### 其他 Agent 运行时

如果你使用的是其他 Agent 运行时，把目标技能目录整体复制到对应的 skills 目录即可。可迁移的最小单元就是以 `SKILL.md` 为核心的技能文件夹。

## 维护规范

新增或更新 skill 时：

1. 添加或更新 `SKILL.md`。
2. 把详细执行说明保留在 `SKILL.md` 及其引用文件中。
3. 如果技能列表、安装方式或仓库约定变了，同步更新根目录中英文 README。
4. 除非某个平台强制要求，否则不要再为单个 skill 添加 `README.md`。
5. 本仓库内涉及跨 Agent 协作时，优先使用 `sync-context/`，并配合 `CONTEXT.md`、`CLAUDE.md` 与自动生成的 `AGENTS.md`。

## 许可证

每个技能目录自行维护许可证信息；如果目录中有 `LICENSE.txt`，以该文件为准。
