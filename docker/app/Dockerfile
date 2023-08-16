FROM tiangolo/uvicorn-gunicorn:python3.11 as image

ENV PYTHONPATH "${PYTHONPATH}:/"
ENV PORT=8000

FROM image as build-stage

ARG POETRY_VERSION=1.5.2
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  ENV=dev

RUN apt-get update && apt-get upgrade -y
RUN apt-get install --no-install-recommends -y curl gcc musl-dev libffi-dev
RUN pip3 install --no-cache-dir poetry=="$POETRY_VERSION"
RUN apt-get clean && rm -rf /var/lib/apt/lists/*



FROM build-stage as requirements
ARG APP_HOME=/app
WORKDIR ${APP_HOME}

COPY poetry.lock pyproject.toml ${APP_HOME}/
RUN poetry install --no-root $(test "$ENV" == prod && echo "--no-dev")

COPY . /app
COPY ./docker/app/entrypoint.sh /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod u+x /entrypoint

COPY ./docker/app/start.sh /start
RUN sed -i 's/\r$//g' /start
RUN chmod u+x /start


ENTRYPOINT ["/entrypoint"]
