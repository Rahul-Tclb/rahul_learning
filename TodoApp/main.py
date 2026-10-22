from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field


router = APIRouter(prefix="/todos", tags=["todos"])


