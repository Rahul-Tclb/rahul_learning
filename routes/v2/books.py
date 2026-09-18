from fastapi import APIRouter, Body
from pydantic import BaseModel

router_v2 = APIRouter()

# books_v2  = [{'1' : 'No Books created'}]


class Book:
    def __init__(
        self, 
        book_id: int, 
        title: str, 
        author: str, 
        description: str, 
        rating: float
        ):
        self.id: int = book_id
        self.title: str = title
        self.author: str = author
        self.description: str = description
        self.rating: float = rating

    # def get_summary(self) -> str:
    #     """Returns a formatted string with the book's details."""
    #     return f"'{self.title}' by {self.author} - Rating: {self.rating}/5\nDescription: {self.description}"


class BookRequest(BaseModel):
    book_id: int
    title: str
    author: str
    description: str
    rating: float





books_v2 = [
    Book(
        book_id=1,
        title="The Hobbit",
        author="J.R.R. Tolkien",
        description="A fantasy novel about the adventures of Bilbo Baggins.",
        rating=4.8
    ),
    Book(
        book_id=2,
        title="Harry Potter and the Sorcerer's Stone",
        author="J.K. Rowling",
        description="A young wizard discovers his magical heritage at Hogwarts.",
        rating=4.9
    ),
    Book(
        book_id=3,
        title="Percy Jackson & the Olympians: The Lightning Thief",
        author="Rick Riordan",
        description="A teenager discovers he is the son of Greek god Poseidon.",
        rating=4.7
    )
]


@router_v2.get('/books')
async def get_books():
  return books_v2


@router_v2.post('/add_book_api')
async def create_book_v2(add_book= Body()):
    books_v2.append(add_book)


@router_v2.post('/add_book_with_pydantic')
async def create_book_v2_pydantic(add_book= BookRequest):
    books_v2.append(add_book)
    
