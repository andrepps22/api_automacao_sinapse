from core.config import setting
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

reg = setting.DBModelReg


@reg.mapped_as_dataclass()
class PropietarioModel:
    __tablename__='proprietario'
    
    id_propietario: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column()
    cpf: Mapped[str] = mapped_column()
    endereco: Mapped[str] = mapped_column()
    data_nascimento: Mapped[datetime] = mapped_column()