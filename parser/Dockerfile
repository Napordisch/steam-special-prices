FROM python:3

WORKDIR /parser-app

COPY requirements.txt /parser-app
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update
RUN apt-get install -y firefox-esr wget
RUN apt-get clean


CMD [ "python", "./main.py" ]
