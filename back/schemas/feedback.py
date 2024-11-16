from pydantic import BaseModel


class Feedback(BaseModel):
    name: str
    email: str
    msg: str
