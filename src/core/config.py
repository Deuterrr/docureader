from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """
    Application configuration loaded from environment variables or .env file.
    Model and CSV paths, and service credentials go here.
    """
    APP_NAME: str

    KTP_DETECT_MODEL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        # extra="ignore"
    )


configs = Config()
