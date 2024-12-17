FROM python:3

WORKDIR /parser-app

COPY requirements.txt /parser-app
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update
RUN apt-get install -y firefox-esr wget
RUN apt-get clean


# Download the latest stable geckodriver dynamically
RUN ARCH=$(uname -m) && \
    LATEST_URL=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | \
                 grep "browser_download_url.*linux" | grep "$ARCH" | cut -d '"' -f 4) && \
    curl -L $LATEST_URL -o /tmp/geckodriver.tar.gz && \
    tar -xvzf /tmp/geckodriver.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver

RUN geckodriver --version


CMD [ "python", "./main.py" ]
