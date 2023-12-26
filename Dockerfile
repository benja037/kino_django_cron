FROM python:3.8.6-buster

RUN apt update
RUN apt-get install cron -y
RUN alias py=python

ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/

COPY ./apps ./apps
COPY ./kinostats ./kinostats
COPY manage.py .
COPY ./requirements.txt .
COPY ./media ./media
COPY ./static ./static

RUN pip install -r requirements.txt

# django-crontab logfile
RUN mkdir /cron
RUN touch /cron/django_cron.log

EXPOSE 443

CMD  service cron start && python manage.py crontab add && python manage.py runserver 0.0.0.0:443