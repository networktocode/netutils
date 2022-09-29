ARG PYTHON_VER

FROM python:${PYTHON_VER}-slim as base

RUN pip install --upgrade pip \
  && pip install poetry

WORKDIR /local
COPY . /local

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# -----------------------------------------------------------------------------
# Defines stage with napalm installed
# -----------------------------------------------------------------------------
FROM base as with_napalm
ARG NAPALM_PACKAGE=napalm
ARG NAPALM_VER=4.0.0
RUN pip install $NAPALM_PACKAGE==$NAPALM_VER