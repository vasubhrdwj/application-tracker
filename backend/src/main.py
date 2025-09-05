from fastapi import FastAPI
from src.api.main import api_router

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


app.include_router(api_router)