from fastapi import APIRouter, Depends, status
from core.security import pegar_usuario_corrente
from core.deps import get_session
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


@router.post('/lead', tags=['Lead'], status_code=status.HTTP_201_CREATED)
async def post_lead(lead, current_user=Depends(pegar_usuario_corrente), db: AsyncSession = Depends(get_session)):
    async with db as session:
        pass
