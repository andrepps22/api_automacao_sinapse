from pydantic import BaseModel
from datetime import datetime


class ProprietarioSchema(BaseModel):
    nome: str
    cpf: str
    endereco: str
    data_nascimento: datetime


class PropietarioIDSchema(ProprietarioSchema):
    id_propietario: int