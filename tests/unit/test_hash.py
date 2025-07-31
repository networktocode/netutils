"""Tests for the hash functions."""

import pytest

from netutils.hash import hash_data

EXPECTED_HASHES = [
    (
        "md5",
        "b31be8e621f7d7cb80289c3634a2463f",
    ),
    (
        "sha1",
        "696de4dae5e77515f0460c78dc712f9b055ae7f2",
    ),
    (
        "sha224",
        "bead2aad3706b211e825f5919db78dceca775cae4bd5b58078652ad2",
    ),
    (
        "sha256",
        "a9675e13424e5009161f7b7da6c1bb7e091f1401459176e8efce23c0f1fc5ba9",
    ),
    (
        "sha384",
        "4476744d8167497e9cbc85901a753be7bef5a33a1ce36926c5a21b68c7c2d420daa6cd347d515dd21af1e93927c7ba5c",
    ),
    (
        "sha512",
        "75dc2cbd4b2e025f8c0a1f495bc321343eef8d5561dfa02e29f77b32b9685f7add41169e7f9fb085f5110ac4635de286437c758c115b8eadacc20f086e39cc28",
    ),
    (
        "blake2b",
        "82a094789746f0a0405845ced806282e1bd6f317dd8a9464b6e660105e16108f6582c0f091d787a833c8d8fd5c53004dac2571113045fefe25d1f159f8c1f934",
    ),
    (
        "blake2s",
        "b8fecb4ff8b866c7638985eb66d4ba9cb5f908d0b1a25def4c593ba140b791af",
    ),
    (
        "sha3_224",
        "f0b2b40e360489e0e2da83094238e9591677e1d304d70a1feb1188f2",
    ),
    (
        "sha3_256",
        "308a5dd839eb055ee84f0b2c99344526a716c58a14dffb704b6784437aee91ba",
    ),
    (
        "sha3_384",
        "80e4d0e43bf447ef4d3a6dcd1a795a3573bc6f34d42b81ee78bb757bd86ed6bc9210d752797fd62bfbdb6fc17eb52ed1",
    ),
    (
        "sha3_512",
        "13dddfadbe95282b6b0da1c7c3c7dc28c086cdcc3de39baafb1fb45913ac39c0d9744927c10fb1d858ab257069d3ef367c8913553e7f7eabb1f4ffe6480e5924",
    ),
]


@pytest.mark.parametrize("algorithm,expected", EXPECTED_HASHES)
def test_hash_data(algorithm, expected):
    """Test the hash_data function."""
    data = "Network To Code"
    assert hash_data(data, algorithm) == expected


def test_hash_data_invalid_algorithm():
    """Test the hash_data function with an invalid algorithm."""
    data = "Network To Code"
    with pytest.raises(AttributeError):
        hash_data(data, "invalid")
