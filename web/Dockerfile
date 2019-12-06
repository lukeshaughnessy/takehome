FROM python:3.6
LABEL maintainer="Peng Xiao<xiaoquwl@gmail.com>"

COPY . /

RUN pip install -r requirements.txt && pip install gunicorn

ENTRYPOINT ["/runserver.sh"]