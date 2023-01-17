FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && apt-get -y install git

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
ADD ./src /code

RUN pip install --upgrade pip && pip install -r requirements.txt
