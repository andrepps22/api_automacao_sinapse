from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from core.criar_codigo import criar_codigo


class ProprietarioSchema(BaseModel):
    id_proprietario: Optional[str] = Field(default_factory=lambda: criar_codigo('Corretor'))
    nome: str
    cpf: str
    endereco: str
    data_nascimento: datetime

