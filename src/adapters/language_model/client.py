from openai import AsyncOpenAI

from src.settings import settings

client = AsyncOpenAI(api_key=settings.openai.api_key)