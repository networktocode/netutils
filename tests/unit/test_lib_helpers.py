"""Test for the lib_helpers definitions."""

from unittest import mock

import pytest
from netutils.lib_helpers import get_napalm_getters


@mock.patch("netutils.lib_helpers.HAS_NAPALM", False)
def test_get_napalm_getters_napalm_not_installed():
    with pytest.raises(ImportError) as exc:
        get_napalm_getters()
    assert "Napalm must be install for this function to operate." == str(exc.value)


@mock.patch("netutils.lib_helpers.get_network_driver", mock.Mock())
def test_get_napalm_getters_napalm_installed_default():
    napalm_getters = get_napalm_getters()
    assert napalm_getters == {
        "asa": {},
        "cisco_wlc_ssh": {},
        "eos": {},
        "fortios": {},
        "huawei": {},
        "ios": {},
        "iosxr": {},
        "junos": {},
        "nxos": {},
        "nxos_ssh": {},
        "panos": {},
        "sros": {},
        "vyos": {},
    }


@mock.patch("netutils.lib_helpers.get_network_driver", mock.Mock())
@mock.patch(
    "netutils.lib_helpers.inspect.getmembers",
    mock.Mock(return_value=[("get_foo", mock.Mock()), ("not_get", mock.Mock())]),
)
def test_get_napalm_getters_napalm_only_getters():
    napalm_getters = get_napalm_getters()
    assert list(napalm_getters.values())[0] == {"get_foo": False}
