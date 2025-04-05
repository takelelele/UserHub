FROM python:3.12-alpine

RUN pip install poetry==1.8.3

WORKDIR /UserHUB

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

RUN poetry run alembic init migrations

COPY src/migrations migrations/

COPY src/ ./
