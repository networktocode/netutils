"""Functions for working with Passwords."""

# TODO: Swap out crypt prior to py3.13
import crypt  # pylint: disable=deprecated-module
import random
import secrets
import string
import sys
import ast
import typing as t
from functools import wraps
import base64

try:
    from hashlib import scrypt

    HAS_SCRYPT = True
except ImportError:
    HAS_SCRYPT = False


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

JUNIPER_ENCODING = [
    [1, 4, 32],
    [1, 16, 32],
    [1, 8, 32],
    [1, 64],
    [1, 32],
    [1, 4, 16, 128],
    [1, 32, 64],
]

JUNIPER_KEYS = ["QzF3n6/9CAtpu0O", "B1IREhcSyrleKvMW8LXx", "7N-dVbwsY2g4oaJZGUDj", "iHkq.mPf5T"]
JUNIPER_KEYS_STRING = "".join(JUNIPER_KEYS)
JUNIPER_KEYS_LENGTH = len(JUNIPER_KEYS_STRING)
JUNIPER_CHARACTER_KEYS: t.Dict[str, int] = {}
for idx, jun_key in enumerate(JUNIPER_KEYS):
    for character in jun_key:
        JUNIPER_CHARACTER_KEYS[character] = 3 - idx


def _fail_on_mac(func: t.Callable[..., t.Any]) -> t.Callable[..., t.Any]:
    """There is an issue with Macintosh for encryption."""

    @wraps(func)
    def decorated(*args: t.Any, **kwargs: t.Any) -> t.Any:
        if sys.platform == "darwin":
            raise ValueError("Macintosh is not supported, see https://bugs.python.org/issue33213 for upstream issue.")
        return func(*args, **kwargs)

    return decorated


def compare_cisco_type5(
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
        >>> from netutils.password import compare_cisco_type5
        >>> compare_cisco_type5("cisco","$1$nTc1$Z28sUTcWfXlvVe2x.3XAa.")
        True
        >>> compare_cisco_type5("not_cisco","$1$nTc1$Z28sUTcWfXlvVe2x.3XAa.")
        False
        >>>
    """
    salt = get_hash_salt(encrypted_password)
    if encrypt_cisco_type5(unencrypted_password, salt) == encrypted_password:
        if return_original is True:
            return encrypted_password
        return True
    return False


def compare_cisco_type7(
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
        >>> from netutils.password import compare_cisco_type7
        >>> compare_cisco_type7("cisco","121A0C041104")
        True
        >>> compare_cisco_type7("not_cisco","121A0C041104")
        False
        >>>
    """
    if decrypt_cisco_type7(encrypted_password) == unencrypted_password:
        if return_original is True:
            return encrypted_password
        return True
    return False


def compare_cisco_type9(
    unencrypted_password: str, encrypted_password: str, return_original: bool = False
) -> t.Union[str, bool]:
    """Given an encrypted and unencrypted password of Cisco Type 9 password, compare if they are a match.

    Args:
        unencrypted_password: A password that has not been encrypted, and will be compared against.
        encrypted_password: A password that has been encrypted.
        return_original: Whether or not to return the original, this is helpful when used to populate the configuration. Defaults to False.

    Returns:
        Whether or not the password is as compared to.

    Examples:
        >>> from netutils.password import compare_cisco_type9
        >>> compare_cisco_type9("cisco","$9$588|P!iWqEx=Wf$nadLmT9snc6V9QAeUuATSOoCAZMQIHqixJfZpQj5EU2")
        True
        >>> compare_cisco_type9("not_cisco","$9$588|P!iWqEx=Wf$nadLmT9snc6V9QAeUuATSOoCAZMQIHqixJfZpQj5EU2")
        False
        >>>
    """
    salt = get_hash_salt(encrypted_password)
    if encrypt_cisco_type9(unencrypted_password, salt) == encrypted_password:
        if return_original is True:
            return encrypted_password
        return True
    return False


def decrypt_cisco_type7(encrypted_password: str) -> str:
    """Given an unencrypted password of Cisco Type 7 password decrypt it.

    Args:
        encrypted_password: A password that has been encrypted, and will be decrypted.

    Returns:
        The unencrypted_password password.

    Examples:
        >>> from netutils.password import decrypt_cisco_type7
        >>> decrypt_cisco_type7("121A0C041104")
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
def encrypt_cisco_type5(unencrypted_password: str, salt: t.Optional[str] = None, salt_len: int = 4) -> str:
    """Given an unencrypted password of Cisco Type 5 password, encrypt it.

    Args:
        unencrypted_password: A password that has not been encrypted, and will be compared against.
        salt: A random set of characters that can be set by the operator. Defaults to random generated one.
        salt_len: The number of random set of characters, when not manually set. Defaults to 4.

    Returns:
        The encrypted password.

    Examples:
        >>> from netutils.password import encrypt_cisco_type5
        >>> encrypt_cisco_type5("cisco")  # doctest: +SKIP
        '$1$MHkb$v2MFmDkQX66TTxLkFF50K/'
        >>>
    """
    if not salt:
        salt = "".join(secrets.choice(ALPHABET) for _ in range(salt_len))
    elif not set(salt) <= set(ALPHABET):
        raise ValueError(f"type5_pw salt used improper characters, must be one of {ALPHABET}")
    return crypt.crypt(unencrypted_password, f"$1${salt}$")


def encrypt_cisco_type7(unencrypted_password: str, salt: t.Optional[int] = None) -> str:
    """Given an unencrypted password of Cisco Type 7 password, encrypt it.

    Args:
        unencrypted_password: A password that has not been encrypted, and will be compared against.
        salt: A random number between 0 and 15 that can be set by the operator. Defaults to random generated one.

    Returns:
        The encrypted password.

    Examples:
        >>> from netutils.password import encrypt_cisco_type7
        >>> encrypt_cisco_type7("cisco", 11)
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
        dec_char = ord(unencrypted_password[i])  # pylint: disable=unnecessary-list-index-lookup
        # Get the next character of the key.
        key_char = ast.literal_eval(XLAT[(i + salt) % 53])
        # XOR the plaintext character with the key character.
        enc_char = dec_char ^ key_char
        # Build the encrypted password one character at a time.
        # The ASCII code of each encrypted character is added as 2 hex digits.
        encrypted_password += format(enc_char, "02X")
    return encrypted_password


def encrypt_cisco_type9(unencrypted_password: str, salt: t.Optional[str] = None) -> str:
    """Given an unencrypted password of Cisco Type 9 password, encrypt it.

    Note: This uses the built-in Python `scrypt` function to generate the password
    hash. However, this function is not available on the default Python installed
    on MacOS. If MacOS is used, it is recommended to install Python using Homebrew
    (or similar) which will include `scrypt`.

    Args:
        unencrypted_password: A password that has not been encrypted, and will be compared against.
        salt: a 14-character string that can be set by the operator. Defaults to random generated one.

    Returns:
        The encrypted password.

    Examples:
        >>> from netutils.password import encrypt_cisco_type9
        >>> encrypt_cisco_type9("123456", "cvWdfQlRRDKq/U")
        '$9$cvWdfQlRRDKq/U$VFTPha5VHTCbSgSUAo.nPoh50ZiXOw1zmljEjXkaq1g'

    Raises:
        ImportError: If `scrypt` cannot be imported from the system.
    """
    if not HAS_SCRYPT:
        raise ImportError(
            "Your version of python does not have scrypt support built in. "
            "Please install a version of python with scrypt."
        )

    if salt:
        if len(salt) != 14:
            raise ValueError("Salt must be 14 characters long.")
        salt_bytes = salt.encode()
    else:
        # salt must always be a 14-byte-long printable string, often includes symbols
        salt_bytes = "".join(secrets.choice(ENCRYPT_TYPE9_ENCODING_CHARS) for _ in range(14)).encode()

    key = scrypt(unencrypted_password.encode(), salt=salt_bytes, n=2**14, r=1, p=1, dklen=32)

    # Cisco type 9 uses a different base64 encoding than the standard one, so we need to translate from
    # the standard one to the Cisco one.
    type9_encoding_translation_table = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
        ENCRYPT_TYPE9_ENCODING_CHARS,
    )
    hashed_password = base64.b64encode(key).decode().translate(type9_encoding_translation_table)

    # and strip off the trailing '='
    hashed_password = hashed_password[:-1]

    return f"$9${salt_bytes.decode()}${hashed_password}"


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


def decrypt_juniper_type9(encrypted_password: str) -> str:
    """Given an encrypted Junos $9$ type password, decrypt it.

    Args:
        encrypted_password: A password that has been encrypted, and will be decrypted.

    Returns:
        The unencrypted_password password.

    Examples:
        >>> from netutils.password import decrypt_juniper_type9
        >>> decrypt_juniper_type9("$9$7YdwgGDkTz6oJz69A1INdb")
        'juniper'
        >>>
    """
    # Strip $9$ from start of string
    password_characters = encrypted_password.split("$9$", 1)[1]

    # Get first character and toss extra characters
    first_character = password_characters[0]
    stripped_password_characters = password_characters[JUNIPER_CHARACTER_KEYS[first_character] + 1 :]  # noqa: E203

    previous_char = first_character
    decrypted_password = ""  # nosec
    while stripped_password_characters:
        # Get encoding modulus
        decode = JUNIPER_ENCODING[len(decrypted_password) % len(JUNIPER_ENCODING)]

        # Get nibble we will decode
        nibble = stripped_password_characters[0 : len(decode)]  # noqa: E203
        stripped_password_characters = stripped_password_characters[len(decode) :]  # noqa: E203

        # Decode value for nibble and convert to character, append to decrypted password
        value = 0
        for index, char in enumerate(nibble):
            gap = (
                (JUNIPER_KEYS_STRING.index(char) - JUNIPER_KEYS_STRING.index(previous_char)) % JUNIPER_KEYS_LENGTH
            ) - 1
            value += gap * decode[index]
            previous_char = char
        decrypted_password += chr(value)

    return decrypted_password


def encrypt_juniper_type9(unencrypted_password: str, salt: t.Optional[int] = None) -> str:
    """Given an unencrypted password, encrypt to Juniper $9$ type password.

    Args:
        unencrypted_password: A password that has not been encrypted, and will be compared against.
        salt: A integer that can be set by the operator. Defaults to random generated one.

    Returns:
        The encrypted password.

    Examples:
        >>> from netutils.password import encrypt_juniper_type9
        >>> encrypt_juniper_type9("juniper", 35) # doctest: +SKIP
        '$9$7YdwgGDkTz6oJz69A1INdb'
        >>>
    """
    if not salt:
        salt = random.randint(0, JUNIPER_KEYS_LENGTH) - 1  # nosec

    # Use salt to generate start of encrypted password
    first_character = JUNIPER_KEYS_STRING[salt]
    random_chars = "".join(
        [
            JUNIPER_KEYS_STRING[random.randint(0, JUNIPER_KEYS_LENGTH) - 1]  # nosec
            for x in range(0, JUNIPER_CHARACTER_KEYS[first_character])
        ]
    )
    encrypted_password = "$9$" + first_character + random_chars

    previous_character = first_character
    for index, char in enumerate(unencrypted_password):
        encode = JUNIPER_ENCODING[index % len(JUNIPER_ENCODING)][::-1]  # Get encoding modulus in reverse order
        char_ord = ord(char)
        gaps: t.List[int] = []
        for modulus in encode:
            gaps = [int(char_ord / modulus)] + gaps
            char_ord %= modulus

        for gap in gaps:
            gap += JUNIPER_KEYS_STRING.index(previous_character) + 1
            new_character = JUNIPER_KEYS_STRING[gap % JUNIPER_KEYS_LENGTH]
            previous_character = new_character
            encrypted_password += new_character

    return encrypted_password


# Provide until transition to 2.0
compare_type5 = compare_cisco_type5
compare_type7 = compare_cisco_type7
decrypt_type7 = decrypt_cisco_type7
encrypt_type5 = encrypt_cisco_type5
encrypt_type7 = encrypt_cisco_type7
