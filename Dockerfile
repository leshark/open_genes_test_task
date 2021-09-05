FROM python:3.8-slim

RUN  apt update && apt install -y curl

WORKDIR /bio_stats_service

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev


ENV LANG C.UTF-8

COPY src src

# copy required data for migrations
COPY test_data test_data
COPY alembic.ini .
COPY fill_db.py .
