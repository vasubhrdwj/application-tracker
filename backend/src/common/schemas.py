from pydantic import BaseModel
from datetime import date
from pydantic import EmailStr, Field

#Application Schema
class ApplicationBase(BaseModel):
    job_title: str
    company: str
    status: str = "applied"  # default status
    date_applied: date = date.today()
    notes: str | None = None


#User Schema
class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = Field(default=None, max_length=100)
    is_active: bool = True

class UserCreate(UserBase):
    password: str = Field(min_length=8)

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

