"""Test for deprecation warnings."""

import pytest

from netutils.config.parser import HPComwareConfigParser


def test_hp_comware_config_parser_deprecated():
    """Test that HPComwareConfigParser is deprecated and issues a warning."""
    expected_message = (
        "HPComwareConfigParser is deprecated and will be removed in a future version. Use HPEConfigParser instead."
    )

    with pytest.warns(DeprecationWarning, match=expected_message):
        # Instantiating the class should trigger the deprecation warning
        HPComwareConfigParser("test config")
