from pydantic import BaseModel
from typing import Optional


class LeadSchema(BaseModel):
    codigo_lead: int
    nome_lead: str
    etapa_lead: str
    cliente_novo: Optional[bool] = None
    canal_vendas: Optional[int]  = None# vai buscar na tabela onde estão cadastrados os canais de vendas