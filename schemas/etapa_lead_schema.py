from pydantic import BaseModel


class EtapaleadSchema(BaseModel):
    codigo_lead: int
    etapa_lead: str