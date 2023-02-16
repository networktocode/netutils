"""Test for the password functions when optional packages are installed."""
import pytest

from netutils import password


ENCRYPT_TYPE9 = [
    {
        "sent": {"unencrypted_password": "123456", "salt": "cvWdfQlRRDKq/U"},
        "received": "$9$cvWdfQlRRDKq/U$VFTPha5VHTCbSgSUAo.nPoh50ZiXOw1zmljEjXkaq1g",
    },
]

@pytest.mark.parametrize("data", ENCRYPT_TYPE9)
def test_encrypt_type7(data):
    pytest.importorskip("cryptography")
    assert password.encrypt_type9(**data["sent"]) == data["received"]
