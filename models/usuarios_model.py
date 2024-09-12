from sqlalchemy.orm import Mapped, mapped_column
from core.config import setting


reg = setting.DBModelReg



@reg.mapped_as_dataclass()
class UsuarioModel:
    __tablename__ = 'usuarios'


    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    email: Mapped[str]
    hashe: Mapped[str]



    __table_args__ = {'extend_existing': True}