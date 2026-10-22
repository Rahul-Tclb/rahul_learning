
from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.orm import Session
from sqlalchemy import select

from TodoApp import models
from .database import engine, get_db

# Create the 'todos' table if it does not exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo App")
router = APIRouter(prefix="/todos", tags=["todos"])


# --- Response schema --------------------------------------------------------
class TodoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    priority: int = Field(ge=1, le=5)
    completed: bool


# --- GET endpoints ----------------------------------------------------------
@router.get("/", response_model=list[TodoResponse], status_code=status.HTTP_200_OK)
def read_all(db: Session = Depends(get_db)):
    return db.scalars(select(models.Todos)).all()


@router.get("/{todo_id}", response_model=TodoResponse, status_code=status.HTTP_200_OK)
def read_one(todo_id: int, db: Session = Depends(get_db)):
    todo = db.get(models.Todos, todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo


app.include_router(router)


