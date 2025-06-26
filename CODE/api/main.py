from fastapi import FastAPI
from api.routes import email_send, webhook_receive, auth

app = FastAPI(title="Email Integration API", version="1.0")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(email_send.router, prefix="/email", tags=["email"])
app.include_router(webhook_receive.router, prefix="/webhook", tags=["webhook"])
