import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from agents.agent import root_agent

async def main():
    # Khởi tạo Runner và Session Service
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        session_service=session_service
    )

    print("--- ADK Agent Team (Refactored) ---")
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
        
        for event in response.events:
            if event.content and event.content.parts:
                text = event.content.parts[0].text
                if text:
                    print(f"[{event.author}]: {text}")

if __name__ == "__main__":
    asyncio.run(main())
