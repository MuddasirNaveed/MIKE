from celery import shared_task
from django.conf import settings
from .models import EmailLog
import boto3
import requests

@shared_task
def send_email_task(email_log_id):
    email_log = EmailLog.objects.get(id=email_log_id)
    ses = boto3.client(
        'ses',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION,
    )
    try:
        ses.send_email(
            Source=email_log.sender,
            Destination={'ToAddresses': [email_log.recipient]},
            Message={
                'Subject': {'Data': email_log.subject},
                'Body': {'Text': {'Data': email_log.body}},
            },
        )
        email_log.status = 'sent'
    except Exception as e:
        email_log.status = f'error: {e}'
    email_log.save()
    return email_log.message_id

@shared_task
def forward_inbound_email(email_log_id):
    email_log = EmailLog.objects.get(id=email_log_id)
    url = email_log.application.webhook.endpoint_url
    try:
        requests.post(url, json={
            'message_id': email_log.message_id,
            'sender': email_log.sender,
            'recipient': email_log.recipient,
            'subject': email_log.subject,
            'body': email_log.body,
        }, timeout=10)
    except Exception:
        pass
