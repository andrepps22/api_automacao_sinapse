from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from models.proprietario_model import PropietarioModel
from schemas.propietario_schemas import PropietarioSchema
import json
from typing import List
from core.deps import get_session


router = APIRouter()

@router.post('/Proprietario', status_code=status.HTTP_201_CREATED, response_model=PropietarioSchema, tags=['Proprietario'])
async def post_imoveis(proprietario: PropietarioSchema = PropietarioSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
      
        query = insert(PropietarioModel).values(
                nome = proprietario.nome,
                cpf = proprietario.cpf,
                endereco = proprietario.endereco,
                data_nascimento = proprietario.data_nascimento    
        )

        await session.execute(query)
        await session.commit()
    return proprietario