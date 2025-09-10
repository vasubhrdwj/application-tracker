from fastapi import APIRouter
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

router = APIRouter(prefix="/applications", tags = ["applications"])


# Define the Pydantic model for a Job Application
class Application(BaseModel):
    id: int
    user_name: str
    job_title: str
    company: str
    status: str = "applied"  # default status
    date_applied: date = date.today()
    notes: str | None = None

# In-memory "database"
applications: list[Application] = []

# Create endpoint: accepts an Application and returns it
@router.post("/applicationlog/", response_model=Application)
async def create_application(app_data: Application):
    applications.append(app_data)
    return app_data
