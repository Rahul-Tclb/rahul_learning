from fastapi import APIRouter, Body

router = APIRouter()

Books_2  = [{'1' : 'No Books created'}]

@router.get('/books')
async def get_books():
  return Books_2
