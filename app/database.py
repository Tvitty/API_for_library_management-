from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings as s

DATA_BASE_URL = f"postgresql+asyncpg://{s.DB_USER}:{s.DB_PASS}@{s.DB_HOST}:{s.DB_PORT}/{s.DB_NAME}"
"""Данные для подключения к БД"""

engine = create_async_engine(DATA_BASE_URL)
"""Движок для подключения к БД"""

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
"""Генератор сессий"""

class Base(DeclarativeBase):
    """Класс для миграций"""
    pass
