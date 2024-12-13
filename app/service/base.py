from app.database import async_session_maker
from sqlalchemy import select, insert, update, delete


class BaseService:
    """Базовый сервис для взаимодействия с таблицами"""
    model = None

    @classmethod
    async def find_all(cls):
        """Метод для поиска и возврата всех записей в таблице"""
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_by_id(cls, model_id: int):
        """Метод для поиска и возврата записи в таблице по ID"""
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(id=model_id)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def add(cls, **data):
        """Метод для добавления записи в таблицу"""
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, model_id, **data):
        """Метод для обновления записи в таблице по ID"""
        async with async_session_maker() as session:
            query = update(cls.model).values(**data).where(cls.model.id == model_id)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, model_id):
        """Метод для удаления записи в таблице по ID"""
        async with async_session_maker() as session:
            query = delete(cls.model).where(cls.model.id == model_id)
            await session.execute(query)
            await session.commit()