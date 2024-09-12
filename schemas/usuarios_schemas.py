from pydantic import BaseModel
from typing import Optional


class UsuarioSchemas(BaseModel):
    id: Optional[int]
    nome: str
    email: str
    hash: str