from app.book.models import Book
from app.service.base import BaseService


class BookService(BaseService):
    """Сервис для взаимодействия с таблицей 'Книга'"""
    model = Book
