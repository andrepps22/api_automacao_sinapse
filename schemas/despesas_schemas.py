from pydantic import BaseModel
from typing import Optional
from datetime import date
from typing import Literal, Optional





class DespesasSchemas(BaseModel):
    descricao: str
    valor: float
    data: date  # Certifique-se de usar o tipo `date`
    categoria: Optional[Literal["Alimentação",
    "Saúde",
    "Moradia",
    "Transporte",
    "Educação",
    "Lazer",
    "Imprevistos",
    "Outras"]] = 'Outras'

class DespesasSchemasGet(DespesasSchemas):
    id: Optional[int]
    