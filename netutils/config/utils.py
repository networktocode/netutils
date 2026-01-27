"""Utility functions for working with device configurations."""

import typing as t
import warnings
from functools import wraps


def _open_file_config(cfg_path: str) -> str:
    """Open config file from local disk."""
    # This might fail, raising an IOError
    with open(cfg_path, encoding="utf-8") as filehandler:
        device_cfg = filehandler.read()

    return device_cfg.strip()


def _deprecated(custom_message: t.Optional[str] = None) -> t.Callable[[t.Any], t.Any]:
    """Deprecate a function or class.

    Args:
        custom_message: Custom deprecation message. If None, uses default message.

    Returns:
        Decorator function that issues a deprecation warning when the decorated item is used.
    """
    if custom_message is None:
        custom_message = "This function or class is deprecated and will be removed in a future version."

    def decorator(obj: t.Any) -> t.Any:
        """Decorator that wraps a class or function to issue deprecation warning."""
        if isinstance(obj, type):
            # For classes, wrap __init__ to issue warning on instantiation
            original_init = getattr(obj, "__init__", None)
            if original_init is None:
                return obj

            def __init__(self: t.Any, *args: t.Any, **kwargs: t.Any) -> None:
                warnings.warn(custom_message, DeprecationWarning, stacklevel=2)
                original_init(self, *args, **kwargs)

            setattr(obj, "__init__", __init__)
            return obj

        # For functions, wrap the function
        @wraps(obj)
        def wrapper(*args: t.Any, **kwargs: t.Any) -> t.Any:
            warnings.warn(custom_message, DeprecationWarning, stacklevel=2)
            return obj(*args, **kwargs)

        return wrapper

    return decorator
