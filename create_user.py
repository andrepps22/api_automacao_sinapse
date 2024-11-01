from core.security import gerar_hash
import asyncio

from fastapi import HTTPException, status
from sqlalchemy import insert, select
from core.database import Session
from core.security import gerar_hash
from models.usuarios_model import UsuarioModel


async def criar_usuario(usuario: dict):
    async with Session() as session:
        query = select(UsuarioModel).where(
            UsuarioModel.username == usuario['username'] or UsuarioModel.email == usuario['email']
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
                username=usuario['username'],
                email=usuario['email'],
                senha=gerar_hash(usuario['senha'])
            )
            await session.execute(query)
            await session.commit()
            return usuario


if __name__ == "__main__":
    import asyncio

    usuario = {
        'username': 'Andre',
<<<<<<< HEAD
        'email': 'nao@tem.com',
=======
        'email': 'nao@tememail.com',
>>>>>>> 84fc453 (atualização de dados)
        'senha': '8EYT56MyNy'
    }

    asyncio.run(criar_usuario(usuario))
