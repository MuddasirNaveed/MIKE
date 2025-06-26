from django.db import models
from apps.applications.models import Application

class EmailLog(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='emails')
    message_id = models.CharField(max_length=255, unique=True)
    sender = models.EmailField()
    recipient = models.EmailField()
    subject = models.CharField(max_length=512)
    body = models.TextField()
    direction = models.CharField(max_length=10, choices=(('inbound', 'Inbound'), ('outbound', 'Outbound')))
    status = models.CharField(max_length=50, default='queued')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.direction.upper()} - {self.subject[:40]}"
