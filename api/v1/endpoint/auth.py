from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from core.security import criar_token, verificar_senha
from models.usuarios_model import UsuarioModel
from schemas.token_schemas import TokenSchemas

router = APIRouter()


@router.post('/token', response_model=TokenSchemas, tags=['Token'])
async def login_para_acess_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_session)):

    async with db as session:
        user = await session.scalar(select(UsuarioModel).where(UsuarioModel.username == form_data.username))

        if not user or not verificar_senha(form_data.password, user.senha):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail='Username ou senha incorretas')
    
    access_token = criar_token({'sub': user.username})

    return {'access_token': access_token, 'token_type':'Bearer'}
        