from core.config import setting
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, String, JSON, Boolean
from typing import Dict



reg = setting.DBModelReg


@reg.mapped_as_dataclass()
class ImoveisModel:
    __tablename__= 'imovel'
    
    codigo_imovel: Mapped[str] = mapped_column(String, init=False, primary_key=True)
    codigo_corretor: Mapped[int] = mapped_column(Integer, ForeignKey('corretor.id_corretor'))
    codigo_proprietario: Mapped[int] = mapped_column(Integer, ForeignKey('proprietario.id_proprietario'))
    tipo_imovel: Mapped[str] = mapped_column(String)
    condominio: Mapped[bool] = mapped_column(Boolean)
    rua: Mapped[str] = mapped_column(String)
    numero: Mapped[str] = mapped_column(String)
    referencia: Mapped[str] = mapped_column(String)
    descricao: Mapped[str] = mapped_column(String)
    quartos: Mapped[str] = mapped_column(JSON)
    cozinha: Mapped[str] = mapped_column(JSON)
    sacada: Mapped[str] = mapped_column(JSON)
    banheiro: Mapped[str] = mapped_column(JSON)
    observacoes: Mapped[str] = mapped_column(String)
    cep: Mapped[str] = mapped_column(String)
    
    __table_args__ = {'extend_existing': True}