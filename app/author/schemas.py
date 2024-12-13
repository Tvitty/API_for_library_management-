from datetime import date
from typing import Optional
from pydantic import BaseModel


class SAuthor(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_date: Optional[date] = None

class SAuthorAdd(BaseModel):
    first_name: str
    last_name: str
    birth_date: Optional[date] = None
