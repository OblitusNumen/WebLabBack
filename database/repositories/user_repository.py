from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from werkzeug.security import generate_password_hash, check_password_hash

from database.models.user import User


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, email: str, pw: str) -> Optional[User]:
        user = User(email=email, hashed_password=generate_password_hash(pw))
        self.session.add(user)
        await self.session.flush()
        return await self.get_by_id(user.id)

    async def get_by_id(self, id: UUID) -> Optional[User]:
        stmt = select(User).where(User.id == id).limit(1)
        return await self.session.scalar(stmt)

    async def get_by_email(self, email: str) -> Optional[User]:
        stmt = select(User).where(User.email == email).limit(1)
        return await self.session.scalar(stmt)

    async def get_by_auth(self, email: str, pw: str) -> Optional[User]:
        stmt = select(User).where(User.email == email).limit(1)
        user: User = await self.session.scalar(stmt)
        if user is None:
            return None
        if not check_password_hash(user.hashed_password, pw):
            return None
        return user
