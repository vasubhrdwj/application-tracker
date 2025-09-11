from fastapi import FastAPI, Request
from src.api.main import api_router
from src.core.config import settings

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Server running on port 8080"}

@app.get("/health-check")
async def health(req: Request):
    return req.headers


app.include_router(api_router)