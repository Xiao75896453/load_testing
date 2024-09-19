from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    STAGE: str
    SERVICE_PORT: int
    WORKERS: int
    HOST: str

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_DATABASE: str
    DB_POOL_SIZE: int
    DB_MAX_OVERFLOW: int
    DB_POOL_RECYCLE: int

    class Config:
        env_file = ".env"


settings = Settings()
