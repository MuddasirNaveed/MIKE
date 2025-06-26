from django.contrib import admin
from .models import Webhook

@admin.register(Webhook)
class WebhookAdmin(admin.ModelAdmin):
    list_display = ('application', 'endpoint_url', 'is_active', 'created_at')
    search_fields = ('application__name', 'endpoint_url')
    list_filter = ('is_active',)
