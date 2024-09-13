from datetime import date
from typing import Literal, Optional

from pydantic import BaseModel


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
    