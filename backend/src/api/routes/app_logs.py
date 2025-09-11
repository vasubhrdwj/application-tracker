from fastapi import APIRouter
from src.common.schemas import Application

router = APIRouter(prefix="/applications", tags = ["applications"])

# In-memory "database"
applications: list[Application] = []

# Create endpoint: accepts an Application and returns it
@router.post("/applicationlog/", response_model=Application)
async def create_application(app_data: Application):
    applications.append(app_data)
    return app_data
