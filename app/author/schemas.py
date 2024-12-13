from datetime import date
from typing import Optional
from pydantic import BaseModel


class SAuthor(BaseModel):
    """Схема получения авторов"""
    id: int
    first_name: str
    last_name: str
    birth_date: Optional[date] = None

class SAuthorAdd(BaseModel):
    """Схема создания автора"""
    first_name: str
    last_name: str
    birth_date: Optional[date] = None
