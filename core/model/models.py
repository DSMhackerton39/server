
import datetime

from sqlalchemy import Column, DATE, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from . import Base


class TblUser(Base):
    __tablename__ = 'tbl_user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    u_id = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)


class TblStatistic(Base):
    __tablename__ = 'tbl_statistics'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    date = Column(DATE, nullable=False, default=datetime.date.today())
    count = Column(Integer, nullable=False, default=0)
    user_id = Column(ForeignKey('tbl_user.id'), nullable=False, index=True)

    user = relationship('TblUser')
