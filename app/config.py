from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Настройки для подключения к БД"""
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()
