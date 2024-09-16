from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UsuarioSchemas(BaseModel):
    username: str
    email: str


class UsuarioSenhaSchemas(UsuarioSchemas):
    senha: str

class UsuarioPublicoSchemas(UsuarioSchemas):
    id: Optional[int]
    criado_em: datetime
