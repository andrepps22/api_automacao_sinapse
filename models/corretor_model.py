from core.config import setting
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer


reg = setting.DBModelReg


@reg.mapped_as_dataclass()
class CorretorModel:
    __tablename__ = 'corretor'
    
    id_corretor: Mapped[int] = mapped_column(Integer, init=False, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String)
    cpf: Mapped[str] = mapped_column(String ,unique=True)
    endereco: Mapped[str] = mapped_column(String)
    celular: Mapped[str] = mapped_column(String)
   
    
    
    __table_args__ = {'extend_existing': True}
    
