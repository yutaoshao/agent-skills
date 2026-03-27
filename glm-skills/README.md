# GLM Skills

[English](./README.md) | [中文](./README_CN.md)

A collection of AI Agent skills providing usage guides and best practices for `z-ai-web-dev-sdk`.

## Overview

This repository contains 12 skill modules covering speech, text, image, video, document processing, and design capabilities.

## Directory Structure

```
glm-skills/
├── ASR/                    # Automatic Speech Recognition
├── TTS/                    # Text to Speech
├── LLM/                    # Large Language Model
├── VLM/                    # Vision Language Model
├── image-generation/       # AI Image Generation
├── video-generation/       # AI Video Generation
├── web-search/             # Web Search
├── web-reader/             # Web Content Extraction
├── canvas-design/          # Canvas Design (Visual Art Creation)
├── frontend-design/        # Frontend Design System
└── document-skills/        # Document Processing Skills
    ├── docx/               # Word Documents
    ├── xlsx/               # Excel Spreadsheets
    ├── pptx/               # PowerPoint Presentations
    └── pdf/                # PDF Documents
```

## Skill Modules

### AI Core Capabilities

| Module | Description | Supported Formats/Features |
|--------|-------------|---------------------------|
| **ASR** | Speech to Text | WAV/MP3/M4A, Base64 encoding |
| **TTS** | Text to Speech | 7 Chinese voices, adjustable speed/volume (0.5-2.0) |
| **LLM** | Chat Completion | Multi-turn conversation, System Prompt, Context management |
| **VLM** | Visual Understanding | Image URL/Base64, multi-image comparison, OCR |
| **image-generation** | Image Generation | Multiple sizes, Base64 output |
| **video-generation** | Video Generation | Text-to-video/Image-to-video, async task mode |

### Web Capabilities

| Module | Description |
|--------|-------------|
| **web-search** | Web search with result limits and time filtering |
| **web-reader** | Web content extraction with auto title/HTML/date parsing |

### Document Processing

| Module | Tech Stack | Main Features |
|--------|------------|---------------|
| **docx** | docx-js, OOXML | Create/Edit/Analyze, Track Changes |
| **xlsx** | pandas, openpyxl | Formula calculation, Financial modeling |
| **pptx** | html2pptx, OOXML | HTML to PPT, Template reuse |
| **pdf** | pypdf, pdfplumber, reportlab | Form filling, OCR |

### Design System

| Module | Description |
|--------|-------------|
| **canvas-design** | Visual art creation with 40+ open-source fonts |
| **frontend-design** | Design Token system, React + Tailwind CSS, WCAG AA compliance |

## Quick Start

### Install SDK

```bash
npm install z-ai-web-dev-sdk
```

### Basic Usage

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

### CLI Tool

Use the `z-ai` CLI for quick testing:

```bash
# Speech recognition
z-ai asr --file audio.mp3

# Image generation
z-ai image --prompt "a beautiful sunset"

# Web search
z-ai search --query "latest AI news"
```

## Skill Document Structure

Each skill module follows a unified structure:

```
skill-name/
├── SKILL.md         # Core documentation (YAML Frontmatter + Markdown)
├── LICENSE.txt      # License
├── scripts/         # Example scripts (TypeScript)
└── [references]     # Optional supplementary docs
```

## Important Notes

1. **Backend Only**: `z-ai-web-dev-sdk` must be used in backend code only
2. **TTS Limit**: Max 1024 characters per request, chunk long text accordingly
3. **Async Tasks**: Image/video generation uses async mode, implement polling logic
4. **Document Editing**: Read the corresponding OOXML reference docs before editing Office documents

## License

- **MIT License**: ASR, TTS, LLM, VLM, image-generation, video-generation, web-search, web-reader, frontend-design
- **Proprietary**: canvas-design, document-skills (see LICENSE.txt in each module)
