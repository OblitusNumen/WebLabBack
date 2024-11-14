import uuid

from sqlalchemy.orm import mapped_column, Mapped

from database.models.base import Base


class Good(Base):
    __tablename__ = "goods"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    img: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()
    discount: Mapped[float] = mapped_column()
    stock: Mapped[int] = mapped_column()
    name: Mapped[str] = mapped_column()
