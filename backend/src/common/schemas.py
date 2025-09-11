from pydantic import BaseModel
from datetime import date

class Application(BaseModel):
    id: int
    user_name: str
    job_title: str
    company: str
    status: str = "applied"  # default status
    date_applied: date = date.today()
    notes: str | None = None