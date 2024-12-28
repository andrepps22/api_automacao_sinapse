from pydantic import BaseModel, Field
from typing import Optional
from core.criar_codigo import criar_codigo

class CorretorSchema(BaseModel):
    id_corretor: Optional[str] = Field(default_factory=lambda: criar_codigo('Corretor'))
    nome: str
    cpf: str
    endereco: str
    celular: str
