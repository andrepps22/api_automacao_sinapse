from pydantic import BaseModel
from typing import Optional


class LeadSchema(BaseModel):
    nome_lead: str
    etapa_lead: str
<<<<<<< HEAD
    cliente_novo: bool
    canal_vendas: int # vai buscar na tabela onde estão cadastrados os canais de vendas
    
    
class LeadPublicSchema(LeadSchema):
    codigo_lead: int
=======
    cliente_novo: Optional[bool] = None
    canal_vendas: Optional[int]  = None# vai buscar na tabela onde estão cadastrados os canais de vendas
>>>>>>> d71c6a34b7c2c5dc52c3dbe59dadb50dc87da345
