from pydantic import BaseModel, constr


class SignUp(BaseModel):
    id: constr(min_length=1, max_length=10)
    password: str


class Login(BaseModel):
    id: constr(min_length=1, max_length=10)
    password: str