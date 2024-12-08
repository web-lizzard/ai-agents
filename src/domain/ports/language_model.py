from typing import Iterable, Protocol


class LanguageModel(Protocol):
    async def generate(
        self, model: str, messages: Iterable, temperature: float = 0, seed: int = 0
    ) -> str:
        ...
