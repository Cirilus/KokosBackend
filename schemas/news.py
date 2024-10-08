import uuid
from datetime import datetime

from pydantic import BaseModel



class NewsCreateRequest(BaseModel):
    title: str
    content: str


class NewsResponse(BaseModel):
    id: uuid.UUID

    title: str
    content: str

    created_at: datetime
    updated_at: datetime
