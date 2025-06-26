from django.db import models
from apps.applications.models import Application

class Webhook(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='webhook')
    endpoint_url = models.URLField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.application.name} → {self.endpoint_url}"
