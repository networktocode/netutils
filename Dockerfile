<<<<<<< HEAD
ARG PYTHON_VER="3.9"
=======
ARG PYTHON_VER="3.10"
>>>>>>> 725e2d2 (Cookie updated by NetworkToCode Cookie Drift Manager Tool)

FROM python:${PYTHON_VER}-slim

# Install Poetry manually via its installer script;
# if we instead used "pip install poetry" it would install its own dependencies globally which may conflict with ours.
# https://python-poetry.org/docs/master/#installing-with-the-official-installer
# This also makes it so that Poetry will *not* be included in the "final" image since it's not installed to /usr/local/
ARG POETRY_HOME=/opt/poetry
ARG POETRY_INSTALLER_PARALLEL=true
ARG POETRY_VERSION=2.1.3
ARG POETRY_VIRTUALENVS_CREATE=false
ADD https://install.python-poetry.org /tmp/install-poetry.py
RUN python /tmp/install-poetry.py

# Add poetry install location to the $PATH
ENV PATH="${POETRY_HOME}/bin:${PATH}"

RUN poetry config virtualenvs.create ${POETRY_VIRTUALENVS_CREATE} && \
    poetry config installer.parallel "${POETRY_INSTALLER_PARALLEL}"

WORKDIR /local
COPY . /local

# Install the app
RUN poetry install --with dev --all-extras
