from fastapi import APIRouter
from src.api.routes import app_logs, users

api_router = APIRouter()

api_router.include_router(app_logs.router)
api_router.include_router(users.router)


