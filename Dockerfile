FROM python:3.9-alpine3.13

# ENV PYTHONUNBUFFERED 1

COPY ./project /project
COPY ./requirements.txt /tmp/requirements.txt

RUN python -m venv /mlops && \
    /mlops/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        test-user

WORKDIR /project
USER test-user