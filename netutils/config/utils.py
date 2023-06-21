"""Utility functions for working with device configurations."""


def _open_file_config(cfg_path: str) -> str:
    """Open config file from local disk."""
    # This might fail, raising an IOError
    with open(cfg_path, encoding="utf-8") as filehandler:
        device_cfg = filehandler.read()

    return device_cfg.strip()
