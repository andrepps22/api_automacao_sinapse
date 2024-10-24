from fastapi import APIRouter

from api.v1.endpoint import auth, usuarios, corretor, imoveis, propietario
from core.config import setting

router = APIRouter()


# router.include_router(usuarios.router, prefix=setting.API_VERSION)
router.include_router(auth.router, prefix=setting.API_VERSION)
router.include_router(corretor.router, prefix=setting.API_VERSION)
router.include_router(imoveis.router, prefix=setting.API_VERSION)
router.include_router(propietario.router, prefix=setting.API_VERSION)