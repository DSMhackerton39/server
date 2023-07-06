from datetime import date

from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from core.model.models import TblUser, TblStatistic
from utils.sockets import sio_server


def get_statistic(user_id: str, session: Session):
    statistics = session.query(TblStatistic.user_id,
                               TblStatistic.date,
                               TblStatistic.count,
                               TblUser.id
                               ).filter(TblStatistic.user_id == user_id).join(TblStatistic,
                                                                              TblStatistic.user_id == TblUser.id)

    return {
        "statistic": [{
            "date": date,
            "count": count
        } for user_id, date, count, u_id in statistics]
    }


@sio_server.event
async def save_statistic(is_sleep: int, session: Session):
    if not is_sleep:
        await sio_server.emit('wake_up', {"message": "wake up"})
        return
    statistic = session.query(TblStatistic).filter(
        TblStatistic.user_id == 8, TblStatistic.date == date.today()).first()

    if statistic:
        statistic.count = statistic.count + 1

    else:
        session.add(
            TblStatistic(
                date=date.today(),
                count=1,
                user_id=8
            )
        )
    await sio_server.emit('sleep', {"message": "user sleep"})

    return
