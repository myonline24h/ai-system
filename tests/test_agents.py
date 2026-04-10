from google.adk.evaluation.agent_evaluator import AgentEvaluator
import pytest
import os

@pytest.mark.anyio
async def test_agent_eval():
    """Test the agent's behavior using the evaluation set."""
    # Ensure current directory is in PYTHONPATH for agent_module to work
    import sys
    sys.path.append(os.getcwd())
    
    await AgentEvaluator.evaluate(
        agent_module="agents.agent",
        eval_dataset_file_path_or_dir="tests/agent_test.test.json",
    )
