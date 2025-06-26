from django.contrib import admin
from .models import Application, APIKey

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'is_active')
    search_fields = ('name',)

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('application', 'key', 'created_at', 'is_active')
    search_fields = ('application__name', 'key')
    readonly_fields = ('key',)
