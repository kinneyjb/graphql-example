FROM python:3.7-alpine

ENV SERVICE_USER app
ENV SERVICE_GROUP app

RUN pip install pipenv && \
    addgroup -g 1000 -S $SERVICE_USER && \
    adduser -u 1000 -S $SERVICE_USER -G $SERVICE_GROUP && \
    mkdir -p /opt/service

COPY src /opt/service

WORKDIR /opt/service

RUN chown -R $SERVICE_USER:$SERVICE_GROUP .

USER 1000

RUN pipenv sync && \
    pipenv install gunicorn

ENTRYPOINT pipenv run gunicorn --bind 0.0.0.0:8080 wsgi
