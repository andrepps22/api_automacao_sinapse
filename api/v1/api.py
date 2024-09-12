from fastapi import APIRouter
from core.config import setting
from api.v1.endpoint import despesas, receitas, resumo

router = APIRouter()

router.include_router(despesas.router, prefix=setting.API_VERSION)
router.include_router(receitas.router, prefix=setting.API_VERSION)
router.include_router(resumo.router, prefix=setting.API_VERSION)