# config.py

import os
from dotenv import load_dotenv

#
# 加载.env文件中的环境变量
load_dotenv()

# 从环境变量中获取OpenAI API密钥
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENAI_API_BASE_URL="https://api.302.ai/v1/"

# 设置记录保留的天数
MEMORY_RETENTION_DAYS = 7





AVAILABLE_MODELS = [
    "gpt-3.5-turbo-instruct",
    "gpt-4o",
    # 添加其他您希望支持的模型
]

# 临时调试代码（请勿在生产环境中保留）
if not OPENAI_API_KEY:
    raise ValueError("未设置 OPENAI_API_KEY 环境变量。请按照 README.md 中的说明进行设置。")
