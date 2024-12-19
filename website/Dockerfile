FROM python:3


RUN apt-get update
RUN apt-get install -y wget
RUN apt-get clean

WORKDIR /website-app

COPY . /website-app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]
