from pydantic import BaseModel, Field
from typing import List, Optional






class ImovelSchema(BaseModel):
    codigo_imovel: str
    codigo_corretor: int
    codigo_proprietario: int
    tipo_imovel: str
    condominio: bool
    rua: str
    numero: str
    referencia: str
    descricao: str
    sala: List[str]
    quartos: List[str]
    cozinha: List[str]
    sacada: List[str]
    banheiro: List[str]
    observacoes: str = None
    cep: str


