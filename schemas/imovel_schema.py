from pydantic import BaseModel
from typing import List


class ImovelImagenSchema(BaseModel):
    nome: str
    link: str


class ImovelSchema(BaseModel):
    id_imovel: int
    rua: str
    numero: str
    referencia: str
    descricao: str
    imagens: List[ImovelImagenSchema]
    observacoes: str
    id_propietario: str
    cep: int
