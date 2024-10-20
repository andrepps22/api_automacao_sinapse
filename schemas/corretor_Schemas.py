from pydantic import BaseModel
from datetime import datetime


class CorretorSchema(BaseModel):
    nome: str
    cpf: str
    endereco: str
    celular: str
    data_nascimento: datetime
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }