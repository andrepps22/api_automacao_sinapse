from fastapi import APIRouter, Depends, status
from core.security import pegar_usuario_corrente
from core.deps import get_session
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from models.etapa_lead_model import EtapaLeadModel
from schemas.etapa_lead_schema import EtapaleadSchema


router = APIRouter()


@router.post('/etapa_lead', tags=['Lead'], response_model=EtapaleadSchema, status_code=status.HTTP_201_CREATED)
async def post_lead(etapalead: EtapaleadSchema, current_user=Depends(pegar_usuario_corrente), db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = insert(EtapaLeadModel).values(
            codigo_lead = etapalead.codigo_lead,
            etapa_lead = etapalead.etapa_lead 
        )
        
        await session.execute(query)
        await session.commit()
    
    return etapalead
