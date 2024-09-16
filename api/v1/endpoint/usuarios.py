from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from core.security import gerar_hash, pegar_usuario_corrente
from models.usuarios_model import UsuarioModel
from schemas.usuarios_schemas import (UsuarioPublicoSchemas, UsuarioSchemas,
                                      UsuarioSenhaSchemas)

router = APIRouter(prefix='/usuarios', tags=['Usuarios'])


@router.get('/', response_model=List[UsuarioPublicoSchemas], status_code=status.HTTP_200_OK)
async def get_usuarios(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel)
        result = await session.execute(query)
        user: List = result.scalars().all()
        return user


@router.get('/{id_usuario}', status_code=status.HTTP_200_OK, response_model=UsuarioPublicoSchemas)
async def get_usuario(id_usuario: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).where(UsuarioModel.id == id_usuario)
        result = await session.execute(query)
        user = result.scalars().one_or_none()
        if user:
            return user
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Não foi encontrado usuário com esse ID')


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UsuarioSchemas)
async def post_usuario(usuario: UsuarioSenhaSchemas, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).where(
            UsuarioModel.username == usuario.username or UsuarioModel.email == usuario.email
        )
        result = await session.execute(query)
        user = result.scalars().one_or_none()

        if user:
            if user.username:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail='Já existe esse usuário, por favor tente outro'
                )
            if user.email:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail='Já existe um usuário utlizando este email, por favor tente outro'
                )
        else:
            query = insert(UsuarioModel).values(
                username=usuario.username,
                email=usuario.email,
                senha=gerar_hash(usuario.senha)
            )
            await session.execute(query)
            await session.commit()
            return usuario


@router.put('/{id_usuario}', response_model=UsuarioPublicoSchemas, status_code=status.HTTP_202_ACCEPTED)
async def put_usuario(id_usuario: int, usuario: UsuarioSenhaSchemas, db: AsyncSession = Depends(get_session), usuario_corrente = Depends(pegar_usuario_corrente)):
    async with db as session:
        query = select(UsuarioModel).where(UsuarioModel.id == id_usuario)
        result = await session.execute(query)
        user = result.scalars().one_or_none()

        if user:
            if user.username:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail='Usuário já esta sendo utilizado'
                )
            elif user.email:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail='Email já esta sendo utilizado'
                )
            query = update(UsuarioModel).values(
                username=usuario.username, email=usuario.email, senha=usuario.senha
            )
            await session.execute(query)
            await session.commit()

            return usuario
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Não foi encontrado usuário com esse ID')
        

@router.delete('/{id_usuario}', status_code=status.HTTP_202_ACCEPTED)
async def delete_usuario(id_usuarios: int, db:AsyncSession = Depends(get_session), usuario_corrente=Depends(pegar_usuario_corrente)):
    async with db as session:
        query = delete(UsuarioModel).where(UsuarioModel.id == id_usuarios)
        await session.execute(query)
        await session.commit()