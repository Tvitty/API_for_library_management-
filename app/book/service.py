from app.book.models import Book
from app.service.base import BaseService


class BookService(BaseService):
    model = Book
