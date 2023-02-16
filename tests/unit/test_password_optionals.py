"""Test for the password functions when optional packages are installed."""
import pytest

from netutils import password



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

ENCRYPT_TYPE9 = [
    {
        "sent": {"unencrypted_password": "123456", "salt": "cvWdfQlRRDKq/U"},
        "received": "$9$cvWdfQlRRDKq/U$VFTPha5VHTCbSgSUAo.nPoh50ZiXOw1zmljEjXkaq1g",
    },
]


@pytest.mark.parametrize("data", COMPARE_TYPE9)
def test_compare_type9(data):
    assert password.compare_type9(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", ENCRYPT_TYPE9)
def test_encrypt_type7(data):
    pytest.importorskip("cryptography")
    assert password.encrypt_type9(**data["sent"]) == data["received"]
