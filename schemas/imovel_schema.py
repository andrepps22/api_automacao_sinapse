from pydantic import BaseModel
from typing import List, Optional
from core.criar_codigo import criar_codigo


class ImovelSchema(BaseModel):
    codigo_imovel: Optional[str] = None
    codigo_corretor: str
    nome_proprietario: str
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

    def __init__(self, **data):
        super().__init__(**data)
        if not self.codigo_imovel:
            self.codigo_imovel = criar_codigo(self.tipo_imovel)
            print(self.codigo_imovel, self.tipo_imovel)