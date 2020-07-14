FROM python:3.7.7-slim

# We copy just the requirements.txt first to leverage cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN python3 -m pip install -r requirements.txt

COPY . /app

EXPOSE 3001/udp

ENTRYPOINT ["python3", "-u", "app.py"]
