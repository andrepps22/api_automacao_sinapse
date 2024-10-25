from core.config import setting
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


reg = setting.DBModelReg


@reg.mapped_as_dataclass()
class LeadModel:
    __tablename__ = "Lead"
    
    codigo_lead: Mapped[int] = mapped_column(Integer, init=False, primary_key=True, autoincrement=True)
    nome_lead: Mapped[str] = mapped_column(String)
    etapa_lead: Mapped[str] = mapped_column(String)
    cliente_novo: Mapped[bool] = mapped_column(Boolean)
    canal_vendas: Mapped[str] = mapped_column(String)
    create_at: Mapped[datetime] = mapped_column(DateTime)

    
    __table_args__ = {'extend_existing': True}