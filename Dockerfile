FROM python:3.10 AS builder

ARG PIP_EXTRA_INDEX_URL
ARG PIP_TRUSTED_HOST

ENV PYTHONUNBUFFERED 1
ENV PORT=${PORT:-5035}

# RUN mkdir -p /code/air_sensor/metrics_data

WORKDIR /code/

COPY requirements.txt .

RUN pip install -r requirements.txt --prefix=/install --trusted-host ${PIP_TRUSTED_HOST-localhost}


FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
COPY --from=builder /install /usr/local
WORKDIR /code/

COPY air_sensor ./air_sensor
COPY metrics_data ./metrics_data
CMD rm ./metrics_data/*
