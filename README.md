# micro-service-app
Project that to be ready for tech taking a job

docker
redis
fastapi
dotenv
sqlalchemy
alembic
fastapi-admin
celery
nginx
monitoring


Optional Dependencies¶
Used by Pydantic:

email_validator - for email validation.
pydantic-settings - for settings management.
pydantic-extra-types - for extra types to be used with Pydantic.
Used by Starlette:

httpx - Required if you want to use the TestClient.
jinja2 - Required if you want to use the default template configuration.
python-multipart - Required if you want to support form "parsing", with request.form().
itsdangerous - Required for SessionMiddleware support.
pyyaml - Required for Starlette's SchemaGenerator support (you probably don't need it with FastAPI).
ujson - Required if you want to use UJSONResponse.
Used by FastAPI / Starlette:

uvicorn - for the server that loads and serves your application.
orjson - Required if you want to use ORJSONResponse.
You can install all of these with pip install "fastapi[all]

and we need to research about base64


bla bla
