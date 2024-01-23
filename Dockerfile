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

RUN poetry install --only main
RUN chmod a+x ./main.py
RUN chmod a+x /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]