from fastapi import APIRouter, Depends, status
from core.security import pegar_usuario_corrente
from core.deps import get_session
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from models.lead_model import LeadModel
from schemas.lead_schemas import LeadSchema


router = APIRouter()


@router.post('/lead', tags=['Lead'], response_model=LeadSchema, status_code=status.HTTP_201_CREATED)
async def post_lead(lead: LeadSchema, current_user=Depends(pegar_usuario_corrente), db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = insert(LeadModel).values(
            codigo_lead = lead.codigo_lead,
            Tipo_post = lead.Tipo_post,
            nome_lead = lead.nome_lead,
            campanha = lead.campanha,
            numero_lead_celular = lead.numero_lead
        )
        
        await session.execute(query)
        await session.commit()
    
    return lead
