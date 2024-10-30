from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer
from core.security import pegar_usuario_corrente

from api.v1.api import router


app = FastAPI(title='SinapseGH',
              redoc_url=False,
              version='0.0.1'
              )

app.include_router(router)

security = HTTPBearer()

@app.get("/docs", include_in_schema=False)
async def get_docs(credentials = Depends(pegar_usuario_corrente)):
    return {"message": "You are authenticated"}

if __name__=='__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)