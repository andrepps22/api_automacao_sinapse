from core.config import setting
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, String, JSON, Boolean
from typing import Dict



reg = setting.DBModelReg


@reg.mapped_as_dataclass()
class ImoveisModel:
    __tablename__= 'imovel'
    
    codigo_imovel: Mapped[str] = mapped_column(String, init=False, primary_key=True)
    tipo_imovel: Mapped[str] = mapped_column(String)
    condominio: Mapped[bool] = mapped_column(Boolean)
    rua: Mapped[str] = mapped_column(String)
    numero: Mapped[str] = mapped_column(String)
    referencia: Mapped[str] = mapped_column(String)
    descricao: Mapped[str] = mapped_column(String)
    imagens: Mapped[Dict] = mapped_column(JSON)
    observacoes: Mapped[str] = mapped_column(String)
    id_propietario: Mapped[int] = mapped_column(ForeignKey('proprietario.id_propietario'))
    cep: Mapped[str] = mapped_column(String)
    
    __table_args__ = {'extend_existing': True}