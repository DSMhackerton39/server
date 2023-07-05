from fastapi import HTTPException, Depends, status

from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from core.model import session_scope

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(user_id: str):
    exp = datetime.utcnow() + timedelta(minutes=9999999)
    encoded_jwt = jwt.encode({"exp": exp, "sub": str(user_id)},
                             'U0VDUkVUS0VZZGlmamlkamZsa2RqZmxkamtsZmprbGpma2xkamZrbGpma2xhc2pkamtkbGZqa2w=',
                             algorithm='HS256')
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    with session_scope() as session:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
        try:
            payload = jwt.decode(token, 'U0VDUkVUS0VZZGlmamlkamZsa2RqZmxkamtsZmprbGpma2xkamZrbGpma2xhc2pkamtkbGZqa2w=',
                                 algorithms='HS256')
            user_id: str = payload.get("sub")
            if user_id is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        return user_id
