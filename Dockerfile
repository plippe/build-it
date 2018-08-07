FROM python:2.7

RUN pip install scrapy

COPY . /opt/repository
WORKDIR /opt/repository

ENTRYPOINT make run
