from datetime import date

from sqlalchemy.orm import Mapped, mapped_column

from core.config import Setting

reg = Setting.DBModelReg


@reg.mapped_as_dataclass()
class DespesasModel:
    __tablename__ = 'despesas'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    descricao: Mapped[str]
    valor: Mapped[float]
    data: Mapped[date]
    categoria: Mapped[str]


    __table_args__ = {'extend_existing': True}



    