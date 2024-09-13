from fastapi import APIRouter

from api.v1.endpoint import auth, despesas, receitas, resumo, usuarios
from core.config import setting

router = APIRouter()

router.include_router(despesas.router, prefix=setting.API_VERSION)
router.include_router(receitas.router, prefix=setting.API_VERSION)
router.include_router(resumo.router, prefix=setting.API_VERSION)
router.include_router(usuarios.router, prefix=setting.API_VERSION)
router.include_router(auth.router, prefix=setting.API_VERSION)