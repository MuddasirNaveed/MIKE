import os
import django
from django.core.asgi import get_asgi_application
from fastapi.middleware.wsgi import WSGIMiddleware
from api.main import app as fastapi_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

django_asgi_app = get_asgi_application()

from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(middleware=[
    Middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
])

app.mount("/api", fastapi_app)
app.mount("/admin", WSGIMiddleware(django_asgi_app))
