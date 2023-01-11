FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
ADD ./src /code

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
