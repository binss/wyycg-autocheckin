FROM python:3-alpine

ENV CRON_SIGNIN='0 9 * * *' \
    TZ=Asia/Shanghai

WORKDIR /tmp
COPY requirements.txt ./
RUN adduser app -D              && \
    apk add --no-cache tzdata gettext   && \
    pip install --no-cache-dir -r requirements.txt  && \
    pip install --no-cache-dir crontab              && \
    rm -rf /tmp/*

WORKDIR /app
COPY main.py ./
COPY docker.py ./

USER app
CMD [ "python3", "-u", "./docker.py" ]

