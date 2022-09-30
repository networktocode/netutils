ARG PYTHON_VER

FROM python:${PYTHON_VER}-slim as base

RUN pip install --upgrade pip \
  && pip install poetry

WORKDIR /local
COPY . /local

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# -----------------------------------------------------------------------------
# Defines stage with optionals installed
# -----------------------------------------------------------------------------
FROM base as with_optionals

RUN pip install --upgrade pip \
  && pip install poetry

WORKDIR /local
COPY . /local

RUN poetry config virtualenvs.create false \
  && poetry install -E optionals --no-interaction --no-ansi