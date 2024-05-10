"""Test functions for NIST URL Utility"""

import pytest

from netutils.nist import get_nist_urls

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


# Testing the composition of the nist url(s) created for a platform
@pytest.mark.parametrize("data", platform_nist_urls)
def test_platform_nist(data):
    platform_obj = get_nist_urls(data["sent"]["vendor"], data["sent"]["platform"], data["sent"]["version"])
    assert platform_obj == data["received"]
