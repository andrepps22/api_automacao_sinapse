from sqlalchemy.orm import Mapped, mapped_column
from core.config import Setting
from datetime import date

reg = Setting.DBModelReg

@reg.mapped_as_dataclass()
class ReceitasModel:
    __tablename__ = 'receitas'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    descricao: Mapped[str]
    valor: Mapped[float]
    data: Mapped[date]


    __table_args__ = {'extend_existing': True}