#use slim image to reduce size and set as ARG, can be overridden at build
ARG PYTHON_VERSION=3.6-slim-buster

FROM python:$PYTHON_VERSION

#recommended for versions < 3.7 
ENV PYTHONUNBUFFERED 1

#defaults to dev, can be overridden at build time eg "prod"
ARG BUILD_ENV=dev

#pass args into env
ENV BUILD_ENV="$BUILD_ENV"
ENV PYTHON_VERSION="$PYTHON_VERSION"

#populate metadata
LABEL maintainer="lukeshaughnessy@gmail.com"
LABEL app.distro.name=linux
LABEL app.distro.release=debian
LABEL app.image.name=app-web
LABEL app.build.env="$BUILD_ENV"
LABEL app.python.version="$PYTHON_VERSION"

COPY . /app
WORKDIR /app

#install gunicorn for use in prod 
#it's also possible here to compile wheels and do a multipart build 
#but that's just showing off
RUN pip install -r requirements.txt && pip install gunicorn

#add user and group to avoid running app as root
RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser && \
    chown -R appuser.appuser /app/ && \
    chmod +x /app/runserver.sh
USER appuser

ENTRYPOINT ["/app/runserver.sh"]