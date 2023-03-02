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
        "sent": {"unencrypted_password": "cisco", "encrypted_password": "070C285F4D06"},
        "received": True,
    },
    {
        "sent": {
            "unencrypted_password": "cisco",
            "encrypted_password": "070C285F4D06",
            "return_original": True,
        },
        "received": "070C285F4D06",
    },
    {
        "sent": {"unencrypted_password": "invalid_password", "encrypted_password": "070C285F4D06"},
        "received": False,
    },
]

DECRYPT_TYPE7 = [
    {
        "sent": {"encrypted_password": "14141B180F0B"},
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
        "received": "104D000A0618",
    },
]

GET_HASH_SALT = [
    {
        "sent": {"encrypted_password": "$1$nTc1$Z28sUTcWfXlvVe2x.3XAa."},
        "received": "nTc1",
    },
]

ENCRYPT_JUNIPER = [
    {
        "sent": {"unencrypted_password": "juniper", "salt": 35},
        "received_one": "$9$7",
        "received_two": "gGDkTz6oJz69A1INdb",
    },
]

DECRYPT_JUNIPER = [
    {
        "sent": {"encrypted_password": "$9$7YdwgGDkTz6oJz69A1INdb"},
        "received": "juniper",
    }
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


@pytest.mark.parametrize("data", ENCRYPT_JUNIPER)
def test_encrypt_juniper(data):
    # Passwords include random padding, check only the non random sections
    decrypted_password = password.encrypt_juniper(**data["sent"])
    assert decrypted_password[0:4] == data["received_one"]
    assert decrypted_password[7:] == data["received_two"]


@pytest.mark.parametrize("data", DECRYPT_JUNIPER)
def test_decrypt_juniper(data):
    assert password.decrypt_juniper(**data["sent"]) == data["received"]
