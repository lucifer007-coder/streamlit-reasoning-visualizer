# Streamlit Reasoning Visualizer

[![PyPI version](https://img.shields.io/pypi/v/streamlit-reasoning-visualizer.svg)](https://pypi.org/project/streamlit-reasoning-visualizer/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Streamlit](https://img.shields.io/badge/Streamlit-Component-FF4B4B?logo=streamlit)](https://streamlit.io/)

A beautiful, interactive Streamlit component for visualizing LLM reasoning processes with collapsible thought sections and rich markdown/LaTeX rendering.

![Reasoning Visualizer Demo](https://raw.githubusercontent.com/ketanmahandule/streamlit-reasoning-visualizer/main/assets/demo.gif)

## ✨ Features

- **🧠 Collapsible Reasoning Section** - Hide/show the model's chain-of-thought with smooth animations
- **📝 Rich Markdown Rendering** - Full markdown support including code blocks, tables, and formatting
- **🔢 LaTeX Math Support** - Beautiful equation rendering with KaTeX, including `\boxed{}` expressions
- **🏷️ Multi-format Tag Parsing** - Supports various reasoning tag formats used by different LLMs
- **🎨 Modern UI** - Clean, minimalist design with smooth animations using Framer Motion

## 📦 Installation

```bash
pip install streamlit-reasoning-visualizer
```

## 🚀 Quick Start

```python
import streamlit as st
from reasoning_visualizer import visualizer

st.title("Reasoning Visualizer Demo")

# Sample response with reasoning tags
response = """<think>
Let me work through this step by step.
1. First, I need to understand the problem
2. Then, I'll apply the relevant formula
3. Finally, I'll calculate the result

Using the quadratic formula: $x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}$
</think>

The answer is **42**.

$$\\boxed{x = 42}$$
"""

visualizer(text=response)
```

## 🏷️ Supported Reasoning Tag Formats

The component automatically detects and parses these tag formats:

| Format | Example |
|--------|---------|
| `<think>` | `<think>reasoning...</think>` |
| `[THOUGHT]` | `[THOUGHT]reasoning...[/THOUGHT]` |
| `<reasoning>` | `<reasoning>reasoning...</reasoning>` |
| `<chain_of_thought>` | `<chain_of_thought>reasoning...</chain_of_thought>` |

If no tags are found, the entire text is displayed as the final answer.

## 📖 API Reference

### `visualizer(text, key=None)`

Render the Reasoning Visualizer component.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `text` | `str` | The raw text containing reasoning tags and the answer |
| `key` | `str`, optional | Unique key for multiple visualizer instances |

**Example with multiple visualizers:**

```python
visualizer(text=response1, key="viz1")
visualizer(text=response2, key="viz2")
```

## 🔧 Development

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm

### Setup

1. Clone the repository:
```bash
git clone https://github.com/ketanmahandule/streamlit-reasoning-visualizer.git
cd streamlit-reasoning-visualizer
```

2. Install Python dependencies:
```bash
pip install -e ".[dev]"
```

3. Install frontend dependencies:
```bash
cd reasoning_visualizer/frontend
npm install
```

4. Start development mode:

In `reasoning_visualizer/__init__.py`, set `_RELEASE = False`, then:

```bash
# Terminal 1: Start the React dev server
cd reasoning_visualizer/frontend
npm start

# Terminal 2: Run the example app
streamlit run example.py
```

### Building the Frontend

```bash
cd reasoning_visualizer/frontend
npm run build
```

### Running Tests

```bash
pytest tests/ -v
```

### Demo

<img width="1767" height="442" alt="image" src="https://github.com/user-attachments/assets/ab950d59-bfa7-4890-860d-c30244f4a6c8" />

<img width="1762" height="397" alt="image" src="https://github.com/user-attachments/assets/45307819-4ae4-4670-a566-01a17b8b7858" />

<img width="1752" height="792" alt="image" src="https://github.com/user-attachments/assets/29909fc8-243d-48e7-a763-a57dc6d8f1cf" />

<img width="1766" height="551" alt="image" src="https://github.com/user-attachments/assets/26858bc6-e16e-475e-9139-0537e359a3ec" />


## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Animations powered by [Framer Motion](https://www.framer.com/motion/)
- Math rendering by [KaTeX](https://katex.org/)
- Icons from [Lucide React](https://lucide.dev/)

