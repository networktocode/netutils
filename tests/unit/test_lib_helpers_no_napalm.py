"""Test for the lib_helpers definitions failures when napalm not installed."""

import pytest
from netutils.lib_helpers import get_napalm_getters


def test_get_napalm_getters_napalm_not_installed():
    with pytest.raises(ImportError) as exc:
        get_napalm_getters()
    assert "Napalm must be install for this function to operate." == str(exc.value)
