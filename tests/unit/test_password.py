"""Test for the password functions."""
import pytest

from netutils import password

COMPARE_TYPE5 = [
    {
        "sent": {"unencrypted_password": "cisco", "encrypted_password": "$1$nTc1$Z28sUTcWfXlvVe2x.3XAa."},
        "received": True,
    },
    {
        "sent": {
            "unencrypted_password": "cisco",
            "encrypted_password": "$1$nTc1$Z28sUTcWfXlvVe2x.3XAa.",
            "return_original": True,
        },
        "received": "$1$nTc1$Z28sUTcWfXlvVe2x.3XAa.",
    },
    {
        "sent": {"unencrypted_password": "inavalid_password", "encrypted_password": "$1$nTc1$Z28sUTcWfXlvVe2x.3XAa."},
        "received": False,
    },
]

COMPARE_TYPE7 = [
    {
        "sent": {"unencrypted_password": "cisco", "encrypted_password": "121A0C041104"},
        "received": True,
    },
    {
        "sent": {
            "unencrypted_password": "cisco",
            "encrypted_password": "121A0C041104",
            "return_original": True,
        },
        "received": "121A0C041104",
    },
    {
        "sent": {"unencrypted_password": "invalid_password", "encrypted_password": "121A0C041104"},
        "received": False,
    },
]

DECRYPT_TYPE7 = [
    {
        "sent": {"encrypted_password": "121A0C041104"},
        "received": "cisco",
    }
]

ENCRYPT_TYPE5 = [
    {
        "sent": {"unencrypted_password": "cisco", "salt": "nTc1"},
        "received": "$1$nTc1$Z28sUTcWfXlvVe2x.3XAa.",
    },
]

ENCRYPT_TYPE7 = [
    {
        "sent": {"unencrypted_password": "cisco", "salt": 10},
        "received": "0a4d000a0618",
    },
]

GET_HASH_SALT = [
    {
        "sent": {"encrypted_password": "$1$nTc1$Z28sUTcWfXlvVe2x.3XAa."},
        "received": "nTc1",
    },
]


@pytest.mark.parametrize("data", COMPARE_TYPE5)
def test_compare_type5(data):
    assert password.compare_type5(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", COMPARE_TYPE7)
def test_compare_type7(data):
    assert password.compare_type7(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", DECRYPT_TYPE7)
def test_decrypt_type7(data):
    assert password.decrypt_type7(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", ENCRYPT_TYPE5)
def test_encrypt_type5(data):
    assert password.encrypt_type5(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", ENCRYPT_TYPE7)
def test_encrypt_type7(data):
    assert password.encrypt_type7(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", GET_HASH_SALT)
def test_get_hash_salt(data):
    assert password.get_hash_salt(**data["sent"]) == data["received"]
