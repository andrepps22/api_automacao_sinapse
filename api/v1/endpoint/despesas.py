from fastapi import APIRouter, status, Depends, HTTPException
from datetime import datetime
from schemas.despesas_schemas import DespesasSchemas, DespesasSchemasGet
from models.despesas_model import DespesasModel
from sqlalchemy import select, update, delete, insert
from sqlalchemy.ext.asyncio import AsyncSession
from core.deps import get_sessison
from typing import List


router = APIRouter()


@router.get('/despesas/', response_model=List[DespesasSchemasGet], tags=['Despesas'], status_code=status.HTTP_200_OK)
async def get_despesas(db: AsyncSession = Depends(get_sessison)):
    async with db as session:
        query = select(DespesasModel)
        result = await session.execute(query)
        despesas: List = result.scalars().all()
        return despesas


@router.get('/despesas/{id_despesa}',  response_model=DespesasSchemasGet, tags=['Despesas'], status_code=status.HTTP_200_OK)
async def get_despesa(id_despesa: int, db: AsyncSession = Depends(get_sessison)):
    async with db as session:
        query = select(DespesasModel).where(DespesasModel.id == id_despesa)
        result = await session.execute(query)
        despesa = result.scalars().one_or_none()

        if despesa:
            return despesa
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Não existe uma despesa com esse ID')


@router.post('/despesas/', response_model=DespesasSchemas, tags=['Despesas'], status_code=status.HTTP_201_CREATED)
async def post_despesa(despesa: DespesasSchemas, db: AsyncSession = Depends(get_sessison)):
    async with db as session:
        query = insert(DespesasModel).values(
            descricao=despesa.descricao, valor=despesa.valor, data=despesa.data, categoria=despesa.categoria
        )
        await session.execute(query)
        await db.commit()
        return despesa


@router.put('/despesas/{id_despesa}', tags=['Despesas'], status_code=status.HTTP_201_CREATED)
async def put_despesa(id_despesa: int, despesas: DespesasSchemas, db=Depends(get_sessison)):
    async with db as session:
        query = select(DespesasModel).where(DespesasModel.id == id_despesa)
        result = await session.execute(query)
        despesa_put = result.scalars().one_or_none()
        print(despesa_put)

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


@router.delete('/despesas/{id_despesa}', tags=['Despesas'], status_code=status.HTTP_204_NO_CONTENT)
async def delete_despesa(id_despesa: int, db=Depends(get_sessison)):
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
