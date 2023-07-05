from datetime import date

from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from core.model.models import TblUser, TblStatistic


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


def save_statistic(u_id: str, session: Session):
    statistic = session.query(TblStatistic).filter(TblStatistic.user_id == u_id).first()
    if statistic:
        statistic.count = statistic.count + 1
        return

    session.add(
        TblStatistic(
            date=date.today(),
            count=1,
            user_id=u_id
        )
    )
    return