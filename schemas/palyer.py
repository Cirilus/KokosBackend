import uuid
from datetime import datetime

from pydantic import BaseModel



class PlayerSchema(BaseModel):
    id: uuid.UUID

    firstname: str
    middelname: str
    lastname: str

    played_from: datetime

    biography: str
    position: str
    achievements: str
