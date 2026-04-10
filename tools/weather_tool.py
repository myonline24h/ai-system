from google.adk.tools import FunctionTool

def get_weather(city: str) -> str:
    """Tra cứu thời tiết của một thành phố."""
    weather_data = {
        "hanoi": "Nhiều mây, 25°C",
        "saigon": "Nắng đẹp, 32°C",
        "danang": "Có mưa rào, 28°C"
    }
    return weather_data.get(city.lower(), f"Không có dữ liệu thời tiết cho {city}")

weather_tool = FunctionTool(func=get_weather)
