from fastapi import FastAPI
from app.author.router import router as router_author
from app.book.router import router as router_book
from app.borrow.router import router as router_borrow


app = FastAPI()

app.include_router(router_author)
app.include_router(router_book)
app.include_router(router_borrow)
