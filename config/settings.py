"""Application settings, loaded from the environment and .env"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    ENVIRONMENT: str = "development"
    DATABASE_URI: str


settings = Settings()
