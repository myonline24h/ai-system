import os
from google.adk.models.lite_llm import LiteLlm

# Cấu hình Ollama
# Bạn cần chạy: export OLLAMA_API_BASE="http://localhost:11434"
os.environ["OLLAMA_API_BASE"] = "http://localhost:11434"

# Sử dụng model qwen2.5 (giả định bạn dùng bản 7b hoặc 14b, tôi để qwen2.5 theo ý bạn)
# Lưu ý: Dùng ollama_chat để tránh lỗi vòng lặp tool call
MODEL_NAME = LiteLlm(model="ollama_chat/qwen3.5:9b")
