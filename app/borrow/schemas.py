from datetime import date
from pydantic import BaseModel


class SBorrow(BaseModel):
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
    return_date: date

class SBorrowReturn(BaseModel):
    id: int