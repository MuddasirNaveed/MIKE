from fastapi import Header, HTTPException, Depends
from django.db.models import Q
from apps.applications.models import APIKey

async def get_application(x_api_key: str = Header(...)):
    try:
        api_key = APIKey.objects.select_related('application').get(Q(key=x_api_key), is_active=True, application__is_active=True)
    except APIKey.DoesNotExist:
        raise HTTPException(status_code=403, detail='Invalid API Key')
    return api_key.application
