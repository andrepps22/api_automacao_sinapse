from core.config import setting
<<<<<<< HEAD
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey, func
=======
from sqlalchemy import Integer, String, Boolean, DateTime, func
>>>>>>> d71c6a34b7c2c5dc52c3dbe59dadb50dc87da345
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
<<<<<<< HEAD
    canal_vendas: Mapped[str] = mapped_column(String)
    create_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
=======
    canal_vendas: Mapped[str] = mapped_column(String, nullable=True)
    create_at: Mapped[datetime] = mapped_column(DateTime, init=False, server_default=func.now())
>>>>>>> d71c6a34b7c2c5dc52c3dbe59dadb50dc87da345

    
    __table_args__ = {'extend_existing': True}