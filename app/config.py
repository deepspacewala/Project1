from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    """Application settings"""
    DATA_DIR: Path = Path("./data")
    OPENAI_API_KEY: str = ""
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_FILE_TYPES: list = [".txt", ".md", ".json", ".sql", ".log"]
    
    class Config:
        env_file = ".env"

settings = Settings() 