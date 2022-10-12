"""Update docs tests to include assurance that development script ran."""
import sys

sys.path.append("...")
from development_scripts import main  # noqa:E402 pylint: disable=wrong-import-position


def test_docs_generated():
    """Assert each generated file has been auto generated, run `python development_scripts.py` if failed."""
    assert main(test=True) is True
