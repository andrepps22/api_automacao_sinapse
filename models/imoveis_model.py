from core.config import setting
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, String, JSON, DateTime, func
from datetime import  datetime
from typing import Dict




reg = setting.DBModelReg


@reg.mapped_as_dataclass()
class ImoveisModel:
    __tablename__= 'imovel'


    codigoImovel: Mapped[str] = mapped_column(String, primary_key=True)
    codigoCorretor: Mapped[str] = mapped_column(String)
    numeroRegistro: Mapped[int] = mapped_column(Integer)
    documentoRegistro: Mapped[str] = mapped_column(JSON)
    numeroMatricula: Mapped[int] = mapped_column(Integer)
    documentoMatricula: Mapped[str] = mapped_column(JSON)
    IPTU: Mapped[str] = mapped_column(String)
    qtdParcelasAtrasadasIPTU: Mapped[int] = mapped_column(Integer)
    observacoesIPTU: Mapped[str] = mapped_column(String)
    condominio: Mapped[str] = mapped_column(String)
    qtdParcelasAtrasadasCondominio: Mapped[int] = mapped_column(Integer)
    observacoesCondominio: Mapped[str] = mapped_column(String)
    cep: Mapped[str] = mapped_column(String)
    rua: Mapped[str] = mapped_column(String)
    numero: Mapped[str] = mapped_column(String)
    bairro: Mapped[str] = mapped_column(String)
    cidade: Mapped[str] = mapped_column(String)
    estado: Mapped[str] = mapped_column(String)
    referencia: Mapped[str] = mapped_column(String)
    descricao: Mapped[str] = mapped_column(String)
    valorImovel: Mapped[str] = mapped_column(String)
    condominio: Mapped[str] = mapped_column(String)
    valorCondominio: Mapped[str] = mapped_column(String)
    garagem: Mapped[str] = mapped_column(String)
    garagemCoberta: Mapped[str] = mapped_column(String, nullable=True)
    garagemTipo: Mapped[str] = mapped_column(String, nullable=True)
    garagemFoto: Mapped[str] = mapped_column(JSON, nullable=True)
    fachadaFoto: Mapped[str] = mapped_column(JSON)
    salaFotos: Mapped[str] = mapped_column(JSON)
    suite: Mapped[str] = mapped_column(String)
    suiteFotos: Mapped[str] = mapped_column(JSON, nullable=True)
    quantidadeQuarto: Mapped[int] = mapped_column(Integer)
    quartos: Mapped[str] = mapped_column(JSON)
    cozinha: Mapped[str] = mapped_column(JSON)
    sacada: Mapped[str] = mapped_column(JSON)
    quantidadeBanheiros: Mapped[int] = mapped_column(Integer)
    banheiro: Mapped[str] = mapped_column(JSON)
    quartos: Mapped[str] = mapped_column(JSON)
    cozinha: Mapped[str] = mapped_column(JSON)
    metrosQuadradoUtil: Mapped[str] = mapped_column(String)
    metrosQuadradoTotal: Mapped[str] = mapped_column(String)
    create_at: Mapped[datetime] = mapped_column(DateTime, init=False, server_default=func.now())

    

    
    
    __table_args__ = {'extend_existing': True}
    
    
   