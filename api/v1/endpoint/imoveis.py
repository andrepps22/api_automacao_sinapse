from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from models.imoveis_model import ImoveisModel
from schemas.imovel_schema import ImovelSchema
import json
from typing import List
from core.deps import get_session


router = APIRouter()


@router.post('/imovel', status_code=status.HTTP_201_CREATED, response_model=ImovelSchema, tags=['Imoveis'])
async def post_imoveis(imovel: ImovelSchema = ImovelSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        imagens_json = json.dumps([imagem.dict()
                                  for imagem in imovel.imagens])
        query = insert(ImoveisModel).values(
            codigo_imovel=imovel.codigo_imovel,
            rua=imovel.rua,
            numero=imovel.numero,
            referencia=imovel.referencia,
            descricao=imovel.descricao,
            imagens=imagens_json,
            observacoes=imovel.observacoes,
            id_propietario=imovel.id_propietario,
            cep=imovel.cep)

        await session.execute(query)
        await session.commit()
        return imovel


@router.get('/imoveis/', status_code=status.HTTP_200_OK, tags=['Imoveis'])
async def get_imoveis(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ImoveisModel)
        result = await session.execute(query)
        imoveis: List = result.scalars().all()
    
    return imoveis