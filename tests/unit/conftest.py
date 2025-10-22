"""Used to setup fixtures to be used through tests"""

import pytest
from click.testing import CliRunner


@pytest.fixture
def cli_runner():
    """Provide CLI runner for Click tests."""
    return CliRunner()
