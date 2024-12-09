from sqlalchemy import Column, String, Date, Integer
from app.database import Base


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(Date)