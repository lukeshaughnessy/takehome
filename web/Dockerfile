FROM python:3.6
LABEL maintainer="lukeshaughnessy@gmail.com"

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt && pip install gunicorn
RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser && \
    chown -R appuser.appuser /app/ && \
    chmod +x /app/runserver.sh
USER appuser

ENTRYPOINT ["/app/runserver.sh"]