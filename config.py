# config.py

import os
from dotenv import load_dotenv

load_dotenv()

# API Keys and URLs
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE_URL = "https://api.302.ai/v1/"

ANTHROPIC_API_KEY = OPENAI_API_KEY
ANTHROPIC_API_BASE_URL = "https://api.302.ai/"

# LLM Parameters
TEMPERATURE = 0.7
MAX_TOKENS = 1024
TIMEOUT = None
MAX_RETRIES = 2

# logger 中输出这些参数
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(f"temperature: {TEMPERATURE}")
logger.info(f"max_tokens: {MAX_TOKENS}")
logger.info(f"timeout: {TIMEOUT}")
logger.info(f"max_retries: {MAX_RETRIES}")




MEMORY_RETENTION_DAYS = 7

AVAILABLE_MODELS = [
    "gpt-3.5-turbo",
    "gpt-4o",
    "gpt-4o-mini",
    "claude-3-haiku-20240307",
    "claude-3-opus-20240229",
    "claude-3-5-sonnet-20240620",
    "claude-3-5-sonnet-20241022",
    # Add other models if needed
]

if not OPENAI_API_KEY:
    raise ValueError("未设置 OPENAI_API_KEY 环境变量。请按照 README.md 中的说明进行设置。")