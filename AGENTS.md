# AGENTS.md

## Project
Multi-agent AI system using Google ADK + LiteLLM + Ollama.

## Dev Commands
```bash
uv sync --dev          # Install dependencies
python main.py         # Run interactive CLI
pytest                 # Run all tests
pytest tests/test_weather_tool.py  # Run unit tests only
```

## Setup Requirements
- Python >= 3.12
- [Ollama](https://ollama.ai/) running at `localhost:11434`
- Model: `qwen3.5:9b` (pull with `ollama pull qwen3.5:9b`)

## Model Config (`config.py`)
- **Prefix**: Use `ollama_chat/` not `ollama/` to avoid infinite tool-call loops
- Current: `MODEL_NAME = LiteLlm(model="ollama_chat/qwen3.5:9b")`

## Architecture
```
root_agent (TeamLeader)
├── greeting_agent  → greetings
└── weather_agent  → weather queries
    └── weather_tool (get_weather)
```

## Testing Notes
- `test_weather_tool.py` - Pure unit tests, no Ollama needed
- `test_agents.py` - Uses `AgentEvaluator.evaluate`, requires running Ollama
- CI only runs `test_weather_tool.py` (excludes eval tests)
- `test_agents.py` appends `os.getcwd()` to `PYTHONPATH` for agent module import

## Key Files
| File | Purpose |
|------|---------|
| `main.py` | CLI entry point |
| `config.py` | LLM model config |
| `agents/agent.py` | Root agent (TeamLeader) |
| `agents/greeting_agent.py` | Greeting sub-agent |
| `agents/weather_agent.py` | Weather sub-agent |
| `tools/weather_tool.py` | `get_weather` function tool |
| `tests/agent_test.test.json` | AgentEvaluator eval dataset |
