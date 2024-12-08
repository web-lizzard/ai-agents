from abc import ABC, abstractmethod

from src.logger import logger

from ..commands import BaseResponse, Command


class CommandHandler(ABC):
    async def handle(self, command: Command) -> BaseResponse:
        logger.info(
            f"Command: {self.__class__.__name__} executes with params: {command}"
        )
        return await self._handle(command)

    @abstractmethod
    async def _handle(self, command: Command) -> BaseResponse:
        ...
