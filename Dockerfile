FROM zenmldocker/zenml:0.52.0-py3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./project /app/project
COPY ./requirements.txt /tmp/requirements.txt

# install dependensies
RUN python -m venv /mlops && \
    /mlops/bin/python -m pip install --upgrade pip && \
    /mlops/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

ENV PATH="/mlops/bin:$PATH"

WORKDIR /app/project
