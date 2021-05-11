"""Functions for working with Passwords."""

import crypt
import random
import string
import secrets
import sys
from functools import wraps

# Code example from Python docs
ALPHABET = string.ascii_letters + string.digits
DEFAULT_PASSWORD_CHARS = "".join((string.ascii_letters + string.digits + ".,:-_"))
DEFAULT_PASSWORD_LENGTH = 20

XLAT = [
    0x64,
    0x73,
    0x66,
    0x64,
    0x3B,
    0x6B,
    0x66,
    0x6F,
    0x41,
    0x2C,
    0x2E,
    0x69,
    0x79,
    0x65,
    0x77,
    0x72,
    0x6B,
    0x6C,
    0x64,
    0x4A,
    0x4B,
    0x44,
    0x48,
    0x53,
    0x55,
    0x42,
    0x73,
    0x67,
    0x76,
    0x63,
    0x61,
    0x36,
    0x39,
    0x38,
    0x33,
    0x34,
    0x6E,
    0x63,
    0x78,
    0x76,
    0x39,
    0x38,
    0x37,
    0x33,
    0x32,
    0x35,
    0x34,
    0x6B,
    0x3B,
    0x66,
    0x67,
    0x38,
    0x37,
]


def _fail_on_mac(func):
    """There is an issue with Macintosh for encryption."""

    @wraps(func)
    def decorated(*args, **kwargs):
        if sys.platform == "darwin":
            raise ValueError("Macintosh is not supported, see https://bugs.python.org/issue33213 for upstream issue.")
        return func(*args, **kwargs)

    return decorated


def compare_type5(unencrypted_password, encrypted_password, return_original=False):
    """Given an encrypted and unencrypted password of Cisco Type 5 password, compare if they are a match.

    Args:
        unencrypted_password (str): A password that has not been encrypted, and will be compared against.
        encrypted_password (str): A password that has been encrypted.
        return_original (bool, optional): Whether or not to return the original, this is helpful when used to populate the configuration. Defaults to False.

    Returns:
        bool: Whether or not the password is as compared to.

    Example:
        >>> from netutils.password import compare_type5
        >>> compare_type5("cisco","$1$nTc1$Z28sUTcWfXlvVe2x.3XAa.")
        True
        >>> compare_type5("not_cisco","$1$nTc1$Z28sUTcWfXlvVe2x.3XAa.")
        False
        >>>
    """
    salt = get_hash_salt(encrypted_password)
    if encrypt_type5(unencrypted_password, salt) == encrypted_password:
        if return_original is True:
            return encrypted_password
        return True
    return False


def compare_type7(unencrypted_password, encrypted_password, return_original=False):
    """Given an encrypted and unencrypted password of Cisco Type 7 password, compare if they are a match.

    Args:
        unencrypted_password (str): A password that has not been encrypted, and will be compared against.
        encrypted_password (str): A password that has been encrypted.
        return_original (bool, optional): Whether or not to return the original, this is helpful when used to populate the configuration. Defaults to False.

    Returns:
        bool: Whether or not the password is as compared to.

    Example:
        >>> from netutils.password import compare_type7
        >>> compare_type7("cisco","121A0C041104")
        True
        >>> compare_type7("not_cisco","121A0C041104")
        False
        >>>
    """
    if decrypt_type7(encrypted_password) == unencrypted_password:
        if return_original is True:
            return encrypted_password
        return True
    return False


def decrypt_type7(encrypted_password):
    """Given an unencrypted password of Cisco Type 7 password decrypt it.

    Args:
        encrypted_password (str): A password that has been encrypted, and will be decrypted.

    Returns:
        string: The unencrypted_password password.

    Example:
        >>> from netutils.password import decrypt_type7
        >>> decrypt_type7("121A0C041104")
        'cisco'
        >>>
    """
    return "".join(
        [
            chr(
                int(encrypted_password[i : i + 2], 16)  # noqa: E203
                ^ ord(
                    "dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv9873254k;fg87"[
                        int((int(encrypted_password[:2]) + i / 2 - 1) % 53)
                    ]
                )
            )
            for i in range(2, len(encrypted_password), 2)
        ]
    )


@_fail_on_mac
def encrypt_type5(unencrypted_password, salt=None, salt_len=4):
    """Given an unencrypted password of Cisco Type 5 password, encrypt it.

    Args:
        unencrypted_password (str): A password that has not been encrypted, and will be compared against.
        salt (str, optional): A random set of characters that can be set by the operator. Defaults to random generated one.
        salt_len (int, optional): The number of random set of characters, when not manually set. Defaults to 4.

    Returns:
        string: The encrypted password.

    Example:
        >>> from netutils.password import encrypt_type5
        >>> encrypt_type5("cisco")  # doctest: +SKIP
        '$1$MHkb$v2MFmDkQX66TTxLkFF50K/'
        >>>
    """
    if not salt:
        salt = "".join(secrets.choice(ALPHABET) for i in range(salt_len))
    elif not set(salt) <= set(ALPHABET):
        raise ValueError("type5_pw salt used inproper characters, must be one of %s" % (ALPHABET))
    return crypt.crypt(unencrypted_password, f"$1${salt}$")


def encrypt_type7(unencrypted_password, salt=None):
    """Given an unencrypted password of Cisco Type 7 password, encypt it.

    Args:
        unencrypted_password (str): A password that has not been encrypted, and will be compared against.
        salt (str, optional): A random number between 0 and 15 that can be set by the operator. Defaults to random generated one.

    Returns:
        string: The encrypted password.

    Example:
        >>> from netutils.password import encrypt_type7
        >>> encrypt_type5("cisco")  # doctest: +SKIP
        '$1$ZLGo$J.gAGxS2wqO96drs0Cith/'
        >>>
    """
    if not salt:
        salt = random.randrange(0, 15)  # nosec
    encrypted_password = "%02x" % salt
    for i, _ in enumerate(unencrypted_password):
        encrypted_password += "%02x" % (ord(unencrypted_password[i]) ^ XLAT[salt])
        salt += 1
        if salt == 51:
            salt = 0
    return encrypted_password


def get_hash_salt(encrypted_password):
    """Given an encrypted password obtain the salt value from it.

    Args:
        encrypted_password (str): A password that has been encrypted, which the salt will be taken from.

    Returns:
        string: The encrypted password.

    Example:
        >>> from netutils.password import get_hash_salt
        >>> get_hash_salt('$1$ZLGo$J.gAGxS2wqO96drs0Cith/')
        'ZLGo'
        >>>
    """
    split_password = encrypted_password.split("$")
    if len(split_password) != 4:
        raise ValueError("Could not parse salt out password correctly from {0}".format(encrypted_password))
    return split_password[2]
