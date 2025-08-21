# AI-Powered Agent

This project is an intelligent agent capable of detecting and automatically fixing an operator precedence bug.

## Features

- **CLI calculator** with support for basic arithmetic: addition, subtraction, multiplication, division.
- **Operator precedence** is correctly implemented (`*`/`/` higher than `+`/`-`).
- **AI Agent** (in `main.py`) can:
  - Read calculator source files
  - Detect operator precedence bugs
  - Automatically fix bugs in code via file editing

## Project Structure

.
├── calculator/
│ ├── main.py # Calculator CLI entry point
│ └── pkg/
│ └── calculator.py # Calculator logic and operator precedence
├── main.py # AI Agent entry point
├── requirements.txt
└── README.md


## Setup & Usage

Installation

Clone the repository and navigate to the project folder.

```sh

git clone <your-repo-url>
cd <your-repo-folder>

Set up your Python environment:

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Running the Calculator CLI
uv run calculator/main.py "3 + 7 * 2"

Running the AI Agent
uv run main.py "fix the bug: 3 + 7 * 2 shouldn't be 20"

Regards and Thnx
