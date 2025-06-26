from django.contrib import admin
from .models import Domain

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain_name', 'application', 'is_verified', 'created_at')
    search_fields = ('domain_name', 'application__name')
    list_filter = ('is_verified',)
    readonly_fields = ('verification_token',)
