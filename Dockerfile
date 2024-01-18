FROM python:3.10.12-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./project /app/project
COPY ./requirements.txt /tmp/requirements.txt

# install dependensies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    python -m venv /mlops && \
    /mlops/bin/python -m pip install --upgrade pip setuptools && \
    /mlops/bin/pip install --no-cache-dir -r /tmp/requirements.txt && \
    apt-get remove -y build-essential && \
    apt-get autoremove -y && \
    rm -rf /tmp/* /var/lib/apt/lists/*

ENV PATH="/mlops/bin:$PATH"

WORKDIR /app/project
