from fastapi import APIRouter, Body

router = APIRouter()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]

@router.get("/books")
async def read_all_books():
    print("GET /books")
    return BOOKS

# @router.get("/books/title/{book_title}")
# async def read_book(book_title: str):
#     for book in BOOKS:
#         if book["title"].casefold() == book_title.casefold():
#             return book
#     return {"data": "Not Found"}

# @router.get("/books/by-category")
# async def read_books_by_category(category: str):
#     return [b for b in BOOKS if b["category"].casefold() == category.casefold()]

# @router.get("/books/by-author-category")
# async def read_books_by_author_category(author: str, category: str):
#     return [
#         b for b in BOOKS
#         if b["author"].casefold() == author.casefold()
#         and b["category"].casefold() == category.casefold()
#     ]

# @router.post("/books")
# async def create_book(book: dict = Body(...)):
#     BOOKS.append(book)
#     return book

# @router.put("/books")
# async def update_book(book: dict = Body(...)):
#     for i, b in enumerate(BOOKS):
#         if b["title"].casefold() == book["title"].casefold():
#             BOOKS[i] = book
#             return book
#     return {"data": "Not Found"}

# @router.delete("/books/{book_title}")
# async def delete_book(book_title: str):
#     for i, b in enumerate(BOOKS):
#         if b["title"].casefold() == book_title.casefold():
#             BOOKS.pop(i)
#             return {"data": "Deleted"}
#     return {"data": "Not Found"}