from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from api.dependencies import get_application
from django.conf import settings
import boto3

router = APIRouter()

class EmailVerificationRequest(BaseModel):
    email: EmailStr


class DomainVerificationRequest(BaseModel):
    domain: str


@router.post("/verify", status_code=status.HTTP_202_ACCEPTED)
def verify_email(request: EmailVerificationRequest, app=Depends(get_application)):
    """Send a verification email via AWS SES to the provided address."""
    ses = boto3.client(
        "ses",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION,
    )
    try:
        ses.verify_email_identity(EmailAddress=request.email)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return {"detail": "verification_sent", "email": request.email}


@router.post("/verify-domain", status_code=status.HTTP_202_ACCEPTED)
def verify_domain(request: DomainVerificationRequest, app=Depends(get_application)):
    """Request a domain verification token from AWS SES."""
    ses = boto3.client(
        "ses",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION,
    )
    try:
        response = ses.verify_domain_identity(Domain=request.domain)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return {"domain": request.domain, "token": response.get("VerificationToken")}
