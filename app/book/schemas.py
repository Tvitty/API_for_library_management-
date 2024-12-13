from typing import Optional
from pydantic import BaseModel


class SBook(BaseModel):
    """Схема получения книг"""
    id: int
    book_title: str
    description: Optional[str] = None
    author_id: int
    available_copies: int

class SBookAdd(BaseModel):
    """Схема создания книги"""
    book_title: str
    description: Optional[str] = None
    author_id: int
    available_copies: int
