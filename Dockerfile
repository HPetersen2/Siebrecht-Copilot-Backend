FROM python:3.12-alpine

WORKDIR /app

COPY . .

RUN apk update && \
    apk add --no-cache \
        bash \
        postgresql-libs \
        postgresql-client \
        gcc \
        musl-dev \
        python3-dev \
        postgresql-dev \
        libpq && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev python3-dev postgresql-dev && \
    chmod +x entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]