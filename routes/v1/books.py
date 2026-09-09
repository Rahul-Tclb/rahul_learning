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

# a simple get request to get all the books

@router.get("/books")
async def read_all_books():
    print("GET /books")
    return BOOKS

"""
path parameters request parameters that have been attachd to the URL
"""
@router.get("/books/title/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            return book
    return {"data": "Not Found"}


"""
query parameters are requested that have been attached after a ?
"""

@router.get("/books/by-category")
async def read_books_by_category(category: str):
    return [b for b in BOOKS if b["category"].casefold() == category.casefold()]


# @router.get("/books/by-author-category")
# async def read_books_by_author_category(author: str, category: str):
#     return [
#         b for b in BOOKS
#         if b["author"].casefold() == author.casefold()
#         and b["category"].casefold() == category.casefold()
#     ]


"""
used to create data 
post can have a body that has additional information
"""
@router.post("/books")
async def create_book(book: dict = Body(...)):
    BOOKS.append(book)
    return book


"""
used to update data
"""

@router.put("/books")
async def update_book(book: dict = Body(...)):
    for i, b in enumerate(BOOKS):
        if b["title"].casefold() == book["title"].casefold():
            BOOKS[i] = book
            return book
    return {"data": "Not Found"}



""" used to delete  data 
"""
@router.delete("/books/{book_title}")
async def delete_book(book_title: str):
    for i, b in enumerate(BOOKS):
        if b["title"].casefold() == book_title.casefold():
            BOOKS.pop(i)
            return {"data": "Deleted"}
    return {"data": "Not Found"}







