FROM python:3.8.0-alpine

ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app/underlordsAPI/

WORKDIR /usr/src/app/underlordsAPI/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5050