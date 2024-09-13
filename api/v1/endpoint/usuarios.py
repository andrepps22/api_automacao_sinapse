from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from core.security import gerar_hash
from core.deps import get_sessison
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.usuarios_schemas import UsuarioSchemas, UsuarioSenhaSchemas
from models.usuarios_model import UsuarioModel


router = APIRouter()


@router.post('/usuarios/', status_code=status.HTTP_201_CREATED, response_model=UsuarioSchemas, tags=['Usuario'])
async def post_usuario(usuario: UsuarioSenhaSchemas, db: AsyncSession = Depends(get_sessison)):
    async with db as session:
        query = select(UsuarioModel).where(UsuarioModel.username == usuario.username or UsuarioModel.email == usuario.email)
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