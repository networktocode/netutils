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

COMPARE_TYPE9 = [
    {
        "sent": {"unencrypted_password": "cisco", "encrypted_password": "$9$588|P!iWqEx=Wf$nadLmT9snc6V9QAeUuATSOoCAZMQIHqixJfZpQj5EU2"},
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
        "sent": {"unencrypted_password": "invalid_password", "encrypted_password": "$9$588|P!iWqEx=Wf$nadLmT9snc6V9QAeUuATSOoCAZMQIHqixJfZpQj5EU2"},
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

ENCRYPT_TYPE9 = [
    {
        "sent": {"unencrypted_password": "123456", "salt": "cvWdfQlRRDKq/U"},
        "received": "$9$cvWdfQlRRDKq/U$VFTPha5VHTCbSgSUAo.nPoh50ZiXOw1zmljEjXkaq1g",
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

@pytest.mark.parametrize("data", COMPARE_TYPE9)
def test_compare_type9(data):
    assert password.compare_type9(**data["sent"]) == data["received"]

@pytest.mark.parametrize("data", DECRYPT_TYPE7)
def test_decrypt_type7(data):
    assert password.decrypt_type7(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", ENCRYPT_TYPE5)
def test_encrypt_type5(data):
    assert password.encrypt_type5(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", ENCRYPT_TYPE7)
def test_encrypt_type7(data):
    assert password.encrypt_type7(**data["sent"]) == data["received"]

@pytest.mark.parametrize("data", ENCRYPT_TYPE9)
def test_encrypt_type9(data):
    assert password.encrypt_type9(**data["sent"]) == data["received"]

@pytest.mark.parametrize("data", GET_HASH_SALT)
def test_get_hash_salt(data):
    assert password.get_hash_salt(**data["sent"]) == data["received"]
