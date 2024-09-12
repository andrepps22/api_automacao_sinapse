from pydantic import BaseModel
from typing import Optional
from datetime import date


class ReceitasSchemas(BaseModel):
    descricao: str
    valor: float
    data: date


class ReceitasSchemasGet(ReceitasSchemas):
    id: Optional[int]
    