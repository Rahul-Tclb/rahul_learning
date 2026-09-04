"""V1 API routes."""

from fastapi import APIRouter
from .healthcheck import router as healthcheck_router
from .books import router as books_router

router = APIRouter()

# Include endpoint-specific routers
router.include_router(healthcheck_router)
router.include_router(books_router)