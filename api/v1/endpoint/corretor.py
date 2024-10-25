from fastapi import APIRouter, status, Depends, HTTPException
from core.security import pegar_usuario_corrente
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from models.corretor_model import CorretorModel
from schemas.corretor_Schemas import CorretorSchema
from typing import List
from core.deps import get_session


router = APIRouter()


@router.post('/corretor', response_model=CorretorSchema, tags=['Corretor'], status_code=status.HTTP_201_CREATED)
async def post_corretor(db: AsyncSession = Depends(get_session), corretor: CorretorSchema = CorretorSchema, current_user=Depends(pegar_usuario_corrente)):
    try:
        async with db as session:
            sql = insert(CorretorModel).values(
                nome=corretor.nome,
                cpf=corretor.cpf,
                endereco=corretor.endereco,
                celular=corretor.celular,
                data_nascimento=corretor.data_nascimento)
            await session.execute(sql)
            await session.commit()

        return corretor
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Por favor verifique os campos e tente novamente.')


@router.get('/corretor/', response_model=List[CorretorSchema], status_code=status.HTTP_200_OK, tags=['Corretor'])
async def get_corretor(db: AsyncSession = Depends(get_session), current_user=Depends(pegar_usuario_corrente)):
    async with db as session:
        sql = select(CorretorModel)
        resposta = await session.execute(sql)
        corretores: List = resposta.scalars().all()

    return corretores


@router.get('/corretor/{id_corretor}', response_model=CorretorSchema, status_code=status.HTTP_200_OK, tags=['Corretor'])
async def get_corretor(id: int, db: AsyncSession = Depends(get_session), current_user=Depends(pegar_usuario_corrente)):
    async with db as session:
        sql = select(CorretorModel).where(CorretorModel.id_corretor == id)
        resposta = await session.execute(sql)
        corretor = resposta.scalars().one_or_none()
        if corretor:
            return corretor
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Não exites nenhum corretor com o id: {id}')

    return corretores


# @router.put('/corretor/{id_corretor}', response_model=CorretorSchema, tags=['Corretor'], status_code=status.HTTP_201_CREATED)
# async def put_corretor(db: AsyncSession = Depends(get_session), corretor: CorretorSchema = CorretorSchema):

#     async with db as session:
#         query = select(CorretorModel).where(CorretorModel.id_corretor == id)
#         result = await session.execute(query)
#         user = result.scalars().one_or_none()

#         if user:
#             if user.username:
#                 raise HTTPException(
#                     status_code=status.HTTP_409_CONFLICT,
#                     detail='Usuário já esta sendo utilizado'
#                 )
#             elif user.email:
#                 raise HTTPException(
#                     status_code=status.HTTP_409_CONFLICT,
#                     detail='Email já esta sendo utilizado'
#                 )
#             sql = update(CorretorModel).values(
#                 nome=corretor.nome,
#                 cpf=corretor.cpf,
#                 endereco=corretor.endereco,
#                 celular=corretor.celular,
#                 data_nascimento=corretor.data_nascimento).where(CorretorModel.id_corretor == id)

#             await session.execute(sql)
#             await session.commit()
#             return corretor
#         else:
#             raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
#                                 detail='Por favor verifique os campos e tente novamente.')


# @router.delete('/corretor/{id_corretor}', status_code=status.HTTP_204_NO_CONTENT, tags=['Corretor'])
# async def delete_corretor(id: int, db: AsyncSession = Depends(get_session)):
#     async with db as session:
#         sql = select(CorretorModel).where(CorretorModel.id_corretor == id)
#         result = await session.execute(sql)
#         user = result.scalars().one_or_none()

#         if user:
#             sql = delete(CorretorModel).where(CorretorModel.id_corretor == id)
#             await session.execute(sql)
#             await session.commit()
#         else:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                                 detail=f'Não exites nenhum corretor com o id: {id}')
