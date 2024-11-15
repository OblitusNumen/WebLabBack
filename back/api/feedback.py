from fastapi import Depends
from fastapi import Depends
from fastapi_controllers import Controller, post
from sqlalchemy.ext.asyncio import AsyncSession

from back.schemas.feedback import Feedback
from database.database import get_db_session
from database.repositories.feedback_repository import FeedbackRepository


class FeedbackController(Controller):
    prefix = '/feedback'
    tags = ['feedback']

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    @post("/")
    async def send_feedback(self, feedback: Feedback):
        await FeedbackRepository(self.session).create(name=feedback.name, email=feedback.email, message=feedback.msg)
        return { "message": "OK"}