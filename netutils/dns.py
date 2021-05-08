"""Functions for working with DNS."""
import socket


def fqdn_to_ip(hostname):
    """Provides the IP address of a resolvable name.

    Args:
        hostname (str): An FQDN that may or may not be resolvable.

    Returns:
        ip (str): The IP Address of a valid FQDN.

    Example:
        >>> from netutils.dns import fqdn_to_ip
        >>> from netutils.ip import is_ip
        >>> is_ip(fqdn_to_ip("google.com"))
        True
        >>>

    Raises:
        socket.gaierror: If FQDN is not resolvable, leverage is_fqdn_valid to check first.
    """
    return socket.gethostbyname(hostname)


def is_fqdn_valid(hostname):
    """Verifies whether a hostname is resolvable.

    Args:
        hostname (str): A FQDN that may or may not be resolvable.

    Returns:
        bool: The result as to whether or not the domain was valid.

    Example:
        >>> from netutils.dns import is_fqdn_valid
        >>> is_fqdn_valid("google.com")
        True
        >>> is_fqdn_valid("nevergonnagiveyouup.pizza")
        False
        >>>
    """
    try:
        socket.gethostbyname(hostname)
        return True
    except socket.error:
        return False
