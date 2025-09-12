from fastapi import APIRouter, Depends
from src.core.db import get_db
from src.common.schemas import UserCreate, UserOut
from src.common.models import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("", response_model=UserOut)
async def create_user(data: UserCreate, db = Depends(get_db)):
    user_data = data.model_dump()
    db_user = User(**user_data)  
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user