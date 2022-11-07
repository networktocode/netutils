"""Initialization file for library."""

try:
    from importlib import metadata  # type: ignore[attr-defined]
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata  # type: ignore[no-redef]

__version__ = metadata.version(__name__)
