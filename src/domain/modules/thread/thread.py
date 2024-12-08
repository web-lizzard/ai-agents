from src.domain.ports.language_model import LanguageModel

from .prompts import generate_reply, generate_summarization

_previous_summary = ""


class ThreadService:
    def __init__(self, model: LanguageModel) -> None:
        self._model = model

    async def make_response(self, query: str, model: str) -> str:
        global _previous_summary
        message = await self._model.generate(
            model=model,
            messages=[
                {"role": "system", "content": generate_reply(_previous_summary)},
                {"role": "user", "content": query},
            ],
        )

        _previous_summary = await self._generate_summarization(
            user_message=query, assistant_message=message
        )

        return message

    async def _generate_summarization(
        self, user_message: str, assistant_message: str
    ) -> str:
        return await self._model.generate(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": generate_summarization(
                        _previous_summary,
                        user_message,
                        assistant_response=assistant_message,
                    ),
                }
            ],
        )
