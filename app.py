from fastapi import FastAPI

from routes import api_router

app = FastAPI(
    title="FastAPI & Databricks Apps",
    description="A simple FastAPI application example for Databricks Apps runtime",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {"message": "API is running", "docs": "/docs", "health": "/api/v1/healthcheck"}

app.include_router(api_router)

# Router assignment
app.include_router(api_router)
