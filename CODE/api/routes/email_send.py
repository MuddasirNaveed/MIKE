from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, EmailStr
from api.dependencies import get_application
from apps.emails.models import EmailLog
from apps.emails.tasks import send_email_task
import uuid

router = APIRouter()

class EmailSendRequest(BaseModel):
    from_email: EmailStr
    to_email: EmailStr
    subject: str
    body: str


@router.post("/send", status_code=status.HTTP_202_ACCEPTED)
def send_email(request: EmailSendRequest, app=Depends(get_application)):
    log = EmailLog.objects.create(
        application=app,
        message_id=str(uuid.uuid4()),
        sender=request.from_email,
        recipient=request.to_email,
        subject=request.subject,
        body=request.body,
        direction='outbound',
    )
    send_email_task.delay(log.id)
    return {"message_id": log.message_id, "status": "queued"}
