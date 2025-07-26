from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Customer API"
    VERSION: str = "1.0"
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/intropy-test"


settings = Settings()