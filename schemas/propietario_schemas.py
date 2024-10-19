from pydantic import BaseModel
from datetime import datetime

class PropietarioSchema(BaseModel):
    nome: str
    cpf: str
    endereco: str
    data_nascimento: datetime