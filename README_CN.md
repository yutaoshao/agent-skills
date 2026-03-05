# Agent Skills

[English](./README.md) | [中文](./README_CN.md)

AI Agent 技能库仓库，用于存放和管理各类 AI 能力模块。

## 概览

本仓库是一个模块化的 AI 技能集合，为智能体（Agent）提供标准化的能力接入方案。每个技能模块包含详细的使用指南、代码示例和最佳实践。

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
├── project-analyzer/        # 代码库分析与上手
│   ├── SKILL.md             # 8 个模块化工作流
│   └── references/          # 检查清单、模式目录与报告模板
└── [其他技能库]/             # 扩展位置
```

## 技能库列表

| 技能库 | 描述 | SDK | 模块数 |
|--------|------|-----|--------|
| [glm-skills](./glm-skills/) | 智谱 GLM AI 能力集合 | z-ai-web-dev-sdk | 12 |
| [paper-writer](./paper-writer/) | 学术论文全流程写作（从代码到投稿） | - | 10 |
| [paper-polish](./paper-polish/) | 学术 LaTeX 论文润色工作流 | - | 6 |
| [project-analyzer](./project-analyzer/) | 代码库分析与开发者上手 | - | 8 |

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

### 开发者工具
- **project-analyzer**: 系统化代码库分析（技术栈识别、项目结构、架构模式、依赖分析、代码质量、开发流程、风险评估、综合报告），适用于项目交接与新人上手

## 快速开始

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

# 项目分析器
/plugin marketplace add yutaoshao/agent-skills/project-analyzer
```

### 手动安装

克隆仓库并将所需技能复制到 Claude skills 目录：

```bash
git clone https://github.com/yutaoshao/agent-skills.git
cp -r agent-skills/paper-polish ~/.claude/skills/
cp -r agent-skills/project-analyzer ~/.claude/skills/
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

## 许可证

各技能模块独立授权，详见各模块目录下的 `LICENSE.txt`。
