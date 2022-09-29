"""Test for the lib_helpers definitions."""

from unittest import mock

from netutils.lib_helpers import get_napalm_getters


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
