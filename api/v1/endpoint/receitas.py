from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from core.security import pegar_usuario_corrente
from models.receitas_model import ReceitasModel
from schemas.receitas_schemas import ReceitasSchemas, ReceitasSchemasGet

router = APIRouter()


@router.get('/receitas/', response_model=List[ReceitasSchemasGet], status_code=status.HTTP_200_OK, tags=['Receitas'])
async def get_despesas(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ReceitasModel)
        result = await session.execute(query)
        receitas: List = result.scalars().all()
        return receitas


@router.get('/receitas/{id_receita}', response_model=ReceitasSchemasGet, status_code=status.HTTP_200_OK, tags=['Receitas'])
async def get_despesa(id_receita: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ReceitasModel).where(ReceitasModel.id == id_receita)
        result = await session.execute(query)
        receita = result.scalars().one_or_none()
        if receita:
            return receita
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Não existe uma despesa com esse ID')


@router.get('/receitas',response_model=List[ReceitasSchemasGet], status_code=status.HTTP_200_OK, tags=['Receitas'])
async def get_receitas_descricao(descricao:str, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ReceitasModel).filter(ReceitasModel.descricao.like(descricao))
        result = await session.execute(query)
        despesas: List = result.scalars().all()
        if despesas:
            return despesas
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Não existe uma despesa com essa descricao')


@router.post('/receitas/', response_model=ReceitasSchemas, status_code=status.HTTP_201_CREATED, tags=['Receitas'])
async def post_receita(receita: ReceitasSchemas, db: AsyncSession = Depends(get_session), usuario_corrente = Depends(pegar_usuario_corrente)):
    async with db as session:
        query = insert(ReceitasModel).values(
            descricao=receita.descricao,
            valor=receita.valor,
            data=receita.data
        )
        await session.execute(query)
        await session.commit()

        return receita


@router.put('/receitas/{id_receita}', response_model=ReceitasSchemas, status_code=status.HTTP_202_ACCEPTED, tags=['Receitas'])
async def put_receita(id_receita: int, receita: ReceitasSchemas, db: AsyncSession = Depends(get_session), usuario_corrente = Depends(pegar_usuario_corrente)):
    async with db as session:
        query = select(ReceitasModel).where(ReceitasModel.id == id_receita)
        result = await session.execute(query)
        if result.scalars().one_or_none():
            query = update(ReceitasModel).values(
                descricao=receita.descricao,
                valor=receita.valor,
                data=receita.data
            ).where(
                ReceitasModel.id == id_receita
            )
            await session.execute(query)
            await session.commit()
            return receita
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Não existe uma despesa com esse ID')


@router.delete('/receitas/{id_receita}', status_code=status.HTTP_204_NO_CONTENT, tags=['Receitas'])
async def delete_receita(id_receita: int, db: AsyncSession = Depends(get_session), usuario_corrente = Depends(pegar_usuario_corrente)):
    async with db as session:
        query = select(ReceitasModel).where(ReceitasModel.id == id_receita)
        result = await session.execute(query)
        if result.scalars().one_or_none():
            query = delete(ReceitasModel).where(ReceitasModel.id == id_receita)
            await session.execute(query)
            await session.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Não existe uma despesa com esse ID')
