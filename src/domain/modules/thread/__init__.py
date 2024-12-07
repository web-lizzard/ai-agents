from typing import Iterable, Protocol

from openai import AsyncOpenAI


class LanguageModel(Protocol):

    async def generate(self, model: str, messages: Iterable, temperature: float, seed: int) -> str:
        ...






