from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CorretorSchema(BaseModel):
    nome: str
    cpf: str
    endereco: str
    celular: str
    
    
class CorretorPublicSchema(CorretorSchema):
    id_corretor: int