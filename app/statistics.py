from fastapi import APIRouter, Depends

from utils.security import get_current_user
from utils.sockets import sio_server
from utils.statistics import get_statistic, save_statistic

from core.model import session_scope

app = APIRouter(prefix='/statistics')


@app.get("")
async def get_statistics(user: str = Depends(get_current_user)):
    with session_scope() as session:
        return get_statistic(user_id=user, session=session)


@sio_server.event
@app.post("/only-Ai")
async def save_statistics(user: str = Depends(get_current_user)):
    with session_scope() as session:
        await sio_server.emit('sleep', {"message": "user sleep"})
        return save_statistic(user_id=user, session=session)
