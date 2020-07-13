FROM python:3.7-alpine

RUN apk update && apk add bash make automake gcc g++ subversion python3-dev

# We copy just the requirements.txt first to leverage cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN python3 -m pip install -r requirements.txt

COPY . /app

EXPOSE 3001

CMD ["python3", "src/app.py"]
