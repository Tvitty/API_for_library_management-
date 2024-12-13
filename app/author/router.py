from fastapi import APIRouter
from sqlalchemy.util import await_only

from app.author.schemas import SAuthor, SAuthorAdd
from app.author.service import AuthorService

router = APIRouter(
    prefix="/authors",
    tags=["Авторы"]
)

@router.post("")
async def create_authors(autor: SAuthorAdd) -> None:
    await AuthorService.add(
        first_name=autor.first_name,
        last_name=autor.last_name,
        birth_date=autor.birth_date
    )

@router.get("")
async def get_all_authors() -> list[SAuthor]:
    return await AuthorService.find_all()

@router.get("/{author_id}")
async def get_info_author_by_id(author_id: int) -> SAuthor:
    return await AuthorService.find_by_id(author_id)

@router.put("/{author_id}")
async def updating_author_info_dy_id(author_id: int, author: SAuthorAdd) -> None:
    await AuthorService.update(
        author_id,
        first_name=author.first_name,
        last_name=author.last_name,
        birth_date=author.birth_date
    )

@router.delete("/{author_id}")
async def del_author_by_id(author_id: int) -> None:
    await AuthorService.delete(author_id)