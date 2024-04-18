"""Functions to create a ping via pure Python."""

import socket


def tcp_ping(ip: str, port: int, timeout: int = 1) -> bool:  # pylint: disable=invalid-name
    """Verifies whether a TCP port is open on a given IP address.

    Args:
        ip: An IP address in string format that is able to be converted by `ipaddress` library.
        port: A valid TCP port.
        timeout: The timeout in seconds before returning a False. Defaults to 1.

    Returns:
        The result as to whether or not you were able ping the IP address.

    Examples:
        >>> from netutils.ping import tcp_ping
        >>> tcp_ping("1.1.1.1", 443)  # doctest: +SKIP
        True
        >>> tcp_ping("1.0.100.0", 27)  # doctest: +SKIP
        False
        >>>
    """
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sckt.settimeout(int(timeout))
    try:
        sckt.connect((ip, int(port)))  # pylint: disable=invalid-name
        sckt.shutdown(socket.SHUT_RDWR)
        return True
    # We really only want to know if the TCP connection timed out.
    # If anything else has happened the error should be raised.
    except socket.timeout:
        return False
    finally:
        sckt.close()
