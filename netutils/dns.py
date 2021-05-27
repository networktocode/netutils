"""Functions for working with DNS."""
import socket


def fqdn_to_ip(hostname):
    """Provides the IP address of a resolvable name on the machine it is running from.

       There are many reasons that a valid FQDN may not be resolvable, such as a network error
       from your machine to the DNS server, an upstream DNS issue, etc.

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
        socket.gaierror: If FQDN is not resolvable, leverage is_fqdn_resolvable to check first.
    """
    # The data structure is complex, only require the first item, and drill down from there.
    return socket.getaddrinfo(hostname, 0)[0][4][0]


def is_fqdn_resolvable(hostname):
    """Verifies whether a hostname is resolvable on the machine it is running from.

       There are many reasons that a valid FQDN may not be resolvable, such as a network error
       from your machine to the DNS server, an upstream DNS issue, etc.

    Args:
        hostname (str): A FQDN that may or may not be resolvable.

    Returns:
        bool: The result as to whether or not the domain was valid.

    Example:
        >>> from netutils.dns import is_fqdn_resolvable
        >>> is_fqdn_resolvable("google.com")
        True
        >>> is_fqdn_resolvable("nevergonnagiveyouup.pizza")
        False
        >>>
    """
    try:
        socket.getaddrinfo(hostname, 0)
        return True
    except socket.error:
        return False


# Provide until transition to 1.0
is_fqdn_valid = is_fqdn_resolvable
