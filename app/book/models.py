from sqlalchemy import Column, String, Integer, ForeignKey
from app.database import Base


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, nullable=False)
    book_title = Column(String, nullable=False)
    description = Column(String)
    author_id = Column(ForeignKey("author.id"), nullable=False)
    available_copies = Column(Integer, nullable=False)
