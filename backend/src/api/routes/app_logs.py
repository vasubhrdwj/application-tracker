import json
from fastapi import APIRouter, Depends
from src.core.db import get_db
from src.common.schemas import Application, UserCreate
from src.common.models import Application as ApplicationModel

router = APIRouter(prefix="/applications", tags=["applications"])


@router.post("", response_model=Application)
async def create_application(app_data: Application, db = Depends(get_db)) -> Application:
    data = app_data.model_dump()
    db_app = ApplicationModel(**data)  
    
    db.add(db_app)
    db.commit()

    return app_data

@router.post("/user")
async def create_user(data: UserCreate):
    return data
