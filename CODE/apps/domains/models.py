from django.db import models
from django.conf import settings
from apps.applications.models import Application
import boto3

class Domain(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='domains')
    domain_name = models.CharField(max_length=255, unique=True)
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=64, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.verification_token:
            ses = boto3.client(
                "ses",
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                region_name=settings.AWS_REGION,
            )
            resp = ses.verify_domain_identity(Domain=self.domain_name)
            self.verification_token = resp.get("VerificationToken", "")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.domain_name
