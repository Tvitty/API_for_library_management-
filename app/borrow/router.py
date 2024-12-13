from datetime import date
from fastapi import APIRouter
from app.borrow.schemas import SBorrow, SBorrowReturn
from app.borrow.service import BorrowService

router = APIRouter(
    prefix="/borrows",
    tags=["Выдача книг"]
)

@router.post("")
async def add_borrow(book_id: int, reader_name: str, issue_date:date)-> SBorrowReturn:
    """Эндпоинт для создания выдачи"""
    return await BorrowService.add(book_id, reader_name, issue_date)

@router.get("")
async def get_all_borrows() -> list[SBorrow]:
    """Эндпоинт для получения списка всех выдач"""
    return await BorrowService.find_all()

@router.get("/{borrow_id}")
async def get_info_borrow_by_id(borrow_id: int) -> SBorrow:
    """Эндпоинт для получения выдачи по ID"""
    return await BorrowService.find_by_id(borrow_id)

@router.patch("/{borrow_id}/return")
async def closing_borrow_by_id(borrow_id: int, return_date: date) -> None:
    """Эндпоинт для закрытия выдачи по ID"""
    await BorrowService.patch(borrow_id, return_date)
