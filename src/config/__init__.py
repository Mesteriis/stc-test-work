__all__ = ["settings"]

from pydantic import BaseConfig
from .db import SettingsDB


class Settings(BaseConfig):
    title: str = "тестовое задание"
    project_version: str = "1.0.0"
    project_description: str = "Для служебного использования"

    env: str = "dev"
    port: int = 8000

    db: SettingsDB = SettingsDB()

    @property
    def debug(self) -> bool:
        return self.env == "dev"

    class Config:
        env_prefix = "api_"
        validate_assignment = True


settings = Settings()
