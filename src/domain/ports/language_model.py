from typing import Iterable, Protocol


class LanguageModel(Protocol):

    async def generate(self, model: str, messages: Iterable, temperature: float, seed: int) -> str:
        ...
