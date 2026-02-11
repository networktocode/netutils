"""Tasks for use with Invoke."""

import os
import re
from pathlib import Path

from invoke import Collection, Exit
from invoke import task as invoke_task


def is_truthy(arg):
    """Convert "truthy" strings into Booleans.

    Examples:
        >>> is_truthy('yes')
        True
    Args:
        arg (str): Truthy string (True values are y, yes, t, true, on and 1; false values are n, no,
        f, false, off and 0. Raises ValueError if val is anything else.
    """
    if isinstance(arg, bool):
        return arg

    val = str(arg).lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return True
    if val in ("n", "no", "f", "false", "off", "0"):
        return False
    raise ValueError(f"Invalid truthy value: `{arg}`")


# Use pyinvoke configuration for default values, see http://docs.pyinvoke.org/en/stable/concepts/configuration.html
# Variables may be overwritten in invoke.yml or by the environment variables INVOKE_NETUTILS_xxx
namespace = Collection("netutils")
namespace.configure(
    {
        "netutils": {
            "project_name": "netutils",
            "python_ver": "3.10",
            "local": is_truthy(os.getenv("INVOKE_NETUTILS_LOCAL", "false")),
            "image_name": "netutils",
            "image_ver": os.getenv("INVOKE_PARSER_IMAGE_VER", "latest"),
            "pwd": Path(__file__).parent,
        }
    }
)


# pylint: disable=keyword-arg-before-vararg
def task(function=None, *args, **kwargs):
    """Task decorator to override the default Invoke task decorator and add each task to the invoke namespace."""

    def task_wrapper(function=None):
        """Wrapper around invoke.task to add the task to the namespace as well."""
        if args or kwargs:
            task_func = invoke_task(*args, **kwargs)(function)
        else:
            task_func = invoke_task(function)
        namespace.add_task(task_func)
        return task_func

    if function:
        # The decorator was called with no arguments
        return task_wrapper(function)
    # The decorator was called with arguments
    return task_wrapper


def run_command(context, exec_cmd, port=None, rm=True):
    """Wrapper to run the invoke task commands.

    Args:
        context ([invoke.task]): Invoke task object.
        exec_cmd ([str]): Command to run.
        port (int): Used to serve local docs.
        rm (bool): Whether to remove the container after running the command.

    Returns:
        result (obj): Contains Invoke result from running task.
    """
    if is_truthy(context.netutils.local):
        print(f"LOCAL - Running command {exec_cmd}")
        result = context.run(exec_cmd, pty=True)
    else:
        print(
            f"DOCKER - Running command: {exec_cmd} container: {context.netutils.image_name}:{context.netutils.image_ver}"
        )
        if port:
            result = context.run(
                f"docker run -it {'--rm' if rm else ''} -p {port} -v {context.netutils.pwd}:/local {context.netutils.image_name}:{context.netutils.image_ver} sh -c '{exec_cmd}'",
                pty=True,
            )
        else:
            result = context.run(
                f"docker run -it {'--rm' if rm else ''} -v {context.netutils.pwd}:/local {context.netutils.image_name}:{context.netutils.image_ver} sh -c '{exec_cmd}'",
                pty=True,
            )

    return result


# ------------------------------------------------------------------------------
# BUILD
# ------------------------------------------------------------------------------
@task(
    help={
        "cache": "Whether to use Docker's cache when building images (default enabled)",
        "force_rm": "Always remove intermediate images",
        "hide": "Suppress output from Docker",
    }
)
def build(context, cache=True, force_rm=False, hide=False):
    """Build a Docker image."""
    print(f"Building image {context.netutils.image_name}:{context.netutils.image_ver}")
    command = f"docker build --tag {context.netutils.image_name}:{context.netutils.image_ver} --build-arg PYTHON_VER={context.netutils.python_ver} -f Dockerfile ."

    if not cache:
        command += " --no-cache"
    if force_rm:
        command += " --force-rm"

    result = context.run(command, hide=hide)
    if result.exited != 0:
        print(
            f"Failed to build image {context.netutils.image_name}:{context.netutils.image_ver}\nError: {result.stderr}"
        )


@task
def generate_packages(context):
    """Generate all Python packages inside docker and copy the file locally under dist/."""
    command = "poetry build"
    run_command(context, command)


@task(
    help={
        "check": (
            "If enabled, check for outdated dependencies in the poetry.lock file, "
            "instead of generating a new one. (default: disabled)"
        )
    }
)
def lock(context, check=False):
    """Generate poetry.lock inside the library container."""
    run_command(context, f"poetry {'check' if check else 'lock --no-update'}")


@task
def clean(context):
    """Remove the project specific image."""
    print(f"Attempting to forcefully remove image {context.netutils.image_name}:{context.netutils.image_ver}")
    context.run(f"docker rmi {context.netutils.image_name}:{context.netutils.image_ver} --force")
    print(f"Successfully removed image {context.netutils.image_name}:{context.netutils.image_ver}")


@task
def rebuild(context):
    """Clean the Docker image and then rebuild without using cache."""
    clean(context)
    build(context, cache=False)


@task
def coverage(context):
    """Run the coverage report against pytest."""
    exec_cmd = "coverage run --source=netutils -m pytest"
    run_command(context, exec_cmd)
    run_command(context, "coverage report")
    run_command(context, "coverage html")


@task(
    help={
        "pattern": "Only run tests which match the given substring. Can be used multiple times.",
        "label": "Module path to run (e.g., tests/unit/test_foo.py). Can be used multiple times.",
    },
    iterable=["pattern", "label"],
)
def pytest(context, pattern=None, label=None):
    """Run pytest test cases."""
    doc_test_cmd = "pytest -vv --doctest-modules netutils/"
    pytest_cmd = "coverage run --source=netutils -m pytest"
    if pattern:
        pytest_cmd += "".join([f" -k {_pattern}" for _pattern in pattern])
    if label:
        pytest_cmd += "".join([f" {_label}" for _label in label])
    coverage_cmd = "coverage report"
    exec_cmd = " && ".join([doc_test_cmd, pytest_cmd, coverage_cmd])
    run_command(context, exec_cmd)


@task(aliases=("a",))
def autoformat(context):
    """Run code autoformatting."""
    ruff(context, action=["format"], fix=True)


@task(
    help={
        "action": "Available values are `['lint', 'format']`. Can be used multiple times. (default: `['lint', 'format']`)",
        "target": "File or directory to inspect, repeatable (default: all files in the project will be inspected)",
        "fix": "Automatically fix selected actions. May not be able to fix all issues found. (default: False)",
        "output_format": "See https://docs.astral.sh/ruff/settings/#output-format for details. (default: `concise`)",
    },
    iterable=["action", "target"],
)
def ruff(context, action=None, target=None, fix=False, output_format="concise"):
    """Run ruff to perform code formatting and/or linting."""
    if not action:
        action = ["lint", "format"]
    if not target:
        target = ["."]

    exit_code = 0

    if "format" in action:
        command = "ruff format "
        if not fix:
            command += "--check "
        command += " ".join(target)
        if not run_command(context, command):
            exit_code = 1

    if "lint" in action:
        command = "ruff check "
        if fix:
            command += "--fix "
        command += f"--output-format {output_format} "
        command += " ".join(target)
        if not run_command(context, command):
            exit_code = 1

    if exit_code != 0:
        raise Exit(code=exit_code)


@task
def mypy(context):
    """Run mypy to validate typing-hints.

    Args:
        context (obj): Used to run specific commands
        local (bool): Define as `True` to execute locally
    """
    exec_cmd = "mypy ./netutils"
    run_command(context, exec_cmd)


@task
def pylint(context):
    """Run pylint for the specified name and Python version.

    Args:
        context (obj): Used to run specific commands
        local (bool): Define as `True` to execute locally
    """
    exec_cmd = 'find . -name "*.py" | grep -vE "(tests/unit/mock|netutils/data_files)" | xargs pylint'
    run_command(context, exec_cmd)


@task
def yamllint(context):
    """Run yamllint to validate formatting adheres to NTC defined YAML standards.

    Args:
        context (obj): Used to run specific commands
    """
    exec_cmd = "yamllint ."
    run_command(context, exec_cmd)


@task
def cli(context):
    """Enter the image to perform troubleshooting or dev work.

    Args:
        context (obj): Used to run specific commands
    """
    dev = f"docker run -it -v {context.netutils.pwd}:/local {context.netutils.image_name}:{context.netutils.image_ver} /bin/bash"
    context.run(f"{dev}", pty=True)


@task(
    help={
        "lint-only": "Only run linters; unit tests will be excluded. (default: False)",
    }
)
def tests(context, lint_only=False):
    """Run all tests for the specified name and Python version.

    Args:
        context (obj): Used to run specific commands
        lint_only (bool): If True, only run linters and skip unit tests.
    """
    # If we are not running locally, start the docker containers so we don't have to for each test
    # Sorted loosely from fastest to slowest
    print("Running ruff...")
    ruff(context)
    print("Running yamllint...")
    yamllint(context)
    print("Running mypy...")
    mypy(context)
    print("Running poetry check...")
    lock(context, check=True)
    print("Running pylint...")
    pylint(context)
    print("Running mkdocs...")
    build_and_check_docs(context)
    if not lint_only:
        print("Running unit tests...")
        pytest(context)
    print("All tests have passed!")


@task
def build_and_check_docs(context):
    """Build documentation and test the configuration."""
    command = "mkdocs build --no-directory-urls --strict"
    run_command(context, command)

    # Check for the existence of a release notes file for the current version if it's not a prerelease.
    version = context.run("poetry version --short", hide=True)
    match = re.match(r"^(\d+)\.(\d+)\.\d+$", version.stdout.strip())
    if match:
        major = match.group(1)
        minor = match.group(2)
        release_notes_file = Path(__file__).parent / "docs" / "admin" / "release_notes" / f"version_{major}.{minor}.md"
        if not release_notes_file.exists():
            print(f"Release notes file `version_{major}.{minor}.md` does not exist.")
            raise Exit(code=1)


@task
def docs(context):
    """Build and serve docs locally for development."""
    exec_cmd = "mkdocs serve -v"
    run_command(context, exec_cmd, port="8001:8001")


@task(
    help={
        "version": "Version of netutils to generate the release notes for.",
    }
)
def generate_release_notes(context, version=""):
    """Generate Release Notes using Towncrier."""
    command = "poetry run towncrier build"
    if version:
        command += f" --version {version}"
    else:
        command += " --version `poetry version -s`"
    # Due to issues with git repo ownership in the containers, this must always run locally.
    context.run(command)
