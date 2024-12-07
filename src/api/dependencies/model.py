from adapters.language_model import OpenAiLanguageModel, client
from domain.ports.language_model import LanguageModel


def get_model() -> LanguageModel:
    return OpenAiLanguageModel(client)