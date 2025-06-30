# Third-Party Email Integration Server

This project provides a simple backend combining **Django** and **FastAPI** to send and receive emails on behalf of third‑party applications. Emails are delivered via Amazon SES and inbound messages are forwarded to application defined webhooks.

## Features
- Registration of applications and API keys via Django admin
- Domain and webhook management
- REST API for sending emails (`/api/email/send`)
- Webhook endpoint for receiving inbound emails (`/api/webhook/`)
- Asynchronous processing using Celery and Redis

## Setup
1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Configure environment variables (e.g. in a `.env` file):
   ```
   SECRET_KEY=changeme
   POSTGRES_DB=email_service
   POSTGRES_USER=user
   POSTGRES_PASSWORD=password
   POSTGRES_HOST=localhost
   AWS_ACCESS_KEY_ID=your_key
   AWS_SECRET_ACCESS_KEY=your_secret
   AWS_REGION=us-east-1
   REDIS_URL=redis://localhost:6379/0
   ```
3. Run migrations and create a superuser
   ```bash
   ./manage.py migrate
   ./manage.py createsuperuser
   ```
4. Start the development server
   ```bash
   uvicorn core.asgi:app --reload
   ```
5. Start Celery worker in another terminal
   ```bash
   celery -A core worker -l info
   ```

## Usage
- Obtain an API key from the Django admin.
- Verify sender addresses by POSTing an email to `/api/auth/verify` with your API key and JSON body `{ "email": "address@example.com" }`.
- Verify domains by POSTing to `/api/auth/verify-domain` with JSON `{ "domain": "example.com" }` and add the returned token as a TXT record.
- Send emails by POSTing to `/api/email/send` with your API key in the `X-API-Key` header.
- Configure your email provider to POST inbound messages to `/api/webhook/` with the same header.

Using a tool like **Postman** is recommended for calling these endpoints during development.

This repository provides a minimal but functional foundation which can be extended with additional features such as domain verification and analytics.
