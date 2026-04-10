from google.adk.agents import Agent
from config import MODEL_NAME
from tools.weather_tool import weather_tool

weather_agent = Agent(
    name="WeatherAgent",
    model=MODEL_NAME,
    instruction="Bạn là chuyên gia thời tiết. Hãy sử dụng tool 'get_weather' để cung cấp thông tin chính xác.",
    description="Chuyên trách tra cứu và cung cấp thông tin thời tiết.",
    tools=[weather_tool]
)
