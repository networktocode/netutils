"""Functions for working with Passwords."""

import crypt
import random
import secrets
import string
import sys
import ast
import typing as t
from functools import wraps

# Code example from Python docs
ALPHABET = string.ascii_letters + string.digits
DEFAULT_PASSWORD_CHARS = "".join((string.ascii_letters + string.digits + ".,:-_"))
DEFAULT_PASSWORD_LENGTH = 20
ENCRYPT_TYPE7_LENGTH = 25

XLAT = [
    "0x64",
    "0x73",
    "0x66",
    "0x64",
    "0x3b",
    "0x6b",
    "0x66",
    "0x6f",
    "0x41",
    "0x2c",
    "0x2e",
    "0x69",
    "0x79",
    "0x65",
    "0x77",
    "0x72",
    "0x6b",
    "0x6c",
    "0x64",
    "0x4a",
    "0x4b",
    "0x44",
    "0x48",
    "0x53",
    "0x55",
    "0x42",
    "0x73",
    "0x67",
    "0x76",
    "0x63",
    "0x61",
    "0x36",
    "0x39",
    "0x38",
    "0x33",
    "0x34",
    "0x6e",
    "0x63",
    "0x78",
    "0x76",
    "0x39",
    "0x38",
    "0x37",
    "0x33",
    "0x32",
    "0x35",
    "0x34",
    "0x6b",
    "0x3b",
    "0x66",
    "0x67",
    "0x38",
    "0x37",
]


def _fail_on_mac(func: t.Callable[..., t.Any]) -> t.Callable[..., t.Any]:
    """There is an issue with Macintosh for encryption."""

    @wraps(func)
    def decorated(*args: t.Any, **kwargs: t.Any) -> t.Any:
        if sys.platform == "darwin":
            raise ValueError("Macintosh is not supported, see https://bugs.python.org/issue33213 for upstream issue.")
        return func(*args, **kwargs)

    return decorated


def compare_type5(
    unencrypted_password: str, encrypted_password: str, return_original: bool = False
) -> t.Union[str, bool]:
    """Given an encrypted and unencrypted password of Cisco Type 5 password, compare if they are a match.

    Args:
        unencrypted_password: A password that has not been encrypted, and will be compared against.
        encrypted_password: A password that has been encrypted.
        return_original: Whether or not to return the original, this is helpful when used to populate the configuration. Defaults to False.

    Returns:
        Whether or not the password is as compared to.

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


def compare_type7(
    unencrypted_password: str, encrypted_password: str, return_original: bool = False
) -> t.Union[str, bool]:
    """Given an encrypted and unencrypted password of Cisco Type 7 password, compare if they are a match.

    Args:
        unencrypted_password: A password that has not been encrypted, and will be compared against.
        encrypted_password: A password that has been encrypted.
        return_original: Whether or not to return the original, this is helpful when used to populate the configuration. Defaults to False.

    Returns:
        Whether or not the password is as compared to.

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


def decrypt_type7(encrypted_password: str) -> str:
    """Given an unencrypted password of Cisco Type 7 password decrypt it.

    Args:
        encrypted_password: A password that has been encrypted, and will be decrypted.

    Returns:
        The unencrypted_password password.

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
def encrypt_type5(unencrypted_password: str, salt: t.Optional[str] = None, salt_len: int = 4) -> str:
    """Given an unencrypted password of Cisco Type 5 password, encrypt it.

    Args:
        unencrypted_password: A password that has not been encrypted, and will be compared against.
        salt: A random set of characters that can be set by the operator. Defaults to random generated one.
        salt_len: The number of random set of characters, when not manually set. Defaults to 4.

    Returns:
        The encrypted password.

    Example:
        >>> from netutils.password import encrypt_type5
        >>> encrypt_type5("cisco")  # doctest: +SKIP
        '$1$MHkb$v2MFmDkQX66TTxLkFF50K/'
        >>>
    """
    if not salt:
        salt = "".join(secrets.choice(ALPHABET) for _ in range(salt_len))
    elif not set(salt) <= set(ALPHABET):
        raise ValueError(f"type5_pw salt used inproper characters, must be one of {ALPHABET}")
    return crypt.crypt(unencrypted_password, f"$1${salt}$")


def encrypt_type7(unencrypted_password: str, salt: t.Optional[int] = None) -> str:
    """Given an unencrypted password of Cisco Type 7 password, encypt it.

    Args:
        unencrypted_password: A password that has not been encrypted, and will be compared against.
        salt: A random number between 0 and 15 that can be set by the operator. Defaults to random generated one.

    Returns:
        The encrypted password.

    Example:
        >>> from netutils.password import encrypt_type7
        >>> encrypt_type7("cisco", 11)
        '110A1016141D'
        >>>
    """
    # max length of password for encrypt t7 is 25
    if len(unencrypted_password) > ENCRYPT_TYPE7_LENGTH:  # nosec
        raise ValueError("Password must not exceed 25 characters.")

    if not salt:
        salt = random.randint(0, 15)  # nosec
    # Start building the encrypted password - pre-pend the 2 decimal digit offset.
    encrypted_password = format(salt, "02d")
    for i, _ in enumerate(unencrypted_password):
        # Get the next of the plaintext character.
        dec_char = ord(unencrypted_password[i])
        # Get the next character of the key.
        key_char = ast.literal_eval(XLAT[(i + salt) % 53])
        # XOR the plaintext character with the key character.
        enc_char = dec_char ^ key_char
        # Build the encrypted password one character at a time.
        # The ASCII code of each encrypted character is added as 2 hex digits.
        encrypted_password += format(enc_char, "02X")
    return encrypted_password


def get_hash_salt(encrypted_password: str) -> str:
    """Given an encrypted password obtain the salt value from it.

    Args:
        encrypted_password: A password that has been encrypted, which the salt will be taken from.

    Returns:
        The encrypted password.

    Example:
        >>> from netutils.password import get_hash_salt
        >>> get_hash_salt('$1$ZLGo$J.gAGxS2wqO96drs0Cith/')
        'ZLGo'
        >>>
    """
    split_password = encrypted_password.split("$")
    if len(split_password) != 4:
        raise ValueError(f"Could not parse salt out password correctly from {encrypted_password}")
    return split_password[2]
