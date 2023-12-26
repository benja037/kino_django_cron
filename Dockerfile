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


RUN pip install -r requirements.txt

EXPOSE 443

CMD python manage.py runscript cron