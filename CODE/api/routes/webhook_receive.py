from fastapi import APIRouter, Request, Header, HTTPException
import uuid

router = APIRouter()

@router.post("/")
async def receive_inbound_email(request: Request, x_api_key: str = Header(...)):
    if not x_api_key:
        raise HTTPException(status_code=403, detail="Missing API Key")
    data = await request.json()
    message_id = str(uuid.uuid4())
    return {"message_id": message_id, "status": "received", "content": data}
