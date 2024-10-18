from core.config import setting
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


reg = setting.DBModelReg


@reg.mapped_as_dataclass()
class ImoveisModel:
    __tablename__= 'imovel'
    
    id_imovel: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    rua: Mapped[str] = mapped_column()
    numero: Mapped[str] = mapped_column()
    referencia: Mapped[str] = mapped_column()
    descricao: Mapped[str] = mapped_column()
    imagens: Mapped[str] = mapped_column()
    observacoes: Mapped[str] = mapped_column()
    id_propietario: Mapped[int] = mapped_column(ForeignKey('proprietario.id_propietario'))
    cep: Mapped[int] = mapped_column()