from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class OpenAiSettings(BaseModel):
    api_key: str


class Settings(BaseSettings):

    openai: OpenAiSettings

    model_config = SettingsConfigDict(env_nested_delimiter='__', env_file='.env')

settings = Settings()