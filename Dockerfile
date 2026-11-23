FROM python:3.12.15-alpine3.23

WORKDIR /app

COPY . .


RUN pip install -r req.txt