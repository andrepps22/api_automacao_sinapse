from core.config import setting
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from datetime import date

reg = setting.DBModelReg


@reg.mapped_as_dataclass()
class PropietarioModel:
    __tablename__='proprietario'
    
    id_proprietario: Mapped[str] = mapped_column(String, primary_key=True)
    nome: Mapped[str] = mapped_column(String)
    cpf: Mapped[str] = mapped_column(String, unique=True)
    endereco: Mapped[str] = mapped_column(String)
    data_nascimento: Mapped[date] = mapped_column()
    
    __table_args__ = {'extend_existing': True}