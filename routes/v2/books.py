from fastapi import APIRouter, Body
from pydantic import BaseModel , Field

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
    book_id: optional[int] =  None
    title: str = Field(min_length=5 , max_length=10)
    author: str = Field(min_length= 6 , max_length=100)
    description: str = Field(min_length= 6 , max_length=100)
    rating: int = Field(gt=0 , lt=5)





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
async def read_all_books():
    print("Reading all books")
    return books_v2


# @router_v2.post('/add_book_api')
# async def create_book_v2(add_book= Body()):
#     books_v2.append(add_book)


@router_v2.post('/create-book')
async def create_book_v2_pydantic(book_request : BookRequest):
    new_book = Book(**book_request.model_dump())
    print(type(new_book))
    books_v2.append(find_book_id(new_book))

# write a function to auto incremet the id of the book
def find_book_id(book: Book):
    book.id = 1 if len(books_v2) == 0 else books_v2[-1].id + 1
    # if len(books_v2)> 0:
    #     book.id = books_v2[-1].id + 1
    # else:
    #     book.id = 1
    
    return book


    
