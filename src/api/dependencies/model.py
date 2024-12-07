from src.adapters.language_model import OpenAiLanguageModel, client
from src.domain.ports.language_model import LanguageModel


def get_model() -> LanguageModel:
    return OpenAiLanguageModel(client)