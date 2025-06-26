from fastapi import APIRouter, HTTPException, Header, status
from pydantic import BaseModel, EmailStr
import uuid

router = APIRouter()

class EmailSendRequest(BaseModel):
    from_email: EmailStr
    to_email: EmailStr
    subject: str
    body: str

@router.post("/send")
def send_email(request: EmailSendRequest, x_api_key: str = Header(...)):
    if not x_api_key:
        raise HTTPException(status_code=403, detail="Missing API Key")
    message_id = str(uuid.uuid4())
    return {"message_id": message_id, "status": "queued"}
