from datetime import date
from pydantic import BaseModel


class SBorrow(BaseModel):
    """Схема получения выдач"""
    id: int
    book_id: int
    reader_name: str
    issue_date: date
    return_date: date

class SBorrowAdd(BaseModel):
    book_id: int
    reader_name: str
    issue_date: date

class SBorrowPatch(BaseModel):
    """Схема создания книги"""
    return_date: date

class SBorrowReturn(BaseModel):
    """Схема возврата ID выдачи"""
    id: int
