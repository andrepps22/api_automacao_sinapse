from fastapi import APIRouter, status, Depends, HTTPException
from core.security import pegar_usuario_corrente
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from models.corretor_model import CorretorModel
from schemas.corretor_Schemas import CorretorSchema, CorretorPublicSchema
from typing import List
from core.criar_codigo import criar_codigo
from core.deps import get_session


router = APIRouter()


@router.post('/corretor', response_model=CorretorSchema, tags=['Corretor'], status_code=status.HTTP_201_CREATED)
async def post_corretor(db: AsyncSession = Depends(get_session), corretor: CorretorSchema = CorretorSchema, current_user=Depends(pegar_usuario_corrente)):
    try:
        async with db as session:
            sql = insert(CorretorModel).values(
                id_corretor = corretor.id_corretor,
                nome=corretor.nome,
                cpf=corretor.cpf,
                endereco=corretor.endereco,
                celular=corretor.celular)
            await session.execute(sql)
            await session.commit()
        return (corretor)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Por favor verifique os campos e tente novamente.')


@router.get('/corretor/', response_model=List[CorretorPublicSchema], status_code=status.HTTP_200_OK, tags=['Corretor'])
async def get_corretor(db: AsyncSession = Depends(get_session), current_user=Depends(pegar_usuario_corrente)):
    async with db as session:
        sql = select(CorretorModel)
        resposta = await session.execute(sql)
        corretores: List = resposta.scalars().all()

    return corretores


<<<<<<< HEAD
@router.get('/corretor/{id_corretor}', response_model=CorretorPublicSchema, status_code=status.HTTP_200_OK, tags=['Corretor'])
async def get_corretor(id: int, db: AsyncSession = Depends(get_session), current_user=Depends(pegar_usuario_corrente)):
=======
@router.get('/corretor/{id_corretor}', response_model=CorretorSchema, status_code=status.HTTP_200_OK, tags=['Corretor'])
async def get_corretor(id_corretor: str, db: AsyncSession = Depends(get_session), current_user=Depends(pegar_usuario_corrente)):
>>>>>>> 84fc453 (atualização de dados)
    async with db as session:
        sql = select(CorretorModel).where(CorretorModel.id_corretor == id)
        resposta = await session.execute(sql)
        corretor = resposta.scalars().one_or_none()
        if corretor:
            return corretor
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Não exites nenhum corretor com o id: {id}')
