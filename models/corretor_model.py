from core.config import setting
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


reg = setting.DBModelReg


@reg.mapped_as_dataclass()
class CorretorModel:
    __tablename__ = 'corretor'
    
    id_corretor: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column()
    cpf: Mapped[str] = mapped_column(unique=True)
    endereco: Mapped[str] = mapped_column()
    celular: Mapped[str] = mapped_column()
    data_nascimento: Mapped[datetime] = mapped_column()
    
    
    __table_args__ = {'extend_existing': True}
    
