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


@app.post("/only-Ai/{is_sleep}")
async def save_statistics(is_sleep: int, user: str = Depends(get_current_user)):
    with session_scope() as session:
        return await save_statistic(user_id=user, is_sleep=is_sleep, session=session)
