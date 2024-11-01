from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from models.proprietario_model import PropietarioModel
from schemas.propietario_schemas import ProprietarioSchema
from core.security import pegar_usuario_corrente
from core.criar_codigo import criar_codigo
from typing import List
from core.deps import get_session


router = APIRouter()

@router.post('/proprietario', status_code=status.HTTP_201_CREATED, response_model=ProprietarioSchema, tags=['Proprietario'])
async def post_proprietario(proprietario: ProprietarioSchema = ProprietarioSchema, db: AsyncSession = Depends(get_session), current_user=Depends(pegar_usuario_corrente)):
    async with db as session:
      
        query = insert(PropietarioModel).values(
                id_proprietario = criar_codigo("Proprietario"),
                nome = proprietario.nome,
                cpf = proprietario.cpf,
                endereco = proprietario.endereco,
                data_nascimento = proprietario.data_nascimento    
        )

        await session.execute(query)
        await session.commit()
    return proprietario


@router.get('/proprietario/', status_code=status.HTTP_200_OK, response_model=List[ProprietarioSchema], tags=['Proprietario'])
async def get_proprietario(db: AsyncSession = Depends(get_session), current_user=Depends(pegar_usuario_corrente)):
    async with db as session:
        query = select(PropietarioModel)
        result = await session.execute(query)
        propietarios: List = result.scalars().all() 
<<<<<<< HEAD
        if propietarios:
            return propietarios
        
        
@router.get('/proprietario/{id_proprietario}', status_code=status.HTTP_200_OK, response_model=PropietarioIDSchema, tags=['Proprietario'])
async def get_proprietario(id_proprietario:int, db: AsyncSession = Depends(get_session), current_user=Depends(pegar_usuario_corrente)):
    async with db as session:
        query = select(PropietarioModel).where(PropietarioModel.id_proprietario == id_proprietario)
        result = await session.execute(query)
        proprietario = result.scalars().one_or_none()
        if proprietario:
            return proprietario
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe propietario com este id: {id_proprietario}')
           
=======
        return propietarios
        
        
@router.get('/proprietario/{id_proprietario}', status_code=status.HTTP_200_OK, response_model=List[ProprietarioSchema], tags=['Proprietario'])
async def get_proprietario(id_proprietario:str, db: AsyncSession = Depends(get_session), current_user=Depends(pegar_usuario_corrente)):
    async with db as session:
        query = select(PropietarioModel).where(PropietarioModel.id_proprietario == id_proprietario)
        result = await session.execute(query)
        propietario = result.scalars().one_or_none()
        if propietario:
            return propietario
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Não exites nenhum proprietario com o id: {id_proprietario}')
>>>>>>> 84fc453 (atualização de dados)
