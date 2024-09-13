from pydantic import BaseModel
from typing import Optional


class UsuarioSchemas(BaseModel):
    username: str
    email: str


class UsuarioIdSchemas(UsuarioSchemas):
    id: Optional[int]


class UsuarioSenhaSchemas(UsuarioSchemas):
    senha: str
