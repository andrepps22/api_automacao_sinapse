from fastapi import APIRouter

from api.v1.endpoint import auth, lead, corretor, imoveis, propietario, etapa_lead
from core.config import setting

router = APIRouter()


<<<<<<< HEAD
# router.include_router(lead.router, prefix=setting.API_VERSION)
=======
router.include_router(lead.router, prefix=setting.API_VERSION)
router.include_router(etapa_lead.router, prefix=setting.API_VERSION)
>>>>>>> 863b049b432bf7951a85b345d3f0a83614dbdc65
router.include_router(auth.router, prefix=setting.API_VERSION)
router.include_router(corretor.router, prefix=setting.API_VERSION)
router.include_router(imoveis.router, prefix=setting.API_VERSION)
router.include_router(propietario.router, prefix=setting.API_VERSION)