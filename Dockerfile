FROM python:3.12.2-alpine

LABEL maintainer="maksym.operchuk@gmail.com"

ENV PYTHOUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
