# AI System Project (Google ADK)

This project is a multi-agent AI system built using the **Google Agent Development Kit (ADK)** and **LiteLLM**. It implements a coordinated team of agents to handle user greetings and weather inquiries.

## Project Overview

- **Purpose**: Demonstrate a multi-agent coordination pattern (TeamLeader/Sub-Agents) using Google ADK.
- **Main Technologies**:
  - [Google ADK](https://github.com/google/adk): Framework for building and running AI agents.
  - [LiteLLM](https://github.com/BerriAI/litellm): Unified interface to various LLM providers (configured for local Ollama).
  - [Ollama](https://ollama.ai/): Local LLM backend.
  - [uv](https://github.com/astral-sh/uv): Python package and project manager.

## Architecture

The system follows a hierarchical agent structure:
- **`TeamLeader` (`agents/agent.py`)**: The root agent responsible for planning and delegating tasks to specialized sub-agents.
- **`GreetingAgent` (`agents/greeting_agent.py`)**: Specialized in friendly greetings and conversation openers.
- **`WeatherAgent` (`agents/weather_agent.py`)**: Specialized in weather information, utilizing a dedicated tool.
- **`WeatherTool` (`tools/weather_tool.py`)**: A functional tool that provides mock weather data for major Vietnamese cities (Hanoi, Saigon, Danang).

## Building and Running

### Prerequisites
- Python >= 3.12
- [Ollama](https://ollama.ai/) installed and running.
- Model `qwen2.5:7b` (or similar) pulled in Ollama: `ollama pull qwen2.5:7b`.

### Setup
1. Install dependencies using `uv`:
   ```bash
   uv sync
   ```
   *Alternatively, use pip: `pip install -e .`*

2. Configure environment variables for Ollama (if not already set):
   ```bash
   export OLLAMA_API_BASE="http://localhost:11434"
   ```

### Execution
Run the interactive CLI:
```bash
python main.py
```

## Testing and Evaluation

The project uses `pytest` and ADK's built-in `AgentEvaluator` for verification.

- **Run unit tests**:
  ```bash
  pytest
  ```
- **Evaluation**: The `tests/test_agents.py` uses `AgentEvaluator.evaluate` to test agent behavior against a dataset defined in `tests/agent_test.test.json`.

## Development Conventions

- **Agent Definitions**: Agents are defined using the `Agent` class from `google.adk.agents`. Each agent should have a clear `name`, `instruction`, and optional `description` and `tools`.
- **Tool Definitions**: Tools are created using `FunctionTool` wrapping standard Python functions with docstrings that explain their purpose and parameters to the LLM.
- **Configuration**: LLM model configurations are centralized in `config.py`.
- **Asynchronous Execution**: The system utilizes Python's `asyncio` for non-blocking agent runs.

## Key Files
- `main.py`: Interactive CLI entry point.
- `config.py`: Centralized LLM and environment configuration.
- `agents/`: Directory containing all agent definitions.
- `tools/`: Directory containing tool implementations.
- `tests/`: Directory containing Pytest suites and evaluation datasets.
- `pyproject.toml`: Project metadata and dependencies.
