from typing import ClassVar

from pydantic_settings import BaseSettings
from sqlalchemy.orm import registry


class Setting(BaseSettings):
    API_VERSION: str = '/api/v1'
    JWT_SECRET: str = 'k8tO7kz3OG0s4JNyf0x_920AvY0A8DmbxVMpK7RSdpYt06lL78W9ZNPZUl7wHOClaPo7qCZMYGeSLhsSEeed2B1ztWOQfwKNPusQNqStj0wDJh9aMPW-xAu7gfPCRUJYFmBrM6Yz3FfYXhGM8MB7lyTLRZNDQkVUI4ZiyME7OAcQFdrYAU3UCtN7aKcjCVV2S-7c06oCVm640wHe1tt3Ff3gU-egjfOGwe1fKlB40edSvoKjYFJAJdPyvwvTaMS0DBIDeDb4Fa_YZ-e98bvArMyjfkifi5Bwlq7thcEPISEYsFqrx5jI4hoP1Jqw4oNxQHxynGc84rKrLb7pLwdHP6CBwfUvqZdxyQ'
    ALGORITHM: str = 'HS256'
    ACESS_TOKEN_EXPIRE_MINUTES: int = 120  # minutos 1 semana
    DB_URL: ClassVar = 'postgresql+asyncpg://postgres:123456@localhost:5432/orcamento'
    DBModelReg: ClassVar = registry()


    class Config:
        case_sensitive = True


setting = Setting()


