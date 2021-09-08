"""Utilities for the netutils library."""
from importlib import import_module
import inspect
import os
import glob


def _build_jinja2_function_mappings():
    """Creates a dictionary that maps function names to their objects for custom jinja2 filter usage."""
    function_mappings = {}

    cur_dir = os.path.dirname(os.path.abspath(__file__))

    root_full_file_list = [os.path.basename(file) for file in glob.glob(f"{cur_dir}/*.py")]
    config_full_file_list = [os.path.basename(file) for file in glob.glob(f"{cur_dir}/config/*.py")]

    root_file_list = [file[:-3] for file in root_full_file_list if file not in _EXCLUDED_FILES]
    config_file_list = [f"config.{file[:-3]}" for file in config_full_file_list if file not in _EXCLUDED_FILES]

    all_file_list = root_file_list + config_file_list
    for file in all_file_list:
        cur_module = import_module(f"netutils.{file}")
        module_functions = inspect.getmembers(cur_module, inspect.isfunction)
        for function_name, function_object in module_functions:
            if function_name.startswith("_"):
                continue
            function_mappings[function_name] = function_object
    return function_mappings

_EXCLUDED_FILES = ["__init__.py", "__pycache__", "constants.py", "lib_mapper.py", "protocol_mapper.py", "protocols.json", "config"]
_JINJA2_FUNCTION_MAPPINGS = _build_jinja2_function_mappings()

def jinja2_convenience_function(*args):
    """Convenience function that allows netutils filter to be used easily with jinja2.

    Returns:
        Any: Return value depends on the function called.

    """
    result = _JINJA2_FUNCTION_MAPPINGS
    return result