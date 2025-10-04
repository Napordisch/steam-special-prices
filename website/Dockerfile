FROM python:3


RUN apt-get update
RUN apt-get install -y wget
RUN apt-get clean

WORKDIR /website-app
COPY requirements.txt /website-app
RUN pip install --no-cache-dir -r requirements.txt

# COPY . /website-app


CMD [ "python", "./main.py" ]
