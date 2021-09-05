from pydantic import BaseSettings


class Settings(BaseSettings):

    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DB: str
    MYSQL_SERVER: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
