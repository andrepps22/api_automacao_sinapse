from pydantic import BaseModel, Field
from typing import List, Optional






class ImovelSchema(BaseModel):
    codigo_imovel: str
    tipo_imovel: str
    condominio: bool
    rua: str
    numero: str
    referencia: str
    descricao: str
    imagens: List[str]
    observacoes: str = None
    id_propietario: int
    cep: str


