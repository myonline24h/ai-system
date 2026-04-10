import asyncio
import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import FunctionTool

# Cấu hình model sử dụng LiteLLM (Gemini qua Google API Key)
# Đảm bảo bạn đã set biến môi trường GOOGLE_API_KEY
model_name = "gemini/gemini-1.5-flash"

# 1. Định nghĩa Tool cho Weather Agent
def get_weather(city: str) -> str:
    """Tra cứu thời tiết của một thành phố."""
    # Giả lập dữ liệu thời tiết
    weather_data = {
        "hanoi": "Nhiều mây, 25°C",
        "saigon": "Nắng đẹp, 32°C",
        "danang": "Có mưa rào, 28°C"
    }
    return weather_data.get(city.lower(), f"Không có dữ liệu thời tiết cho {city}")

weather_tool = FunctionTool(func=get_weather)

# 2. Định nghĩa các Sub-Agents
greeting_agent = Agent(
    name="GreetingAgent",
    model=model_name,
    instruction="Bạn là trợ lý chào hỏi. Hãy chào người dùng một cách thân thiện và ngắn gọn.",
    description="Chuyên trách chào hỏi và mở đầu cuộc hội thoại."
)

weather_agent = Agent(
    name="WeatherAgent",
    model=model_name,
    instruction="Bạn là chuyên gia thời tiết. Hãy sử dụng tool 'get_weather' để cung cấp thông tin chính xác.",
    description="Chuyên trách tra cứu và cung cấp thông tin thời tiết.",
    tools=[weather_tool]
)

# 3. Định nghĩa Root Agent (Team Leader)
root_agent = Agent(
    name="TeamLeader",
    model=model_name,
    instruction="Bạn là trưởng nhóm điều phối. Hãy chào hỏi người dùng thông qua GreetingAgent và trả lời câu hỏi thời tiết thông qua WeatherAgent. Đừng tự trả lời nếu có thể điều phối cho các agent chuyên trách.",
    sub_agents=[greeting_agent, weather_agent]
)

async def main():
    # Khởi tạo Runner và Session Service
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        session_service=session_service
    )

    print("--- Agent Team Started (Type 'exit' to quit) ---")
    user_id = "user_123"
    session_id = "session_456"

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            break

        # Chạy agent và in kết quả
        response = await runner.run_async(
            input=user_input,
            user_id=user_id,
            session_id=session_id
        )
        
        # In các event từ các agent khác nhau để thấy sự điều phối
        for event in response.events:
            if event.content and event.content.parts:
                text = event.content.parts[0].text
                if text:
                    print(f"[{event.author}]: {text}")

if __name__ == "__main__":
    asyncio.run(main())
