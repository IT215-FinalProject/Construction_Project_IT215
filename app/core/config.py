from pydantic_settings import BaseSettings


# Đọc cấu hình từ file .env
class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()