from fastapi import FastAPI, Request
from src.api.main import api_router
from starlette import requests

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/health-check")
async def health(req: Request):
    return req.headers


app.include_router(api_router)