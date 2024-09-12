from pydantic import BaseModel
from typing import Dict


class ResumoSchema(BaseModel):
    Resumo_total_por_categoria: Dict
    Despesas_totais_no_mes: float
    Receitas_totais_no_mes: float
    Saldo_do_mes: float
