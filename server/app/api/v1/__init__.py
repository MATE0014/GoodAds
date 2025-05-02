from fastapi import APIRouter
from app.api.v1.endpoints.societies import router as society_router
from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.business import router as business_router
from app.api.v1.endpoints.projects import router as projects_router

api_router = APIRouter()
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(society_router, prefix="/societies", tags=["societies"])
api_router.include_router(business_router, prefix="/businesses", tags=["businesses"])
api_router.include_router(projects_router, prefix="/projects", tags=["projects"])