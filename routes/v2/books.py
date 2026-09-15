from fastapi import APIRouter, Body

router_v2 = APIRouter()

books_v2  = [{'1' : 'No Books created'}]

@router_v2.get('/books')
async def get_books():
  return books_v2
