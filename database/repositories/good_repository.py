from typing import Optional
from uuid import UUID

from sqlalchemy import select, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.good import Good


class GoodRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, name: str, img: str, price: float, discount: float, stock: int) -> Optional[Good]:
        good = Good(name=name, img=img, price=price, discount=discount, stock=stock)
        self.session.add(good)
        await self.session.flush()
        return await self.get_by_id(good.id)

    async def get_by_id(self, id: UUID) -> Optional[Good]:
        stmt = select(Good).where(Good.id == id).limit(1)
        return await self.session.scalar(stmt)

    async def get_all(self) -> ScalarResult[Good]:
        stmt = select(Good)
        return await self.session.scalars(stmt)
