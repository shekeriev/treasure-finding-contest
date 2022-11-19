FROM python:3.9-slim-buster

COPY code/* /app/

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD [ "python3", "-u", "/app/app.py"]
