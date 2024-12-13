from fastapi import HTTPException, status
from app.book.models import Book
from app.borrow.models import Borrow
from app.database import async_session_maker
from app.service.base import BaseService
from sqlalchemy import update, insert, select


class BorrowService(BaseService):
    """Сервис для взаимодействия с таблицей 'Выдача'"""
    model = Borrow

    @classmethod
    async def add(cls, book_id, reader_name, issue_date):
        """
        Метод добавления выдачи с проверкой экземпляров книг
        с изменением количества экземпляров книг
        """
        async with async_session_maker() as session:
            get_copies = select(Book.available_copies).filter_by(id=book_id)
            copies = await session.execute(get_copies)
            copies: int = copies.scalar()
            if copies > 0:
                borrow_add = insert(cls.model).values(
                book_id= book_id,
                reader_name=reader_name,
                issue_date=issue_date,
                ).returning(cls.model.id)
                new_borrow = await session.execute(borrow_add)
                subtract_copies = update(Book).\
                values(available_copies=Book.available_copies-1).filter_by(id=book_id)
                await session.execute(subtract_copies)
                await session.commit()
                return new_borrow.mappings().one()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Книги закончились"
            )

    @classmethod
    async def patch(cls, borrow_id, return_date):
        """Метод закрытия выдачи с изменением количества экземпляров книг"""
        async with async_session_maker() as session:
            issue_closure = update(cls.model).values(return_date=return_date).filter_by(id=borrow_id)
            await session.execute(issue_closure)
            add_copies = update(Book).\
                values(available_copies=Book.available_copies+1).filter_by(id=Borrow.book_id)
            await session.execute(add_copies)
            await session.commit()
