FROM python:3.8

COPY . /app
WORKDIR /app


##############################################
RUN apt-get update 
RUN apt-get install build-essential gcc g++ musl-dev unixodbc-dev -y
RUN apt-get install libc-dev libxslt-dev libxml2-dev libffi-dev -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
##############################################


EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD [ "src/main.py" ]