from pydantic import BaseModel


class LeadSchema(BaseModel):
    nome_lead: str
    etapa_lead: str
    cliente_novo: bool
    canal_vendas: int # vai buscar na tabela onde estão cadastrados os canais de vendas
    
    
class LeadPublicSchema(LeadSchema):
    codigo_lead: int