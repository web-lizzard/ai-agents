from typing import Annotated

from fastapi import Depends, Header

from src.adapters.language_model import OpenAiLanguageModel, client
from src.application.commands.handlers import CommandHandler, ThreadHandler
from src.domain.ports.language_model import LanguageModel


def get_model() -> LanguageModel:
    return OpenAiLanguageModel(client)


def get_command_handler(
    model: Annotated[LanguageModel, Depends(get_model)],
    handler_name: str = Header("thread"),
) -> CommandHandler:
    return ThreadHandler(model)
