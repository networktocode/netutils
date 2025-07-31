"""Used to setup fixtures to be used through tests"""

import importlib.util
import json
import os

import pytest


@pytest.fixture
def get_json_data():
    """Fixture to return the json data as a Python variable."""

    def _method(_file):
        """Fixture to return the json data as a Python variable, given a file location

        Args:
            _file (str): The location of the json file to input data from.

        Returns:
            dict: The data structure from the JSON file.
        """
        with open(_file, encoding="utf-8") as file:
            data = json.load(file)
        return data

    return _method


@pytest.fixture
def get_text_data():
    """Fixture to return the text data as a string."""

    def _method(_file):
        """Fixture to return the text data as a string, given a file location

        Args:
            _file (str): The location of the text file to input data from.

        Returns:
            str: The data structure from the text file.
        """
        with open(_file, encoding="utf-8") as file:
            data = file.read()
        return data

    return _method


@pytest.fixture
def get_python_data():
    """Fixture to return the Python data as a variable."""

    def _method(_file, attr):
        """Fixture to return the Python data as a variable, given a file location.

        Args:
            _file (str): The location of the Python file to input data from.
            attr (str): The variable to obtain from the Python file.

        Returns:
            str: The data structure from the Python file.
        """
        name = os.path.splitext(os.path.basename(_file))[0]
        spec = importlib.util.spec_from_file_location(name, _file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return getattr(module, attr)

    return _method
