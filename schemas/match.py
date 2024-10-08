import uuid
from datetime import datetime

from pydantic import BaseModel


class MatchSchema(BaseModel):
    id: uuid.UUID

    opponent_team: str

    date: datetime

    result: str

    stadium: str
