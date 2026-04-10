from google.adk.agents import Agent
from config import MODEL_NAME

greeting_agent = Agent(
    name="GreetingAgent",
    model=MODEL_NAME,
    instruction="Bạn là trợ lý chào hỏi. Hãy chào người dùng một cách thân thiện và ngắn gọn.",
    description="Chuyên trách chào hỏi và mở đầu cuộc hội thoại."
)
