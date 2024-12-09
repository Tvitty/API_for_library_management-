from sqlalchemy import Column, String, Integer, Date, ForeignKey
from app.database import Base


class Borrow(Base):
    __tablename__ = "borrow"

    id = Column(Integer, primary_key=True)
    book_id = Column(ForeignKey("book.id"))
    reader_name = Column(String, nullable=False)
    issue_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=False)