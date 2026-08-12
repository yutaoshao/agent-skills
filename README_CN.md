# Agent Skills

[English](./README.md) | [中文](./README_CN.md)

AI Agent 技能库仓库，用于存放和管理各类 AI 能力模块。

## 概览

本仓库是一个模块化的 AI 技能集合，为智能体（Agent）提供标准化的能力接入方案。每个技能模块包含详细的使用指南、代码示例和最佳实践，覆盖模型能力、学术写作、阅读学习方法、开发者工作流与仓库级辅助工具。

## 项目结构

```
agent-skills/
├── glm-skills/              # 智谱 GLM 技能库
│   ├── ASR/                 # 语音识别
│   ├── TTS/                 # 文本转语音
│   ├── LLM/                 # 大语言模型
│   ├── VLM/                 # 视觉语言模型
│   ├── image-generation/    # 图像生成
│   ├── video-generation/    # 视频生成
│   ├── web-search/          # 网络搜索
│   ├── web-reader/          # 网页内容提取
│   ├── canvas-design/       # 画布设计
│   ├── frontend-design/     # 前端设计系统
│   └── document-skills/     # 文档处理 (docx/xlsx/pptx/pdf)
├── paper-writer/            # 学术论文写作（全流程）
│   ├── SKILL.md             # 10 阶段工作流（代码到投稿）
│   ├── modules/             # 10 个阶段模块
│   ├── references/          # 写作哲学、检查清单与指南
│   ├── plan-template/       # 跨会话上下文管理
│   └── scripts/             # 初始化与风格检查脚本
├── paper-polish/            # 学术论文润色 (LaTeX)
│   ├── SKILL.md             # 6 个模块化工作流
│   └── references/          # 模式目录与检查清单
├── polish-chinese-core-paper/ # 中文核心期刊论文润色
│   ├── SKILL.md             # 逐句审查、学术诚信优先的实质编辑流程
│   ├── references/          # 必要性、诚信、期刊与 Word 公式审校指南
│   └── scripts/             # 中文表达与 DOCX 公式诊断脚本
├── project-analyzer/        # 代码库分析与上手
│   ├── SKILL.md             # 证据化项目上手流程
│   ├── agents/              # Codex UI 元数据
│   └── references/          # 证据规则、场景路径指南与按需深挖
├── sync-context/            # 跨 Agent 上下文同步与交接
│   ├── SKILL.md             # 会话协议与验证
│   └── scripts/             # 初始化、检查与注入脚本
├── git-commit/              # Git 暂存、提交说明与本地合并回主分支
│   ├── SKILL.md             # 提交流程、暂存规则与本地合并回主分支
│   ├── references/          # commit type、scope 与 body 规范
│   └── scripts/             # 工作区变更摘要脚本
├── how-to-read-a-book/       # 主动阅读与书籍分析
│   └── SKILL.md             # 检视阅读、分析阅读与主题阅读工作流
├── module-diagram-planner/  # 模块图谱选择与规划
│   ├── SKILL.md             # 图谱规划工作流
│   └── references/          # 图类型目录与选择启发
├── adr-management/          # 架构决策记录管理
│   ├── SKILL.md             # 持久化 ADR 流程与 Trellis 联动
│   ├── references/          # ADR 模板与元数据规则
│   └── scripts/             # 无依赖 ADR 生命周期 CLI
└── [其他技能库]/             # 扩展位置
```

## 技能库列表

| 技能库 | 描述 | SDK | 模块数 |
|--------|------|-----|--------|
| [glm-skills](./glm-skills/) | 智谱 GLM AI 能力集合 | z-ai-web-dev-sdk | 12 |
| [paper-writer](./paper-writer/) | 学术论文全流程写作（从代码到投稿） | - | 10 |
| [paper-polish](./paper-polish/) | 学术 LaTeX 论文润色工作流 | - | 6 |
| [polish-chinese-core-paper](./polish-chinese-core-paper/) | 兼顾逐句内容取舍、目标期刊、学术诚信与 Word 公式保真的中文论文编辑工作流 | - | 8 |
| [project-analyzer](./project-analyzer/) | 证据化代码库上手与代表性使用路径追踪 | - | - |
| [sync-context](./sync-context/) | 跨 Agent 上下文同步与交接协议 | - | 3 |
| [git-commit](./git-commit/) | Git 暂存、详细 conventional commit 与安全本地合并回主分支工作流 | - | 6 |
| [how-to-read-a-book](./how-to-read-a-book/) | 面向书籍、论文与长文的主动阅读工作流 | - | 4 |
| [module-diagram-planner](./module-diagram-planner/) | 面向功能模块理解的图谱选择与规划 | - | 2 |
| [adr-management](./adr-management/) | 创建、评审、校验和替代 ADR，并与 Trellis 联动 | - | 3 |

## 技能分类

### 语音与对话
- **ASR**: 语音识别，支持多种音频格式
- **TTS**: 语音合成，多种音色可选
- **LLM**: 大语言模型对话

### 视觉与多模态
- **VLM**: 图像理解与分析
- **image-generation**: AI 图像生成
- **video-generation**: AI 视频生成

### Web 能力
- **web-search**: 网络搜索
- **web-reader**: 网页内容解析

### 文档处理
- **docx**: Word 文档操作
- **xlsx**: Excel 表格处理
- **pptx**: PowerPoint 演示
- **pdf**: PDF 文档处理

### 设计系统
- **canvas-design**: 视觉艺术创作
- **frontend-design**: 前端 UI 设计规范

### 学术写作
- **paper-writer**: 学术论文全流程写作，从项目源代码到可投稿 LaTeX 论文（10 阶段：代码分析、文献综述、论文结构、章节写作、图表生成、引用管理、去AI润色、LaTeX编译、投稿审查、返修重投）
- **paper-polish**: 自动化 LaTeX 论文润色（去 AI 痕迹、引用扩展、图表验证、编译清理、全面质量审查）
- **polish-chinese-core-paper**: 面向中文核心期刊投稿的实质编辑；标准与深度模式逐句、逐公式判断功能、必要性、篇章位置和强调程度，同时保护数据与论证边界，保留 Word 原生 OMML 与嵌入公式对象，核对编号、交叉引用和逐页渲染，并支持计算机与工程学科规则、可追溯期刊 profile 和作者待确认项

### 阅读与学习
- **how-to-read-a-book**: 受 *How to Read a Book* / 《如何阅读一本书》启发的主动阅读工作流（检视阅读、分析阅读、主题阅读比较、按体裁生成阅读产物）

### 开发者工具
- **project-analyzer**: 面向陌生代码库的证据化接手与上手分析。识别项目服务的用户与核心价值，梳理职责和状态边界，并沿一条代表性路径追踪入口、关键代码、数据变化、副作用与测试；技术栈、依赖、质量、CI、安全和技术债作为按需深挖项
- **sync-context**: 跨 Agent 上下文同步，通过 `CONTEXT.md` 交接协议实现（会话启动/结束协议、结构验证、时效检查、通过 `context/` 子目录渐进式披露）
- **git-commit**: 面向真实仓库 diff 的 Git 暂存与详细提交说明（范围判断、staged/unstaged 检查、conventional commit 格式化、提交后核对、安全本地合并回主分支）
- **module-diagram-planner**: 在绘制 Mermaid 或设计文档图之前，为功能模块选择和规划图谱（边界、运行时流程、决策、配置、数据、错误、指标、测试）
- **adr-management**: 管理持久化架构决策记录，支持状态转换、替代关系、确定性校验，并明确关联 Trellis `design.md` 与 `.trellis/spec/`

## 快速开始

### 在 Codex 中安装

使用 Codex 内置的 `$skill-installer`，可以直接从 GitHub 安装单个技能。例如：

```text
$skill-installer https://github.com/yutaoshao/agent-skills/tree/main/polish-chinese-core-paper
$skill-installer https://github.com/yutaoshao/agent-skills/tree/main/adr-management
```

将 URL 末尾替换为本仓库中的其他技能目录即可安装相应技能。Codex 会自动检测新安装的技能；如果技能没有出现，请重启 Codex。

如需手动安装到用户范围，请克隆仓库并将所需技能复制到 `~/.agents/skills`：

```bash
git clone https://github.com/yutaoshao/agent-skills.git
mkdir -p ~/.agents/skills
cp -R agent-skills/polish-chinese-core-paper ~/.agents/skills/
cp -R agent-skills/adr-management ~/.agents/skills/
```

如果技能只应在某个仓库内使用，请改为复制到该仓库的 `.agents/skills/` 目录。

### 通过 Claude Code 插件市场安装

安装整个仓库（所有技能）：

```bash
/plugin marketplace add yutaoshao/agent-skills
```

或单独安装某个技能：

```bash
# 智谱 GLM AI 技能库（语音、视觉、生成、搜索、设计、文档）
/plugin marketplace add yutaoshao/agent-skills/glm-skills

# 学术论文写作（全流程）
/plugin marketplace add yutaoshao/agent-skills/paper-writer

# 学术论文润色
/plugin marketplace add yutaoshao/agent-skills/paper-polish

# 中文核心期刊论文润色
/plugin marketplace add yutaoshao/agent-skills/polish-chinese-core-paper

# 项目分析器
/plugin marketplace add yutaoshao/agent-skills/project-analyzer

# 跨 Agent 上下文同步
/plugin marketplace add yutaoshao/agent-skills/sync-context

# Git 暂存与提交说明
/plugin marketplace add yutaoshao/agent-skills/git-commit

# 主动阅读与书籍分析
/plugin marketplace add yutaoshao/agent-skills/how-to-read-a-book

# 模块图谱规划
/plugin marketplace add yutaoshao/agent-skills/module-diagram-planner

# 架构决策记录管理
/plugin marketplace add yutaoshao/agent-skills/adr-management
```

### 为 Claude Code 手动安装

克隆仓库并将所需技能复制到 Claude skills 目录：

```bash
git clone https://github.com/yutaoshao/agent-skills.git
cp -r agent-skills/paper-polish ~/.claude/skills/
cp -r agent-skills/polish-chinese-core-paper ~/.claude/skills/
cp -r agent-skills/project-analyzer ~/.claude/skills/
cp -r agent-skills/git-commit ~/.claude/skills/
cp -r agent-skills/how-to-read-a-book ~/.claude/skills/
cp -r agent-skills/module-diagram-planner ~/.claude/skills/
cp -r agent-skills/adr-management ~/.claude/skills/
```

每个技能模块的 `SKILL.md` 包含完整的使用指南和代码示例。

## 贡献指南

添加新技能模块时，请遵循以下结构：

```
skill-name/
├── SKILL.md         # 核心文档 (必需)
├── LICENSE.txt      # 许可证 (必需)
├── scripts/         # 示例代码 (推荐)
└── README.md        # 快速入门 (可选)
```

如果新增的顶层技能会影响仓库发现路径、安装方式或能力总览，请在同一次修改中同步更新 `README.md` 和 `README_CN.md`。

## 许可证

各技能模块独立授权，详见各模块目录下的 `LICENSE.txt`。
