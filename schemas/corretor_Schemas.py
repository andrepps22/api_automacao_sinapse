from pydantic import BaseModel
from datetime import datetime


class CorretorSchema(BaseModel):
    id_corretor: int
    nome: str
    cpf: str
    endereco: str
    celular: str
    data_nascimento: datetime