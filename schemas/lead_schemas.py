from pydantic import BaseModel
from typing import Optional


class LeadSchema(BaseModel):
    codigo_lead: int
    Tipo_post: Optional[str]
    nome_lead: str
    campanha: str
    numero_lead_celular: str
 