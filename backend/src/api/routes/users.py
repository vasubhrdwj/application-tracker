from fastapi import APIRouter, Depends
from src.core.db import get_db
from src.common.schemas import UserCreate, UserOut, UserUpdate
from src.common.models import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("", response_model=list[UserOut])
def get_users(db = Depends(get_db), skip: int = 0, limit: int = 20):
    """ Retrieve a list of users with pagination support."""

    users = db.query(User).offset(skip).limit(limit).all()
    if not users:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="No users found")
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


@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db = Depends(get_db)):
    """ Retrieve a user by their ID."""

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.patch("/{user_id}", response_model=UserOut)
def update_user(user_id: int, data: UserUpdate, db = Depends(get_db)):
    """ Update an existing user's information."""

    user = db.query(User).filter(User.id == user_id)
    user_instance = user.first()
    if user_instance is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="User not found")

    update_data = data.model_dump(exclude_unset=True)
    user.update(update_data, synchronize_session=False)
    
    db.commit()
    db.refresh(user_instance)
    return user_instance