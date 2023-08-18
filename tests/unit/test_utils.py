"""Test for the library utilities."""
import os
from glob import glob
from importlib import import_module
from inspect import getmembers, isfunction

import pytest
from jinja2 import Environment, select_autoescape
from jinja2.loaders import FileSystemLoader
from netutils.utils import _JINJA2_FUNCTION_MAPPINGS, jinja2_convenience_function

_EXCLUDED_FILES = [
    "__init__",
    "config/__init__",
    "config/parser",
    "__pycache__",
    "constants",
    "lib_mapper",
    "protocol_mapper",
    "protocols.json",
    "config",
]

_EXCLUDED_DECORATOR_FUNCTIONS = ["wraps", "total_ordering", "abstractmethod"]

_EXCLUDED_FUNCTIONS = ["jinja2_convenience_function", "import_module", "get_network_driver"]


@pytest.fixture
def get_jinja2_function_names():
    """Gets functions dynamically from python files.

    Returns:
        list: List of function names form python files.
    """
    function_names = []
    python_files = [y[9:-3] for x in os.walk("netutils/") for y in glob(os.path.join(x[0], "*.py"))]
    filtered_python_files = [file.replace("/", ".") for file in python_files if file not in _EXCLUDED_FILES]

    for file in filtered_python_files:
        imported_module = import_module(f"netutils.{file}")
        for function_name, _ in getmembers(imported_module, isfunction):
            if (
                function_name.startswith("_")
                or function_name.startswith(tuple(_EXCLUDED_DECORATOR_FUNCTIONS))
                or function_name.startswith(tuple(_EXCLUDED_FUNCTIONS))
            ):
                continue
            function_names.append(f"{function_name}")
    return function_names


def test_jinja2_mapping_contains_all_functions(get_jinja2_function_names):  # pylint: disable=redefined-outer-name
    mapping_function_names = [path.split(".")[-1] for path in list(_JINJA2_FUNCTION_MAPPINGS.values())]
    sorted_get_jinja2_function_names = sorted(list(set(get_jinja2_function_names)))
    sorted_mapping_function_names = sorted(mapping_function_names)

    assert sorted_get_jinja2_function_names == sorted_mapping_function_names


def test_jinja2_mapping_missing_function(get_jinja2_function_names):  # pylint: disable=redefined-outer-name
    mapping_function_names = [path.split(".")[-1] for path in list(_JINJA2_FUNCTION_MAPPINGS.values())]
    mapping_function_names.append("MyExtraFunction")

    sorted_mapping_function_names = sorted(mapping_function_names)
    sorted_get_jinja2_function_names = sorted(get_jinja2_function_names)

    with pytest.raises(AssertionError):
        assert sorted_get_jinja2_function_names == sorted_mapping_function_names


def test_jinja2_template():
    env = Environment(loader=FileSystemLoader("tests/unit/jinja2_template"), autoescape=select_autoescape())

    env.filters.update(jinja2_convenience_function())

    template = env.get_template("test.j2")
    result = template.render()
    assert result == "192.168.0.0 + 200 = 192.168.0.200"
