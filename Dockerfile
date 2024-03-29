FROM python:3.11
MAINTAINER Lars van Rhijn

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE djangfolio.settings.production
ENV PATH /root/.poetry/bin:${PATH}

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

WORKDIR /djangfolio/src
COPY resources/entrypoint.sh /usr/local/bin/entrypoint.sh
COPY poetry.lock pyproject.toml /djangfolio/src/

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install --yes --quiet --no-install-recommends postgresql-client && \
    rm --recursive --force /var/lib/apt/lists/* && \
    \
    mkdir --parents /djangfolio/src/ && \
    mkdir --parents /djangfolio/log/ && \
    mkdir --parents /djangfolio/static/ && \
    chmod +x /usr/local/bin/entrypoint.sh && \
    \
    curl -sSL https://install.python-poetry.org | python3 - && \
    export PATH="/root/.local/bin:$PATH" && \
    poetry config --no-interaction --no-ansi virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-dev


COPY website /djangfolio/src/website/