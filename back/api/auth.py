import uuid

import redis
from fastapi import Cookie, Depends, HTTPException, Response
from fastapi_controllers import Controller, get, post
from sqlalchemy.ext.asyncio import AsyncSession

from back.schemas.auth import GetAuthData, LoginData, RegisterData
from database.database import get_db_session
from database.redis import RedisDB, get_redis_client
from database.repositories.user_repository import UserRepository

SESSION_LIFETIME = 3600


class AuthController(Controller):
    prefix = '/auth'
    tags = ['auth']

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    @post("/login", summary="authorizes registered user", description="Sign in")
    async def login(self, response: Response, data: LoginData, redis: redis.Redis = Depends(get_redis_client)):
        ur = UserRepository(self.session)
        user = await ur.get_by_auth(email=data.email, pw=data.password)
        if user is None:
            raise HTTPException(401, "Email или пароль неверны")
        session = uuid.uuid4()
        redis.set(f"{RedisDB.auth_session}:{session}", str(user.id), ex=SESSION_LIFETIME)
        response.set_cookie("session", str(session), max_age=SESSION_LIFETIME, httponly=True)
        return {"message": "OK"}

    @post("/register", summary="registers new user", description="Register")
    async def register(self, data: RegisterData):
        ur = UserRepository(self.session)
        user = await ur.get_by_email(email=data.email)
        if user is not None:
            raise HTTPException(401, "Пользователь с такой почтой уже зарегистрирован")
        if data.password != data.password_confirm:
            raise HTTPException(401, "Пароли не совпадают")
        user = await ur.create(data.email, data.password)
        if user is None: raise HTTPException(401, "Что-то пошло не так...")
        await self.session.commit()
        return {"message": "OK"}

    @post("/logout", summary="log user out", description="Log out")
    async def logout(self, response: Response, session=Cookie(default=None),
                     redis: redis.Redis = Depends(get_redis_client)):
        redis.delete(f"{RedisDB.auth_session}:{session}")
        response.set_cookie("session", '', max_age=0, httponly=True)
        return {"message": "OK"}

    @get("/session", summary="returns object containing email and authorized state for client", description="get current client session")
    async def get_session(self, session: str = Cookie(default=None), redis: redis.Redis = Depends(get_redis_client)):
        not_auth_data = GetAuthData(email="", authorized=False)
        if session is None:
            return not_auth_data
        user_id = redis.get(f"{RedisDB.auth_session}:{session}")
        if user_id is None:
            return not_auth_data
        user_id = user_id.decode('utf-8')
        ur = UserRepository(self.session)
        user = await ur.get_by_id(user_id)
        if user is None:
            return not_auth_data
        return GetAuthData(email=user.email, authorized=True)
