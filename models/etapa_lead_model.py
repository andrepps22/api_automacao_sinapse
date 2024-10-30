from core.config import setting
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column



reg = setting.DBModelReg


@reg.mapped_as_dataclass()
class EtapaLeadModel:
    __tablename__ = "etapa_lead"
    
    codigo_lead: Mapped[int] = mapped_column(Integer, ForeignKey('client_lead.codigo_lead'),  primary_key=True)
    etapa_lead: Mapped[str] = mapped_column(String)
    

    
    __table_args__ = {'extend_existing': True}
    