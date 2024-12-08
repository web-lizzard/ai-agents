from src.domain.modules.thread import ThreadService
from src.domain.ports.language_model import LanguageModel

from ..commands import BaseResponse, Command
from .base import CommandHandler


class ThreadHandler(CommandHandler):
    _service: ThreadService

    def __init__(self, model: LanguageModel) -> None:
        self._service = ThreadService(model)

    async def _handle(self, command: Command) -> BaseResponse:
        response = await self._service.make_response(
            command.user_request, model=command.model
        )

        return BaseResponse(assistant_message=response)
