from typing import Iterable

from openai import AsyncOpenAI

from src.domain.exceptions import LanguageModelError


class OpenAiLanguageModel:

    def __init__(self, client: AsyncOpenAI) -> None:
        self._client = client
    
    async def generate(self, model: str, messages: Iterable, temperature: float, seed: int) -> str:  # noqa: F821
        response = await self._client.chat.completions.create(model=model, messages=messages, temperature=temperature, seed=seed)

        if not len(response.choices):
            raise LanguageModelError

        return response.choices[0].message.content or ''


