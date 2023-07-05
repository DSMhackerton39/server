import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import api_router
from utils.sockets import sio_app

app = FastAPI()
app.mount('/ws', app=sio_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)