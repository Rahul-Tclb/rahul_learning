from fastapi import FastAPI
from contextlib import asynccontextmanager


from routes import api_router
# from routes import api_router_v2

from TodoApp.database import Base, engine
from TodoApp.main import router as todo_router
import TodoApp.models  

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Creates the table for a basic app. Use migrations for production changes.
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title="FastAPI & Databricks Apps",
    description="A simple FastAPI application example for Databricks Apps runtime",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {"message": "API is running", "docs": "/docs", "health": "/api/v1/healthcheck"}

# app.include_router(api_router)

# Router assignment
app.include_router(api_router)
app.include_router(todo_router, prefix="/api/v1")
# app.include_router(api_router_v2)
