from pydantic import BaseModel


class LoginData(BaseModel):
    email: str
    password: str


class RegisterData(BaseModel):
    email: str
    password: str
    password_confirm: str


class GetAuthData(BaseModel):
    authorized: bool
    email: str
