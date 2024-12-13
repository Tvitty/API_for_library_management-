from sqlalchemy import Column, String, Integer, Date, ForeignKey
from app.database import Base


class Borrow(Base):
    """Модель для таблицы 'Выдача'"""
    __tablename__ = "borrow"

    id = Column(Integer, primary_key=True, nullable=False)
    book_id = Column(ForeignKey("book.id"), nullable=False)
    reader_name = Column(String, nullable=False)
    issue_date = Column(Date, nullable=False)
    return_date = Column(Date)
