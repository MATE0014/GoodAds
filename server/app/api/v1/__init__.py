# ...existing code...
from fastapi import APIRouter
from app.api.v1.endpoints.societies import router as society_router
from app.api.v1.endpoints.auth import router as auth_router

api_router = APIRouter()
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(society_router, prefix="", tags=["societies"])