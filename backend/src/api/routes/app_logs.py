from fastapi import APIRouter

router = APIRouter(prefix="/applications", tags = ["applications"])

@router.get("/test_api")
async def test_api():
    return {"status" : "success"}

# TODO: Arpita
# Create a model application with suitable fields
# create a basic create endpoint, that takes in the application and returns it
