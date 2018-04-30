FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /ratings-ms
WORKDIR /ratings-ms

ADD requirements.txt /ratings-ms

RUN pip install -r requirements.txt

ADD . /ratings-ms

EXPOSE 6003
