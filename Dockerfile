FROM python:3.10-alpine

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]
