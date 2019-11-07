# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:alpine

WORKDIR /app
COPY . /app

EXPOSE 8000

ENV FLASK_APP=api.py

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
# Using pip:
RUN python3 -m pip install -r requirements.txt

CMD ["python", "api.py"]
