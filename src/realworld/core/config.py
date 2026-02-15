import os

from functools import lru_cache
from typing import Literal, Type, cast
from pathlib import Path

from pydantic import PostgresDsn
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)

BASE_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    database_url: PostgresDsn
    env: Literal["dev", "prod"] = cast(
        Literal["dev", "prod"], os.getenv("ENV", "dev").lower()
    )
    model_config = SettingsConfigDict(toml_file=f"{BASE_DIR}/config/{env}.toml")

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (TomlConfigSettingsSource(settings_cls),)


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
