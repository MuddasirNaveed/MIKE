from fastapi import APIRouter, Request, Depends
import uuid
from api.dependencies import get_application
from apps.emails.models import EmailLog
from apps.emails.tasks import forward_inbound_email

router = APIRouter()

@router.post("/")
async def receive_inbound_email(request: Request, app=Depends(get_application)):
    data = await request.json()
    log = EmailLog.objects.create(
        application=app,
        message_id=str(uuid.uuid4()),
        sender=data.get('from'),
        recipient=data.get('to'),
        subject=data.get('subject', ''),
        body=data.get('body', ''),
        direction='inbound',
        status='received'
    )
    forward_inbound_email.delay(log.id)
    return {"message_id": log.message_id, "status": "received"}
