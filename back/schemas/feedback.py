import uuid
from typing import Any

from pydantic import BaseModel
from database.models.good import Good

class Feedback(BaseModel):
    name: str
    email: str
    msg: str