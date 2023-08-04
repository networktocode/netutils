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

int_to_asn = [
    {"sent": {"asn_int": 6500}, "received": "6500"},
    {"sent": {"asn_int": 425985111}, "received": "6500.1111"},
    {"sent": {"asn_int": 425984001}, "received": "6500.1"},
    {"sent": {"asn_int": 65546}, "received": "1.10"},
    {"sent": {"asn_int": 65526}, "received": "65526"},
    {"sent": {"asn_int": "65526"}, "received": "65526"},
    {"sent": {"asn_int": "65535"}, "received": "65535"},
    {"sent": {"asn_int": "65536"}, "received": "1.0"},
    {"sent": {"asn_int": "425985111"}, "received": "6500.1111"},
    {"sent": {"asn_int": 4294967295}, "received": "65535.65535"},
]

int_to_asn_exceptions = [
    {"asn_int": "one22"},
    {"asn_int": "not_an_int"},
    {"asn_int": "4294967296"},
    {"asn_int": "0"},
    {"asn_int": -1},
]


@pytest.mark.parametrize("data", asn_to_int)
def test_asn_to_int(data):
    assert asn.asn_to_int(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", int_to_asn)
def test_int_to_asn(data):
    assert asn.int_to_asn(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", int_to_asn_exceptions)
def test_int_to_asn_exceptions(data):
    with pytest.raises(ValueError):
        assert asn.int_to_asn(**data)
