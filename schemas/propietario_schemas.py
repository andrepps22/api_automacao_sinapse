from pydantic import BaseModel
from datetime import datetime


class PropietarioSchema(BaseModel):
    nome: str
    cpf: str
    endereco: str
    data_nascimento: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class PropietarioIDSchema(PropietarioSchema):
    id_propietario: int