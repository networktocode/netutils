"""Test functions for NIST URL Utility"""

import pytest

from netutils.nist import os_platform_object_builder

platform_data = [
    # Cisco and Arista use the generic parsing
    {
        "sent": {"vendor": "cisco", "platform": "ios", "version": "15.7(2.0z)M"},
        "received": {
            "vendor": "cisco",
            "os_type": "ios",
            "version_string": "15.7(2.0z)M",
            "major": "15",
            "minor": "7",
            "patch": None,
            "prerelease": None,
            "buildmetadata": None,
            "vendor_metadata": False,
        },
    },
    {
        "sent": {"vendor": "arista", "platform": "eos", "version": "4.15.3f"},
        "received": {
            "vendor": "arista",
            "os_type": "eos",
            "version_string": "4.15.3f",
            "major": "4",
            "minor": "15",
            "patch": None,
            "prerelease": None,
            "buildmetadata": None,
            "vendor_metadata": False,
        },
    },
    # Juniper Junos uses a custom parser
    {
        "sent": {"vendor": "juniper", "platform": "junos", "version": "12.4R"},
        "received": {
            "vendor": "juniper",
            "os_type": "junos",
            "version_string": "12.4R",
            "isservice": False,
            "ismaintenance": False,
            "isfrs": True,
            "isspecial": False,
            "main": "12",
            "minor": "4",
            "type": "R",
            "build": None,
            "service": None,
            "service_build": None,
            "service_respin": None,
            "buildmetadata": None,
            "vendor_metadata": True,
            "prerelease": None,
            "major": "12",
            "patch": None,
        },
    },
    {
        "sent": {"vendor": "juniper", "platform": "junos", "version": "12.3x48-d80"},
        "received": {
            "vendor": "juniper",
            "os_type": "junos",
            "version_string": "12.3x48-d80",
            "isservice": False,
            "ismaintenance": False,
            "isfrs": False,
            "isspecial": True,
            "main": "12",
            "minor": "3",
            "type": "x",
            "build": "48",
            "service": "d",
            "service_build": "80",
            "service_respin": None,
            "buildmetadata": None,
            "vendor_metadata": True,
            "prerelease": None,
            "major": "12",
            "patch": "48",
        },
    },
    {
        "sent": {"vendor": "juniper", "platform": "junos", "version": "12.3x48:d80"},
        "received": {
            "vendor": "juniper",
            "os_type": "junos",
            "version_string": "12.3x48:d80",
            "isservice": False,
            "ismaintenance": False,
            "isfrs": False,
            "isspecial": True,
            "main": "12",
            "minor": "3",
            "type": "x",
            "build": "48",
            "service": "d",
            "service_build": "80",
            "service_respin": None,
            "buildmetadata": None,
            "vendor_metadata": True,
            "prerelease": None,
            "major": "12",
            "patch": "48",
        },
    },
    {
        "sent": {"vendor": "juniper", "platform": "junos", "version": "12.3R12-S15"},
        "received": {
            "vendor": "juniper",
            "os_type": "junos",
            "version_string": "12.3R12-S15",
            "isservice": True,
            "ismaintenance": True,
            "isfrs": False,
            "isspecial": False,
            "main": "12",
            "minor": "3",
            "type": "R",
            "build": "12",
            "service": "S",
            "service_build": "15",
            "service_respin": None,
            "buildmetadata": None,
            "vendor_metadata": True,
            "prerelease": None,
            "major": "12",
            "patch": "12",
        },
    },
]

platform_nist_urls = [
    {
        "sent": {"vendor": "cisco", "platform": "ios", "version": "15.5"},
        "received": ["https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString=cpe:2.3:o:cisco:ios:15.5:*"],
    },
    {
        "sent": {"vendor": "arista", "platform": "eos", "version": "4.15.3f"},
        "received": [
            "https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString=cpe:2.3:o:arista:eos:4.15.3f:*"
        ],
    },
    # Juniper platforms receive multiple URLs to try as they are not very standardized and some return info on both
    {
        "sent": {"vendor": "juniper", "platform": "junos", "version": "12.3R12-S15"},
        "received": [
            "https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString=cpe:2.3:o:juniper:junos:12.3r12:s15:*:*:*:*:*:*",
            "https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString=cpe:2.3:o:juniper:junos:12.3r12-s15:*:*:*:*:*:*:*",
        ],
    },
    {
        "sent": {"vendor": "juniper", "platform": "junos", "version": "12.3x48:d25"},
        "received": [
            "https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString=cpe:2.3:o:juniper:junos:12.3x48:d25:*:*:*:*:*:*",
            "https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString=cpe:2.3:o:juniper:junos:12.3x48-d25:*:*:*:*:*:*:*",
        ],
    },
]


# Testing the parsing of a Vendor, Platform, Version into vendor standardized sections
@pytest.mark.parametrize("data", platform_data)
def test_platform_parsing(data):
    platform_obj = os_platform_object_builder(data["sent"]["vendor"], data["sent"]["platform"], data["sent"]["version"])
    assert platform_obj.asdict() == data["received"]


# Testing the composition of the nist url(s) created for a platform
@pytest.mark.parametrize("data", platform_nist_urls)
def test_platform_nist(data):
    platform_obj = os_platform_object_builder(data["sent"]["vendor"], data["sent"]["platform"], data["sent"]["version"])
    assert platform_obj.get_nist_urls() == data["received"]
