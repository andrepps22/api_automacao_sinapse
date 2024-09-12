from pydantic import BaseModel
from typing import Optional
from datetime import date


class DespesasSchemas(BaseModel):
    descricao: str
    valor: float
    data: date  # Certifique-se de usar o tipo `date`
    categoria: str = 'Outras'

class DespesasSchemasGet(BaseModel):
    id: Optional[int]
    descricao: str
    valor: float
    data: date  # Certifique-se de usar o tipo `date`
    categoria: str = 'Outras'