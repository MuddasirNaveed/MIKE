from django.contrib import admin
from .models import EmailLog

@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'application', 'direction', 'status', 'created_at')
    search_fields = ('message_id', 'sender', 'recipient', 'subject')
    list_filter = ('direction', 'status')
