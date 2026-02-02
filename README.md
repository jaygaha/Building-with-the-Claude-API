# Building with the Claude API

This repository contains hands-on exercises and examples from the [Anthropic course: Building with the Claude API](https://github.com/anthropics/courses/tree/master/building_with_claude_api).

## Modules

### Module 1: Accessing Claude with the API

Learn the fundamentals of interacting with Claude through the Anthropic API.

| Notebook | Description |
|----------|-------------|
| `001_requests.ipynb` | Basic API requests, message handling, and multi-turn conversations |
| `001_requests_exercise.ipynb` | Build an interactive chatbot using the messages API |
| `002_system_prompt.ipynb` | Using system prompts to guide Claude's behavior |
| `002_system_prompt_exercise.ipynb` | Create a concise Python code assistant with system prompts |
| `003_temperature.ipynb` | Controlling output randomness with the temperature parameter |
| `004_streaming.ipynb` | Real-time response streaming and handling stream events |
| `005_controlling_output.ipynb` | Message prefilling, stop sequences, and structured output (JSON) |

## Setup

### Prerequisites

- Python 3.8+
- An Anthropic API key ([Get one here](https://console.anthropic.com/))

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jaygaha/Building-with-the-Claude-API.git
   cd Building-with-the-Claude-API
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your API key:
   ```bash
   cp .env-example .env
   ```
   Then edit `.env` and add your Anthropic API key.

5. Launch Jupyter:
   ```bash
   jupyter notebook
   ```

## Resources

- [Anthropic API Documentation](https://docs.anthropic.com/)
- [Claude API Reference](https://docs.anthropic.com/en/api/getting-started)
- [Anthropic Courses](https://github.com/anthropics/courses)
