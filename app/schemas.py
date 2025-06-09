from pydantic import BaseModel
from datetime import datetime


class PostCreate(BaseModel):
    title: str
    content: str



class PostRead(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime


class PostUpdate(BaseModel):
    title: str
    content: str





