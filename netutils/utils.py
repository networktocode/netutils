"""Utilities for the netutils library."""
from importlib import import_module


def jinja2_convenience_function(*args):
    """Convenience function that allows netutils filter to be used easily with jinja2.

    Returns:
        Any: Return value depends on the function called.

    """
    # TODO: Add docstring example.
    args_list = list(args)
    function = args_list.pop(1)
    module_name, function_name = function.split(".")

    instantiated_module = import_module(f"netutils.{module_name}")
    module_function = getattr(instantiated_module, function_name)
    result = module_function(*args_list)
    return result
