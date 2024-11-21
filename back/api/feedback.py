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

    @post("/", summary="saves feedback form", description="Send feedback")
    async def send_feedback(self, feedback: Feedback):
        repo = FeedbackRepository(self.session)
        await repo.create(name=feedback.name, email=feedback.email, message=feedback.msg)
        await self.session.commit()
        return {"message": "OK"}

    @get("/all", summary="returns all feedback", description="Get feedback")
    async def getFeedback(self):
        repo = FeedbackRepository(self.session)
        feedback = await repo.get_all()
        return feedback
