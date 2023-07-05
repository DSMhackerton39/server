from fastapi import APIRouter

from utils.user import create_user, login

from core.model import session_scope
from core.schemas.user import SignUp, Login

app = APIRouter(prefix='/user')


@app.post("/signup")
async def sign_up(body: SignUp):
    with session_scope() as session:
        return create_user(session=session, body=body)


@app.post("/login")
async def logins(body: Login):
    with session_scope() as session:
        return login(session=session, body=body)
