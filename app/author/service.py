from app.author.models import Author
from app.service.base import BaseService


class AuthorService(BaseService):
    """Сервис для взаимодействия с таблицей 'Автор'"""
    model = Author
