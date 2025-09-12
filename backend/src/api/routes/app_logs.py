import json
from fastapi import APIRouter, Depends
from src.core.db import get_db
from src.common.schemas import ApplicationBase, UserCreate
from src.common.models import Application 

router = APIRouter(prefix="/applications", tags=["Applications"])


@router.post("", response_model=ApplicationBase)
async def create_application(app_data: ApplicationBase, db = Depends(get_db)):
    data = app_data.model_dump()
    db_app = Application(**data)  
    
    db.add(db_app)
    db.commit()

    return app_data

