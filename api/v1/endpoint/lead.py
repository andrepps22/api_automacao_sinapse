from fastapi import APIRouter, Depends, status
from core.security import pegar_usuario_corrente
from core.deps import get_session
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
<<<<<<< HEAD
from schemas.lead_schemas import LeadSchema
from models.lead_model import LeadModel
=======
from models.lead_model import LeadModel
from schemas.lead_schemas import LeadSchema
>>>>>>> a4962b31c342cbe753c16e01e7b2b349a40c8159


router = APIRouter()


@router.post('/lead', tags=['Lead'], response_model=LeadSchema, status_code=status.HTTP_201_CREATED)
<<<<<<< HEAD
async def post_lead(lead:LeadSchema, current_user=Depends(pegar_usuario_corrente), db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = insert(LeadModel).values(
            nome_lead=lead.nome_lead,
=======
async def post_lead(lead: LeadSchema, current_user=Depends(pegar_usuario_corrente), db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = insert(LeadModel).values(
            codigo_lead = lead.codigo_lead,
            nome_lead = lead.nome_lead,
>>>>>>> a4962b31c342cbe753c16e01e7b2b349a40c8159
            etapa_lead = lead.etapa_lead,
            cliente_novo = lead.cliente_novo,
            canal_vendas = lead.canal_vendas
        )
        await session.execute(query)
        await session.commit()
    
<<<<<<< HEAD
    return lead
=======
    return lead
>>>>>>> a4962b31c342cbe753c16e01e7b2b349a40c8159
