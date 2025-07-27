from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Customer API"
    VERSION: str = "1.0"
    DATABASE_PASSWORD: str

    class Config:
        env_file = ".env"

    @property
    def DATABASE_URL(self):
        return f"postgresql://postgres:{self.DATABASE_PASSWORD}@localhost:5432/intropy-test"

settings = Settings()