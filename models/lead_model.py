from core.config import setting
from sqlalchemy import Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


reg = setting.DBModelReg


@reg.mapped_as_dataclass()
class LeadModel:
    __tablename__ = "client_lead"
    
    codigo_lead: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome_lead: Mapped[str] = mapped_column(String)
    canal_vendas: Mapped[str] = mapped_column(String, nullable=True)
    Tipo_post: Mapped[str] = mapped_column(String)
    campanha: Mapped[str] = mapped_column(String)
    numero_lead_celular: Mapped[str] = mapped_column(String)
    origem_lead: Mapped[str] = mapped_column(String)
    create_at: Mapped[datetime] = mapped_column(DateTime, init=False, server_default=func.now())


    
    __table_args__ = {'extend_existing': True}
    