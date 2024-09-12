from fastapi import APIRouter, Depends
from typing import List, Dict
from core.deps import get_sessison
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from models.receitas_model import ReceitasModel
from models.despesas_model import DespesasModel
from schemas.resumo_schemas import ResumoSchema
from datetime import datetime

router = APIRouter()


@router.get('/resumos/{ano}/{mes}', response_model=ResumoSchema, tags=['Resumo'])
async def get_resumos(ano, mes, db: AsyncSession = Depends(get_sessison)):
    data_inicio = datetime.strptime(f'{ano}-{mes}-01', '%Y-%m-%d').date()
    data_fim = datetime.strptime(f'{ano}-{mes}-30', '%Y-%m-%d').date()
    despesas_total_mes = 0
    receitas_total_mes = 0
    categorias_total_mes = {}
    async with db as session:
        query_despesas = select(DespesasModel).filter(
            DespesasModel.data.between(data_inicio, data_fim))
        result = await session.execute(query_despesas)
        despesas: List = result.scalars().all()
        for despesa in despesas:
            despesas_total_mes += despesa.valor

        query_categoria = select(DespesasModel.categoria,  func.sum(
            DespesasModel.valor).label('Valor_Total')).group_by(DespesasModel.categoria)
        result = await session.execute(query_categoria)
        categorias: List = result.all()
        for categoria in categorias:
            categorias_total_mes[categoria[0]] = categoria[1]

        query_receitas = select(ReceitasModel).filter(
            ReceitasModel.data.between(data_inicio, data_fim))
        result = await session.execute(query_receitas)
        receitas: List = result.scalars().all()
        for receita in receitas:
            receitas_total_mes += receita.valor

    saldo_total_mes = receitas_total_mes - despesas_total_mes

    resumo = {
        "Resumo_total_por_categoria": categorias_total_mes,
        "Despesas_totais_no_mes": despesas_total_mes,
        "Receitas_totais_no_mes": receitas_total_mes,
        "Saldo_do_mes": round(saldo_total_mes, 2)

    }

    return resumo
