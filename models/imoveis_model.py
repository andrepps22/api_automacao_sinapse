from core.config import setting
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, String
import sqlalchemy as sa
from typing import List



reg = setting.DBModelReg


@reg.mapped_as_dataclass()
class ImoveisModel:
    __tablename__= 'imovel'
    
    id_imovel: Mapped[int] = mapped_column(Integer, init=False, primary_key=True, autoincrement=True)
    rua: Mapped[str] = mapped_column(String)
    numero: Mapped[str] = mapped_column(String)
    referencia: Mapped[str] = mapped_column(String)
    descricao: Mapped[str] = mapped_column(String)
    imagens: Mapped[str] = mapped_column(sa.Text)
    observacoes: Mapped[str] = mapped_column(String)
    id_propietario: Mapped[int] = mapped_column(ForeignKey('proprietario.id_propietario'))
    cep: Mapped[str] = mapped_column(String)