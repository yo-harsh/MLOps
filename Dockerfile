FROM python:3.10.13-alpine3.19

ENV PYTHONUNBUFFERED 1

COPY ./project /project
COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /project

# install dependensies
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        python3-dev gcc libc-dev libffi-dev && \
    # python env setup
    python -m venv /mlops && \
    /mlops/bin/python -m pip install --upgrade pip && \
    # installing requirement
    /mlops/bin/pip install -r /tmp/requirements.txt && \
    # remove tmp
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    # add new test user
    adduser \
        --disabled-password \
        --no-create-home \
        test-user

ENV PATH="/mlops/bin:$PATH"

USER test-user