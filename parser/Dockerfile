FROM python:3


RUN apt-get update
RUN apt-get install -y firefox-esr wget
RUN apt-get clean

# Download the latest stable geckodriver dynamically
RUN ARCH=$(uname -m) && \
    if [ "$ARCH" = "x86_64" ]; then \
        wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz -O /tmp/geckodriver.tar.gz; \
    elif [ "$ARCH" = "aarch64" ]; then \
        wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux-aarch64.tar.gz -O /tmp/geckodriver.tar.gz; \
    else \
        echo "Unsupported architecture: $ARCH" && exit 1; \
    fi && \
    tar -xvzf /tmp/geckodriver.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver

RUN geckodriver --version

WORKDIR /parser-app
COPY requirements.txt /parser-app
RUN pip install --no-cache-dir -r requirements.txt

# COPY . /parser-app

CMD [ "python", "./main.py" ]
