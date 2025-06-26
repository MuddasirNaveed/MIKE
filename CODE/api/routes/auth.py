from fastapi import APIRouter, Header, HTTPException

router = APIRouter()

@router.get("/verify")
def verify_token(x_api_key: str = Header(...)):
    if not x_api_key or len(x_api_key) < 32:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return {"status": "valid"}
