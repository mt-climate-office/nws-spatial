FROM python:3.11-slim

RUN apt update &&  \
    apt install -y cron && \
    apt install -y curl 

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml poetry.lock* main.py /app/
COPY ./nws_spatial/ /app/nws_spatial
RUN poetry install --only main

RUN chmod a+x /app/main.py
RUN touch /app/test.log

RUN (crontab -l; echo '*/5 * * * * cd /app && /usr/local/bin/python ./main.py zones alerts templates') | crontab


CMD cron && tail -f /dev/null