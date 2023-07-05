from fastapi import APIRouter
from . import auth, statistics

api_router = APIRouter()

api_router.include_router(auth.app, tags=['auth'])
api_router.include_router(statistics.app, tags=['statistic'])