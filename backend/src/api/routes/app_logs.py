import json
from fastapi import APIRouter, Depends
from src.core.db import get_db
from src.common.schemas import ApplicationLog, UserCreate
from src.common.models import Application 

router = APIRouter(prefix="/applications", tags=["applications"])


@router.post("", response_model=ApplicationLog)
async def create_application(app_data: ApplicationLog, db = Depends(get_db)):
    data = app_data.model_dump()
    db_app = Application(**data)  
    
    db.add(db_app)
    db.commit()

    return app_data

@router.post("/user")
async def create_user(data: UserCreate):
    return data
