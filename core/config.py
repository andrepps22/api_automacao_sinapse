from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.orm import registry


class Setting(BaseSettings):
    API_VERSION: str = '/api/v1'
    JWT_SECRET: str = 'CYZ7spPeiGu2soM7W9igWynKe1sPDkUBayzjq9n3ZKY'
    ALGORITHM: str = 'HS256'
    ACESS_TOKEN_EXPIRE_MINUTES: int = 10080  # minutos 1 semana
    DB_URL: ClassVar = 'postgresql+asyncpg://postgres:123456@localhost:5432/orcamento'
    DBModelReg: ClassVar = registry()

    """
    import secrets
    token: str = secrets.token_urlsafe(32)
    
    """

    class Config:
        case_sensitive = True


setting = Setting()


