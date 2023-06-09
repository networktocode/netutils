"""Test for the password functions."""
import pytest

from netutils import password

COMPARE_CISCO_TYPE5 = [
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

COMPARE_CISCO_TYPE7 = [
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

COMPARE_CISCO_TYPE9 = [
    {
        "sent": {
            "unencrypted_password": "cisco",
            "encrypted_password": "$9$588|P!iWqEx=Wf$nadLmT9snc6V9QAeUuATSOoCAZMQIHqixJfZpQj5EU2",
        },
        "received": True,
    },
    {
        "sent": {
            "unencrypted_password": "cisco",
            "encrypted_password": "$9$588|P!iWqEx=Wf$nadLmT9snc6V9QAeUuATSOoCAZMQIHqixJfZpQj5EU2",
            "return_original": True,
        },
        "received": "$9$588|P!iWqEx=Wf$nadLmT9snc6V9QAeUuATSOoCAZMQIHqixJfZpQj5EU2",
    },
    {
        "sent": {
            "unencrypted_password": "invalid_password",
            "encrypted_password": "$9$588|P!iWqEx=Wf$nadLmT9snc6V9QAeUuATSOoCAZMQIHqixJfZpQj5EU2",
        },
        "received": False,
    },
]

DECRYPT_CISCO_TYPE7 = [
    {
        "sent": {"encrypted_password": "14141B180F0B"},
        "received": "cisco",
    }
]

ENCRYPT_CISCO_TYPE5 = [
    {
        "sent": {"unencrypted_password": "cisco", "salt": "nTc1"},
        "received": "$1$nTc1$Z28sUTcWfXlvVe2x.3XAa.",
    },
]

ENCRYPT_CISCO_TYPE7 = [
    {
        "sent": {"unencrypted_password": "cisco", "salt": 10},
        "received": "104D000A0618",
    },
]

ENCRYPT_CISCO_TYPE9 = [
    {
        "sent": {"unencrypted_password": "cisco", "salt": "x2xAAwQ3MBbEnk"},
        "received": "$9$x2xAAwQ3MBbEnk$JCxr6MnPb.k5ymK72mTypyRJYH5W74ZRvtLTprCj.xQ",
    },
]

GET_HASH_SALT = [
    {
        "sent": {"encrypted_password": "$1$nTc1$Z28sUTcWfXlvVe2x.3XAa."},
        "received": "nTc1",
    },
]

ENCRYPT_JUNIPER_TYPE9 = [
    {
        "sent": {"unencrypted_password": "juniper", "salt": 35},
        "received_one": "$9$7",
        "received_two": "gGDkTz6oJz69A1INdb",
    },
]

DECRYPT_JUNIPER_TYPE9 = [
    {
        "sent": {"encrypted_password": "$9$7YdwgGDkTz6oJz69A1INdb"},
        "received": "juniper",
    }
]


@pytest.mark.parametrize("data", COMPARE_CISCO_TYPE5)
def test_compare_cisco_type5(data):
    assert password.compare_cisco_type5(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", COMPARE_CISCO_TYPE7)
def test_compare_cisco_type7(data):
    assert password.compare_cisco_type7(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", COMPARE_CISCO_TYPE9)
def test_compare_cisco_type9(data):
    assert password.compare_cisco_type9(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", DECRYPT_CISCO_TYPE7)
def test_decrypt_cisco_type7(data):
    assert password.decrypt_cisco_type7(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", ENCRYPT_CISCO_TYPE5)
def test_encrypt_cisco_type5(data):
    assert password.encrypt_cisco_type5(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", ENCRYPT_CISCO_TYPE7)
def test_encrypt_cisco_type7(data):
    assert password.encrypt_cisco_type7(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", ENCRYPT_CISCO_TYPE9)
def test_encrypt_cisco_type9(data):
    assert password.encrypt_cisco_type9(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", GET_HASH_SALT)
def test_get_hash_salt(data):
    assert password.get_hash_salt(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", ENCRYPT_JUNIPER_TYPE9)
def test_encrypt_juniper_type9(data):
    # Passwords include random padding, check only the non random sections
    decrypted_password = password.encrypt_juniper_type9(**data["sent"])
    assert decrypted_password[0:4] == data["received_one"]
    assert decrypted_password[7:] == data["received_two"]


@pytest.mark.parametrize("data", DECRYPT_JUNIPER_TYPE9)
def test_decrypt_juniper_type9(data):
    assert password.decrypt_juniper_type9(**data["sent"]) == data["received"]
