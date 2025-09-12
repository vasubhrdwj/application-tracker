from fastapi import APIRouter, Depends
from src.core.db import get_db
from src.common.schemas import UserCreate, UserOut
from src.common.models import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("", response_model=list[UserOut])
def get_users(db = Depends(get_db), skip: int = 0, limit: int = 20):
    """ Retrieve a list of users with pagination support."""
    
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@router.post("", response_model=UserOut)
async def create_user(data: UserCreate, db = Depends(get_db)):
    """ Create a new user in the database."""

    user_data = data.model_dump()
    db_user = User(**user_data)  
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user