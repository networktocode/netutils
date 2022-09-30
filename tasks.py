"""Tasks for use with Invoke."""
import os
import sys
from distutils.util import strtobool

from invoke import task

try:
    import toml
except ImportError:
    sys.exit("Please make sure to `pip install toml` or enable the Poetry shell and run `poetry install`.")


def is_truthy(arg):
    """Convert "truthy" strings into Booleans.

    Args:
        arg (str): Truthy string (True values are y, yes, t, true, on and 1; false values are n, no,
        f, false, off and 0. Raises ValueError if val is anything else.

    Examples:
        >>> is_truthy('yes')
        True
    """
    if isinstance(arg, bool):
        return arg
    return bool(strtobool(arg))


PYPROJECT_CONFIG = toml.load("pyproject.toml")
TOOL_CONFIG = PYPROJECT_CONFIG["tool"]["poetry"]

# Can be set to a separate Python version to be used for launching or building image
PYTHON_VER = os.getenv("PYTHON_VER", "3.9")
# Name of the docker image/image
IMAGE_NAME = os.getenv("IMAGE_NAME", TOOL_CONFIG["name"])
# Tag for the image
IMAGE_VER = os.getenv("IMAGE_VER", f"{TOOL_CONFIG['version']}-py{PYTHON_VER}")
# Gather current working directory for Docker commands
PWD = os.getcwd()
# Local or Docker execution provide "local" to run locally without docker execution
INVOKE_LOCAL = is_truthy(os.getenv("INVOKE_LOCAL", False))  # pylint: disable=W1508
# Get project name from the toml file
PROJECT_NAME = PYPROJECT_CONFIG["tool"]["poetry"]["name"]
# Get current project version from the toml file
PROJECT_VERSION = PYPROJECT_CONFIG["tool"]["poetry"]["version"]


def _get_image_name(with_optionals=False):
    """Gets the name of the container image to use.

    Args:
        with_optionals (bool): Get name of container image with optionals installed.

    Returns:
        str: Name of container image. Includes tag.
    """
    if with_optionals and not os.getenv("GITHUB_ACTION", None):
        name = f"{IMAGE_NAME}:{IMAGE_VER}-optionals"
    else:
        name = f"{IMAGE_NAME}:{IMAGE_VER}"

    return name


def run_cmd(context, exec_cmd, local=INVOKE_LOCAL, with_optionals=False):
    """Wrapper to run the invoke task commands.

    Args:
        context ([invoke.task]): Invoke task object.
        exec_cmd ([str]): Command to run.
        local (bool): Define as `True` to execute locally
        with_optionals (bool): Build a container with optionals installed

    Returns:
        result (obj): Contains Invoke result from running task.
    """
    name = _get_image_name(with_optionals)

    if is_truthy(local):
        print(f"LOCAL - Running command {exec_cmd}")
        result = context.run(exec_cmd, pty=True)
    else:
        print(f"DOCKER - Running command: {exec_cmd} container: {name}")
        result = context.run(f"docker run -it -v {PWD}:/local {name} sh -c '{exec_cmd}'", pty=True)

    return result


@task
def build(
    context, nocache=False, forcerm=False, hide=False, with_optionals=False
):  # pylint: disable=too-many-arguments
    """Build a Docker image.

    Args:
        context (obj): Used to run specific commands
        nocache (bool): Do not use cache when building the image
        forcerm (bool): Always remove intermediate containers
        hide (bool): Hide output of Docker image build
        with_optionals (bool): Build a container with optionals installed
    """
    name = _get_image_name(with_optionals)

    if with_optionals:
        command = f"docker build --tag {name} --target with_optionals"

    else:
        command = command = f"docker build --tag {name} --target base"

    command += f" --build-arg PYTHON_VER={PYTHON_VER} -f Dockerfile ."
    if nocache:
        command += " --no-cache"
    if forcerm:
        command += " --force-rm"

    result = context.run(command, hide=hide)
    if result.exited != 0:
        print(f"Failed to build image {IMAGE_NAME}:{IMAGE_VER}\nError: {result.stderr}")


@task
def clean(context, with_optionals=False):
    """Remove the project specific image.

    Args:
        context (obj): Used to run specific commands
        with_optionals (bool): Build a container with optionals installed
    """
    name = _get_image_name(with_optionals)

    print(f"Attempting to forcefully remove image {name}")
    context.run(f"docker rmi {name} --force")
    print(f"Successfully removed image {name}")


@task
def rebuild(context):
    """Clean the Docker image and then rebuild without using cache.

    Args:
        context (obj): Used to run specific commands
    """
    clean(context)
    build(context)


@task
def coverage(context, local=INVOKE_LOCAL):
    """Run the coverage report against pytest.

    Args:
        context (obj): Used to run specific commands
        local (bool): Define as `True` to execute locally
    """
    exec_cmd = "coverage run --source=netutils -m pytest"
    run_cmd(context, exec_cmd, local)
    run_cmd(context, "coverage report", local)
    run_cmd(context, "coverage html", local)


@task
def pytest(context, local=INVOKE_LOCAL):
    """Run pytest for the specified name and Python version.

    Args:
        context (obj): Used to run specific commands
        local (bool): Define as `True` to execute locally
    """
    exec_cmd = "pytest -vv --doctest-modules netutils/ && coverage run --source=netutils -m pytest --ignore='tests/unit/test_lib_helpers_no_optionals.py' && coverage report"
    run_cmd(context, exec_cmd, local, with_optionals=True)


@task
def pytest_without_optionals(context, local=INVOKE_LOCAL):
    """This will run pytest only to assert the correct errors are raised when pytest is not installed.

    This must be run inside of a container or environment in which optionals is not installed, otherwise the test case
    assertion will fail.

    Args:
        context (obj): Used to run specific commands
        local (bool): Define as `True` to execute locally
    """
    exec_cmd = 'find tests/ -name "test_lib_helpers_no_optionals.py" | xargs pytest -vv'
    run_cmd(context, exec_cmd, local)


@task
def black(context, local=INVOKE_LOCAL):
    """Run black to check that Python files adherence to black standards.

    Args:
        context (obj): Used to run specific commands
        local (bool): Define as `True` to execute locally
    """
    exec_cmd = "black --check --diff ."
    run_cmd(context, exec_cmd, local)


@task
def flake8(context, local=INVOKE_LOCAL):
    """Run flake8 for the specified name and Python version.

    Args:
        context (obj): Used to run specific commands
        local (bool): Define as `True` to execute locally
    """
    exec_cmd = "flake8 ."
    run_cmd(context, exec_cmd, local)


@task
def pylint(context, local=INVOKE_LOCAL):
    """Run pylint for the specified name and Python version.

    Args:
        context (obj): Used to run specific commands
        local (bool): Define as `True` to execute locally
    """
    exec_cmd = 'find . -name "*.py" | grep -v "tests/unit/mock" | xargs pylint'
    run_cmd(context, exec_cmd, local)


@task
def yamllint(context, local=INVOKE_LOCAL):
    """Run yamllint to validate formatting adheres to NTC defined YAML standards.

    Args:
        context (obj): Used to run specific commands
        local (bool): Define as `True` to execute locally
    """
    exec_cmd = "yamllint ."
    run_cmd(context, exec_cmd, local)


@task
def pydocstyle(context, local=INVOKE_LOCAL):
    """Run pydocstyle to validate docstring formatting adheres to NTC defined standards.

    Args:
        context (obj): Used to run specific commands
        local (bool): Define as `True` to execute locally
    """
    exec_cmd = "pydocstyle ."
    run_cmd(context, exec_cmd, local)


@task
def bandit(context, local=INVOKE_LOCAL):
    """Run bandit to validate basic static code security analysis.

    Args:
        context (obj): Used to run specific commands
        local (bool): Define as `True` to execute locally
    """
    exec_cmd = "bandit --recursive ./ --configfile .bandit.yml"
    run_cmd(context, exec_cmd, local)


@task
def mypy(context, local=INVOKE_LOCAL):
    """Run mypy to validate typing-hints.

    Args:
        context (obj): Used to run specific commands
        local (bool): Define as `True` to execute locally
    """
    exec_cmd = "mypy ./netutils"
    run_cmd(context, exec_cmd, local)


@task
def cli(context):
    """Enter the image to perform troubleshooting or dev work.

    Args:
        context (obj): Used to run specific commands
    """
    dev = f"docker run -it -v {PWD}:/local {IMAGE_NAME}:{IMAGE_VER} /bin/bash"
    context.run(f"{dev}", pty=True)


@task
def tests(context, local=INVOKE_LOCAL):
    """Run all tests for the specified name and Python version.

    Args:
        context (obj): Used to run specific commands
        local (bool): Define as `True` to execute locally
    """
    black(context, local)
    flake8(context, local)
    pylint(context, local)
    yamllint(context, local)
    pydocstyle(context, local)
    bandit(context, local)
    mypy(context, local)
    pytest(context, local)
    pytest_without_optionals(context, local)

    print("All tests have passed!")


@task
def html(context, sourcedir="docs/source", builddir="docs/build"):
    """Creates html docs using sphinx-build command.

    Args:
        context (obj): Used to run specific commands
        sourcedir (str, optional): Source directory for sphinx to use. Defaults to "source".
        builddir (str, optional): Output directory for sphinx to use. Defaults to "build".
    """
    print("Building html documentation...")
    clean_docs(context, builddir)
    command = f"sphinx-build {sourcedir} {builddir}"
    context.run(command)


@task
def clean_docs(context, builddir="docs/build"):
    """Removes the build directory and all of its contents.

    Args:
        context (obj): Used to run specific commands
        builddir (str, optional): Directory to be removed. Defaults to "build".
    """
    print(f"Removing everything under {builddir} directory...")
    context.run("rm -rf " + builddir)
