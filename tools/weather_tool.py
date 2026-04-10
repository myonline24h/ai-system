from google.adk.tools import FunctionTool

def get_weather(city: str) -> str:
    """Tra cứu thời tiết của một thành phố."""
    city_map = {
        "hanoi": "hanoi", "hà nội": "hanoi",
        "saigon": "saigon", "sài gòn": "saigon", "tp hcm": "saigon", "ho chi minh": "saigon",
        "danang": "danang", "đà nẵng": "danang"
    }
    
    clean_city = city.lower().strip()
    target_city = city_map.get(clean_city, clean_city)

    weather_data = {
        "hanoi": "Nhiều mây, 25°C",
        "saigon": "Nắng đẹp, 32°C",
        "danang": "Có mưa rào, 28°C"
    }
    return weather_data.get(target_city, f"Không có dữ liệu thời tiết cho {city}")

weather_tool = FunctionTool(func=get_weather)
