"""Test for deprecation warnings."""

import pytest

from netutils.config.parser import HPEConfigParser


def test_hpe_config_parser_deprecated():
    """Test that HPEConfigParser is deprecated and issues a warning."""
    expected_message = "HPEConfigParser is deprecated and will be removed in a future version. Use subclasses like HPComwareConfigParser instead."

    with pytest.warns(DeprecationWarning, match=expected_message):
        # Instantiating the class should trigger the deprecation warning
        HPEConfigParser("test config")
