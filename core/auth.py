from pytz import timezone
from typing import List, Optional
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from core.config import setting
from core.security import verificar_senha


oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f'{setting.API_VERSION}/usuarios/login'
)

