from pydantic import BaseModel
from datetime import datetime

class PropietarioSchema(BaseModel):
    id_propietario: int
    nome: str
    cpf: str
    endereco: str
    data_nascimento: datetime