from datetime import date
from typing import Optional

from pydantic import BaseModel


class ReceitasSchemas(BaseModel):
    descricao: str
    valor: float
    data: date


class ReceitasSchemasGet(ReceitasSchemas):
    id: Optional[int]
    