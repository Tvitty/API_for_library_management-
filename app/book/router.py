from fastapi import APIRouter
from app.book.schemas import SBook, SBookAdd
from app.book.service import BookService


router = APIRouter(
    prefix="/books",
    tags=["Книги"]
)

@router.post("")
async def add_book(book: SBookAdd) -> None:
    """Эндпоинт для создания книги"""
    await BookService.add(
        book_title=book.book_title,
        description=book.description,
        author_id=book.author_id,
        available_copies=book.available_copies
    )

@router.get("")
async def get_all_books() -> list[SBook]:
    """Эндпоинт для получения списка всех книг"""
    return await BookService.find_all()

@router.get("/{book_id}")
async def get_info_book_by_id(book_id: int) -> SBook:
    """Эндпоинт для получения книги по ID"""
    return await BookService.find_by_id(book_id)

@router.put("/{book_id}")
async def updating_book_info_dy_id(book_id: int, book: SBookAdd):
    """Эндпоинт для редактирования книги по ID"""
    await BookService.update(
        book_id,
        book_title=book.book_title,
        description=book.description,
        author_id=book.author_id,
        available_copies=book.available_copies
    )

@router.delete("/{book_id}")
async def del_book_by_id(book_id: int):
    """Эндпоинт для удаления книги по ID"""
    await BookService.delete(book_id)
