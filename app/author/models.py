from sqlalchemy import Column, String, Date, Integer, Nullable
from app.database import Base


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(Date, default=None)