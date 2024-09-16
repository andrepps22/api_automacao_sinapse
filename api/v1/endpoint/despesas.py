from datetime import datetime
from typing import List
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from models.despesas_model import DespesasModel
from schemas.despesas_schemas import DespesasSchemas, DespesasSchemasGet
from core.security import pegar_usuario_corrente

router = APIRouter(prefix='/despesas', tags=['Despesas'])


DB = Annotated[AsyncSession, Depends(get_session)]


@router.get('/', response_model=List[DespesasSchemasGet], status_code=status.HTTP_200_OK)
async def get_despesas(db: DB):
    async with db as session:
        query = select(DespesasModel)
        result = await session.execute(query)
        despesas: List = result.scalars().all()
        return despesas


@router.get('/{id_despesa}',  response_model=DespesasSchemasGet, status_code=status.HTTP_200_OK)
async def get_despesa(id_despesa: int, db: DB):
    async with db as session:
        query = select(DespesasModel).where(DespesasModel.id == id_despesa)
        result = await session.execute(query)
        despesa = result.scalars().one_or_none()

        if despesa:
            return despesa
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Não existe uma despesa com esse ID')
        

@router.get('', response_model=List[DespesasSchemasGet], status_code=status.HTTP_200_OK)
async def get_despesa_descricao(descricao: str, db: DB):
    async with db as session:
        query = select(DespesasModel).filter(DespesasModel.descricao.like(descricao))
        result = await session.execute(query)
        despesas: List = result.scalars().all()

        if despesas:
            return despesas
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Não existe uma despesa com essa descricao')
        
#TODO colocar o response model
@router.get('/{ano}/{mes}')
async def get_despesas(ano, mes, db: DB ):
    data_inicio = datetime.strptime(f'{ano}-{mes}-01', '%Y-%m-%d').date()
    data_fim = datetime.strptime(f'{ano}-{mes}-30', '%Y-%m-%d').date()
    async with db as session:
        query = select(DespesasModel).filter(DespesasModel.data.between(data_inicio, data_fim))
        result = await session.execute(query)
        despesa: List = result.scalars().all()

    if despesa:
        return despesa
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Não existe uma despesas neste periodo')



@router.post('/', response_model=DespesasSchemas, status_code=status.HTTP_201_CREATED)
async def post_despesa(despesa: DespesasSchemas, db: DB, usuario_corrente = Depends(pegar_usuario_corrente)):
    async with db as session:
        query = insert(DespesasModel).values(
            descricao=despesa.descricao, valor=despesa.valor, data=despesa.data, categoria=despesa.categoria
        )
        await session.execute(query)
        await db.commit()
        return despesa


@router.put('/{id_despesa}', status_code=status.HTTP_201_CREATED)
async def put_despesa(id_despesa: int, despesas: DespesasSchemas, db: DB, usuario_corrente = Depends(pegar_usuario_corrente)):
    async with db as session:
        query = select(DespesasModel).where(DespesasModel.id == id_despesa)
        result = await session.execute(query)
        despesa_put = result.scalars().one_or_none()

        if despesa_put:
            query = update(DespesasModel).values(
                descricao=despesas.descricao,
                valor=despesas.valor,
                data=despesas.data,
                categoria=despesas.categoria
            ).where(
                DespesasModel.id == id_despesa
            )
            await session.execute(query)
            await session.commit()

            return despesas
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Não existe uma despesa com esse ID')


@router.delete('/{id_despesa}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_despesa(id_despesa: int, db: DB, usuario_corrente = Depends(pegar_usuario_corrente)):
    async with db as session:
        query = select(DespesasModel).where(DespesasModel.id == id_despesa)
        result = await session.execute(query)
        despesa = result.scalars().one_or_none()

        if despesa:
            query = delete(DespesasModel).where(DespesasModel.id == id_despesa)
            await session.execute(query)
            await session.commit()

        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Não existe uma despesa com esse ID')
