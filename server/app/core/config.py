import os
from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "ITACATI Contact Center"
    app_version: str = "0.1.0"
    environment: str = os.getenv("APP_ENV", "dev")


settings = Settings()