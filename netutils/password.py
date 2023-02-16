"""Functions for working with Passwords."""

import crypt
import random
import secrets
import string
import sys
import ast
import typing as t
from functools import wraps
import hashlib

# Code example from Python docs
ALPHABET = string.ascii_letters + string.digits
DEFAULT_PASSWORD_CHARS = "".join((string.ascii_letters + string.digits + ".,:-_"))
DEFAULT_PASSWORD_LENGTH = 20
ENCRYPT_TYPE7_LENGTH = 25
ENCRYPT_TYPE9_ENCODING_CHARS = "".join(("./", string.digits, string.ascii_uppercase, string.ascii_lowercase))

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

    Examples:
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

    Examples:
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


def compare_type9(
    unencrypted_password: str, encrypted_password: str, return_original: bool = False
) -> t.Union[str, bool]:
    """Given an encrypted and unencrypted password of Cisco Type 7 password, compare if they are a match.

    Args:
        unencrypted_password: A password that has not been encrypted, and will be compared against.
        encrypted_password: A password that has been encrypted.
        return_original: Whether or not to return the original, this is helpful when used to populate the configuration. Defaults to False.

    Returns:
        Whether or not the password is as compared to.

    Examples:
        >>> from netutils.password import compare_type9
        >>> compare_type9("cisco","$9$588|P!iWqEx=Wf$nadLmT9snc6V9QAeUuATSOoCAZMQIHqixJfZpQj5EU2")
        True
        >>> compare_type7("not_cisco","$9$588|P!iWqEx=Wf$nadLmT9snc6V9QAeUuATSOoCAZMQIHqixJfZpQj5EU2")
        False
        >>>
    """
    salt = get_hash_salt(encrypted_password)
    if encrypt_type9(unencrypted_password, salt) == encrypted_password:
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

    Examples:
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

    Examples:
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

    Examples:
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


def _wpa_base64_encode(data: bytes):
    # Adapted with many thanks from https://github.com/skrobul/cisco_scrypt/blob/main/lib/cisco_scrypt.rb

    # Cisco uses non-standard base64 encoding, which happens to be the same
    # implementation as used for WPA passwords.
    # this involves encoding 3 bytes at a time.

    # First we need to pad the string with NULs until its length is a multiple of 3
    modulus = len(data) % 3
    padding = b"\x00" * (3 - modulus)
    data += padding
    result = ""

    # Now we can encode the string in 3-byte chunks
    for chunk in [data[i:i+3] for i in range(0, len(data), 3)]:
        # Now we run each chunk through the WPA base64 encoding algorythm
        # The fiddly bit is that the iteration count depends on the length of the chunk, excluding the padding, +1
        # so if the chunk is 3 bytes long, we iterate 4 times, if it's 2 bytes long, we iterate 3 times, etc.
        byte_count = len(chunk.strip(b"\x00"))
        iterations = byte_count + 1
        value = int.from_bytes(chunk, byteorder="big")
        encoded_chunk = ""
        for _ in range(iterations):
            position = (value & 0xFC0000) >> 18
            encoded_chunk += ENCRYPT_TYPE9_ENCODING_CHARS[position]
            value = value << 6
        result += encoded_chunk

    return result


def encrypt_type9(unencrypted_password: str, salt: t.Optional[str] = None) -> str:
    """Given an unencrypted password of Cisco Type 9 password, encypt it.

    Args:
        unencrypted_password: A password that has not been encrypted, and will be compared against.
        salt: a 14-character string that can be set by the operator. Defaults to random generated one.

    Returns:
        The encrypted password.

    Examples:
        >>> from netutils.password import encrypt_type9
        >>> encrypt_type7("123456")
        "$9$cvWdfQlRRDKq/U$VFTPha5VHTCbSgSUAo.nPoh50ZiXOw1zmljEjXkaq1g"
        >>> encrypt_type7("123456", "cvWdfQlRRDKq/U")
        "$9$cvWdfQlRRDKq/U$VFTPha5VHTCbSgSUAo.nPoh50ZiXOw1zmljEjXkaq1g"
    """
    if salt:
        if len(salt) != 14:
            raise ValueError("Salt must be 14 characters long.")
        salt_bytes = salt.encode()
    else:
        # salt must always be a 14-byte-long printable string, often includes symbols
        salt_bytes = "".join(secrets.choice(ENCRYPT_TYPE9_ENCODING_CHARS) for _ in range(14)).encode()

    key = hashlib.scrypt(unencrypted_password.encode(), salt=salt_bytes, n=2**14, r=1, p=1, dklen=32)
    hash = _wpa_base64_encode(key)

    return f"$9${salt_bytes.decode()}${hash}"


def get_hash_salt(encrypted_password: str) -> str:
    """Given an encrypted password obtain the salt value from it.

    Args:
        encrypted_password: A password that has been encrypted, which the salt will be taken from.

    Returns:
        The encrypted password.

    Examples:
        >>> from netutils.password import get_hash_salt
        >>> get_hash_salt('$1$ZLGo$J.gAGxS2wqO96drs0Cith/')
        'ZLGo'
        >>>
    """
    split_password = encrypted_password.split("$")
    if len(split_password) != 4:
        raise ValueError(f"Could not parse salt out password correctly from {encrypted_password}")
    return split_password[2]
