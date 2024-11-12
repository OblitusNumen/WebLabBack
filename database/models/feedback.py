import uuid

from sqlalchemy.orm import mapped_column, Mapped

from database.models.base import Base


class Feedback(Base):
    __tablename__ = "feedback"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    msg: Mapped[str] = mapped_column()
