from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from core.config import setting

reg = setting.DBModelReg



@reg.mapped_as_dataclass()
class UsuarioModel:
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str]
    criado_em: Mapped[datetime] = mapped_column(init=False, server_default=func.now())



    __table_args__ = {'extend_existing': True}