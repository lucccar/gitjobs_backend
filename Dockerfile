FROM python:3.8-slim

COPY . /app
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:${PWD}/app/src:${PYTHONPATH}/app/src/searchdao:${PYTHONPATH}/app/src/model:${PYTHONPATH}/app/src/external:${PYTHONPATH}/app/src/database"

##############################################
RUN apt-get update 
RUN apt-get install build-essential gcc g++ musl-dev unixodbc-dev -y
RUN apt-get install libc-dev libxslt-dev libxml2-dev libffi-dev -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
##############################################


EXPOSE 5000

CMD ["gunicorn", "-w", "2", "--bind", "0.0.0.0:5000", "src.main:app"]