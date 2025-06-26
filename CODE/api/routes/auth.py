from fastapi import APIRouter, Depends
from api.dependencies import get_application

router = APIRouter()

@router.get("/verify")
def verify_token(app=Depends(get_application)):
    return {"status": "valid", "application": app.name}
