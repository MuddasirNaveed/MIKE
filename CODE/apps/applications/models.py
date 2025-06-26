from django.db import models
import secrets

class Application(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class APIKey(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='api_keys')
    key = models.CharField(max_length=64, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = secrets.token_hex(32)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.application.name} - {self.key[:8]}"
