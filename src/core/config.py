from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GROQ_API_KEY: str
    ELEVENLABS_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = Settings()
