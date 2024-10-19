from pydantic import BaseModel
from typing import List, Optional


class ImovelImagenSchema(BaseModel):
    nome: str
    link: str


class ImovelSchema(BaseModel):
    codigo_imovel: int
    rua: str
    numero: str
    referencia: str
    descricao: str
    imagens: List[ImovelImagenSchema] = []
    observacoes: str = None
    id_propietario: int
    cep: str


