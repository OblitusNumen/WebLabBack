import uuid

from sqlalchemy.orm import mapped_column, Mapped

from database.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    email: Mapped[str]
    hashed_password: Mapped[str]
