from pydantic import BaseModel


class ImovelSchema(BaseModel):
    id_imovel: int
    rua: str
    numero: str
    referencia: str
    descricao: str
    imagens: str
    observacoes: str
    id_propietario: str
    cep: int