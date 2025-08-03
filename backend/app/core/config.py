from pydantic_settings import BaseSettings, SettingsConfigDict
from datetime import timedelta

class Settings(BaseSettings):
    PROJECT_NAME: str = 'Movie Booking System'
    API_PREFIX: str = '/api/v1'
    ALGORITHM: str = 'HS256'
    EXPIRES_DELTA: timedelta = timedelta(hours=1)
    DATABASE_URL: str
    SECRET_KEY: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

settings = Settings()
