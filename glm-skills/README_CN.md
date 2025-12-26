# GLM Skills

[English](./README.md) | [中文](./README_CN.md)

AI Agent 技能库集合，为 `z-ai-web-dev-sdk` 提供各类 AI 能力的使用指南和最佳实践。

## 概览

本仓库包含 12 个技能模块，覆盖语音、文本、图像、视频、文档处理及设计等多种 AI 能力。

## 目录结构

```
glm-skills/
├── ASR/                    # 语音识别 (Automatic Speech Recognition)
├── TTS/                    # 文本转语音 (Text to Speech)
├── LLM/                    # 大语言模型 (Large Language Model)
├── VLM/                    # 视觉语言模型 (Vision Language Model)
├── image-generation/       # AI 图像生成
├── video-generation/       # AI 视频生成
├── web-search/             # 网络搜索
├── web-reader/             # 网页内容提取
├── canvas-design/          # 画布设计 (视觉艺术创作)
├── frontend-design/        # 前端设计系统
└── document-skills/        # 文档处理技能集
    ├── docx/               # Word 文档
    ├── xlsx/               # Excel 表格
    ├── pptx/               # PowerPoint 演示
    └── pdf/                # PDF 文档
```

## 技能模块

### AI 核心能力

| 模块 | 描述 | 支持格式/特性 |
|------|------|--------------|
| **ASR** | 语音转文字 | WAV/MP3/M4A，Base64 编码传输 |
| **TTS** | 文字转语音 | 7 种中文声音，速度/音量可调 (0.5-2.0) |
| **LLM** | 对话生成 | 多轮对话，System Prompt，Context 管理 |
| **VLM** | 视觉理解 | 图片 URL/Base64，多图对比，OCR |
| **image-generation** | 图像生成 | 多种尺寸，Base64 输出 |
| **video-generation** | 视频生成 | 文生视频/图生视频，异步任务模式 |

### Web 能力

| 模块 | 描述 |
|------|------|
| **web-search** | 网络搜索，支持结果数量限制和时效性过滤 |
| **web-reader** | 网页内容提取，自动提取标题/HTML/发布时间 |

### 文档处理

| 模块 | 技术栈 | 主要功能 |
|------|--------|----------|
| **docx** | docx-js, OOXML | 创建/编辑/分析，Track Changes |
| **xlsx** | pandas, openpyxl | 公式计算，财务建模 |
| **pptx** | html2pptx, OOXML | HTML 转 PPT，模板复用 |
| **pdf** | pypdf, pdfplumber, reportlab | 表单填写，OCR |

### 设计系统

| 模块 | 描述 |
|------|------|
| **canvas-design** | 视觉艺术创作，包含 40+ 开源字体 |
| **frontend-design** | Design Token 系统，React + Tailwind CSS，WCAG AA 无障碍 |

## 快速开始

### 安装 SDK

```bash
npm install z-ai-web-dev-sdk
```

### 基础用法

```typescript
import ZAI from 'z-ai-web-dev-sdk';

async function chat() {
  const zai = await ZAI.create();
  const response = await zai.chat.completions.create({
    messages: [
      { role: 'system', content: 'You are a helpful assistant.' },
      { role: 'user', content: 'Hello!' }
    ]
  });
  return response;
}
```

### CLI 工具

使用 `z-ai` 命令行工具快速测试：

```bash
# 语音识别
z-ai asr --file audio.mp3

# 图像生成
z-ai image --prompt "a beautiful sunset"

# 网页搜索
z-ai search --query "latest AI news"
```

## 技能文档结构

每个技能模块遵循统一结构：

```
skill-name/
├── SKILL.md         # 核心文档 (YAML Frontmatter + Markdown)
├── LICENSE.txt      # 许可证
├── scripts/         # 示例脚本 (TypeScript)
└── [参考文档]        # 可选的补充文档
```

## 注意事项

1. **后端限定**: `z-ai-web-dev-sdk` 必须在后端代码中使用
2. **TTS 限制**: 单次请求最大 1024 字符，长文本需分块处理
3. **异步任务**: 图像/视频生成使用异步模式，需实现轮询逻辑
4. **文档编辑**: 操作 Office 文档前，请阅读对应的 OOXML 参考文档

## 许可证

- **MIT License**: ASR, TTS, LLM, VLM, image-generation, video-generation, web-search, web-reader, frontend-design
- **Proprietary**: canvas-design, document-skills (见各模块 LICENSE.txt)
