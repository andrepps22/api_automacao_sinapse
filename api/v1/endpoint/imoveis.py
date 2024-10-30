from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from models.imoveis_model import ImoveisModel
from schemas.imovel_schema import ImovelSchema
from core.security import pegar_usuario_corrente
from typing import List
from core.deps import get_session


router = APIRouter()


@router.post('/imovel', status_code=status.HTTP_201_CREATED, response_model=ImovelSchema, tags=['Imoveis'])
async def post_imoveis(imovel: ImovelSchema = ImovelSchema, db: AsyncSession = Depends(get_session), current_user=Depends(pegar_usuario_corrente)):
    async with db as session:
        query = insert(ImoveisModel).values(
            codigo_imovel=imovel.codigo_imovel,
            codigo_corretor=imovel.codigo_corretor,
            codigo_proprietario=imovel.codigo_proprietario,
            tipo_imovel=imovel.tipo_imovel,
            condominio=imovel.condominio,
            rua=imovel.rua,
            numero=imovel.numero,
            referencia=imovel.referencia,
            descricao=imovel.descricao,
            quartos=imovel.quartos,
            cozinha=imovel.cozinha,
            sacada=imovel.sacada,
            banheiro=imovel.sacada,
            observacoes=imovel.observacoes,
            cep=imovel.cep)

        await session.execute(query)
        await session.commit()
        return imovel


@router.get('/imoveis/', status_code=status.HTTP_200_OK, tags=['Imoveis'])
async def get_imoveis(db: AsyncSession = Depends(get_session), current_user=Depends(pegar_usuario_corrente)):
    async with db as session:
        query = select(ImoveisModel)
        result = await session.execute(query)
        imoveis: List = result.scalars().all()

    return imoveis
