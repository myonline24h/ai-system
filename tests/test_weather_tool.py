import pytest
from tools.weather_tool import get_weather

def test_get_weather_success():
    assert get_weather("hanoi") == "Nhiều mây, 25°C"
    assert get_weather("Hà Nội") == "Nhiều mây, 25°C"
    assert get_weather("Sài Gòn") == "Nắng đẹp, 32°C"
    assert get_weather("SAIGON") == "Nắng đẹp, 32°C"
    assert get_weather("danang") == "Có mưa rào, 28°C"
    assert get_weather("Đà Nẵng") == "Có mưa rào, 28°C"

def test_get_weather_unknown_city():
    city = "London"
    assert get_weather(city) == f"Không có dữ liệu thời tiết cho {city}"
