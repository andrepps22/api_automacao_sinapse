from pydantic import BaseModel


class LeadSchema(BaseModel):
    codigo_lead: int
    nome_lead: str
    etapa_lead: str
    cliente_novo: bool
    canal_vendas: int # vai buscar na tabela onde estão cadastrados os canais de vendas