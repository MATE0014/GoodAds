# ...existing code...
from fastapi import APIRouter
from app.api.v1.endpoints.societies import router as society_router

api_router = APIRouter()
api_router.include_router(society_router, prefix="", tags=["societies"])