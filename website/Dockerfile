FROM python:3

WORKDIR /website-app

COPY . /website-app
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get clean
CMD [ "python", "./main.py" ]
