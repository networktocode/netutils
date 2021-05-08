"""Test for the BGP ASN functions."""

import pytest

from netutils import asn

asn_to_int = [
    {"sent": {"asplain": "6500"}, "received": 6500},
    {"sent": {"asplain": "6500.1111"}, "received": 425985111},
    {"sent": {"asplain": "6500.1"}, "received": 425984001},
    {"sent": {"asplain": "1.10"}, "received": 65546},
    {"sent": {"asplain": "0.65526"}, "received": 65526},
]


@pytest.mark.parametrize("data", asn_to_int)
def test_asn_to_int(data):
    assert asn.asn_to_int(**data["sent"]) == data["received"]
