from core.config import setting
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


reg = setting.DBModelReg


@reg.mapped_as_dataclass()
class LeadModel:
    __tablename__ = "Lead"
    
    codigo_lead: Mapped[int] = mapped_column(Integer, init=False, primary_key=True, autoincrement=True)
    nome_lead: Mapped[str]
    etapa_lead: str
    cliente_novo: bool
    canal_vendas: int
    create_at: datetime
