from fastapi import APIRouter, Depends

from utils.security import get_current_user
from utils.statistics import get_statistic

from core.model import session_scope

app = APIRouter(prefix='/statistics')


@app.get("")
async def get_statistics(user: str = Depends(get_current_user)):
    with session_scope() as session:
        return get_statistic(user_id=user, session=session)
