from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from core.model.models import TblUser
from core.schemas.user import SignUp, Login
from utils.security import get_password_hash, verify_password, create_access_token


def create_user(session: Session, body: SignUp):
    session.add(
        TblUser(
            u_id=body.id,
            password=get_password_hash(body.password),
        )
    )

    return HTTPException(status_code=status.HTTP_201_CREATED, detail="success")


def login(session: Session, body: Login):
    user = session.query(TblUser.u_id, TblUser.password, TblUser.id).filter(TblUser.u_id == body.id)

    if not user.scalar():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id does not exist")

    user = user.first()
    if not verify_password(plain_password=body.password, hashed_password=user["password"]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Wrong password")

    return {
        "access_token": create_access_token(user_id=user.id)
    }


def check_id(session: Session, id: str):
    user = session.query(TblUser.id).filter(TblUser.id == id)

    if user.scalar():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Overlap")

    else:
        return {
            "message": "Available"
        }
