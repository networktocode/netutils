"""Test for the library utilities."""
from importlib import import_module
from inspect import getmembers, isfunction
from glob import glob
import os
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
    "utils",
]

_EXCLUDED_DECORATOR_FUNCTIONS = ["wraps", "total_ordering", "abstractmethod"]


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
            if function_name.startswith("_") or function_name.startswith(tuple(_EXCLUDED_DECORATOR_FUNCTIONS)):
                continue
            function_names.append(f"{function_name}")
    return function_names


def _recursive_dict_expand(nested_dict):
    result = []
    for _, function_path in nested_dict.items():
        if isinstance(function_path, dict):
            nested_items = _recursive_dict_expand(function_path)
            for item in nested_items:
                result.append(item)
        else:
            result.append(function_path)
    return result


def test_jinja2_mapping_contains_all_functions(get_jinja2_function_names):  # pylint: disable=redefined-outer-name
    function_paths = _recursive_dict_expand(_JINJA2_FUNCTION_MAPPINGS)
    function_names = [x.split(".")[1] for x in function_paths]

    assert set(get_jinja2_function_names) == set(function_names)


def test_jinja2_mapping_missing_function(get_jinja2_function_names):  # pylint: disable=redefined-outer-name
    function_paths = _recursive_dict_expand(_JINJA2_FUNCTION_MAPPINGS)
    function_names = [x.split(".")[1] for x in function_paths]
    function_names.append("MyExtraFunction")

    with pytest.raises(AssertionError):
        assert set(get_jinja2_function_names) == set(function_names)


def test_jinja2_template():
    env = Environment(loader=FileSystemLoader("tests/unit/jinja2_template"), autoescape=select_autoescape())

    for function_name, function_object in jinja2_convenience_function().items():
        env.filters[function_name] = function_object

    template = env.get_template("test.j2")
    result = template.render()
    assert result == "192.168.0.0 + 200 = 192.168.0.200"
