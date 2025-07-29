"""Tasks for use with Invoke."""

from invoke import Collection, Exit
from invoke import task as invoke_task


def is_truthy(arg):
    """Convert "truthy" strings into Booleans.

    Examples
    --------
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
# Variables may be overwritten in invoke.yml or by the environment variables INVOKE_PYNTC_xxx
namespace = Collection("netutils")
namespace.configure(
    {
        "netutils": {
            "project_name": "netutils",
            "python_ver": "3.13",
            "local": False,
            "image_name": "netutils",
            "image_ver": "latest",
            "pwd": ".",
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


def run_command(context, exec_cmd, port=None):
    """Wrapper to run the invoke task commands.

    Args:
        context ([invoke.task]): Invoke task object.
        exec_cmd ([str]): Command to run.
        port (int): Used to serve local docs.

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
                f"docker run -it -p {port} -v {context.netutils.pwd}:/local {context.netutils.image_name}:{context.netutils.image_ver} sh -c '{exec_cmd}'",
                pty=True,
            )
        else:
            result = context.run(
                f"docker run -it -v {context.netutils.pwd}:/local {context.netutils.image_name}:{context.netutils.image_ver} sh -c '{exec_cmd}'",
                pty=True,
            )

    return result


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
    """Run the coverage report against pytest.

    Args:
        context (obj): Used to run specific commands
    """
    exec_cmd = "coverage run --source=netutils -m pytest"
    run_command(context, exec_cmd)
    run_command(context, "coverage report")
    run_command(context, "coverage html")


@task
def pytest(context):
    """Run pytest for the specified name and Python version.

    Args:
        context (obj): Used to run specific commands
    """
    exec_cmd = "pytest -vv --doctest-modules netutils/ && coverage run --source=netutils -m pytest && coverage report"
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
        local (bool): Define as `True` to execute locally
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


@task
def tests(context):
    """Run all tests for the specified name and Python version.

    Args:
        context (obj): Used to run specific commands
    """
    ruff(context)
    pylint(context)
    yamllint(context)
    mypy(context)
    pytest(context)

    print("All tests have passed!")


@task
def docs(context):
    """Build and serve docs locally for development."""
    exec_cmd = "mkdocs serve -v --dev-addr=0.0.0.0:8001"
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
