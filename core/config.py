from typing import ClassVar
import os

from pydantic_settings import BaseSettings
from sqlalchemy.orm import registry


class Setting(BaseSettings):
    

    API_VERSION: str = '/api/v1'
    JWT_SECRET: str = os.environ.get('JWT_SECRET')
    ALGORITHM: str = os.environ.get('ALGORITHM')
    ACESS_TOKEN_EXPIRE_MINUTES: int
    DB_URL: str = os.environ.get('DB_URL')
    DBModelReg: ClassVar = registry()


    class Config:
        case_sensitive = True
        env_file='.env'


setting = Setting()


