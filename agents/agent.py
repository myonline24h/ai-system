from google.adk.agents import Agent
from config import MODEL_NAME
from agents.greeting_agent import greeting_agent
from agents.weather_agent import weather_agent

root_agent = Agent(
    name="TeamLeader",
    model=MODEL_NAME,
    instruction="Bạn là trưởng nhóm điều phối. Hãy chào hỏi người dùng thông qua GreetingAgent và trả lời câu hỏi thời tiết thông qua WeatherAgent. Đừng tự trả lời nếu có thể điều phối cho các agent chuyên trách.",
    sub_agents=[greeting_agent, weather_agent]
)
