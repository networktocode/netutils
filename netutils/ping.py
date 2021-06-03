"""Functions to create a ping via pure Python."""
import socket


def tcp_ping(ip, port, timeout=1):  # pylint: disable=invalid-name
    """Verifies whether a TCP port is open on a given IP address.

    Args:
        ip (str): An IP address in string format that is able to be converted by `ipaddress` library.
        port (int): A valid TCP port.
        timeout (int): The timeout in seconds before returning a False. Defaults to 1.

    Returns:
        bool: The result as to whether or not you were able ping the IP address.

    Example:
        >>> from netutils.ping import tcp_ping
        >>> tcp_ping("1.1.1.1", 443)
        True
        >>> tcp_ping("1.0.100.0", 27)
        False
        >>>
    """
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sckt.settimeout(int(timeout))
    try:
        sckt.connect((ip, int(port)))  # pylint: disable=invalid-name
        sckt.shutdown(int(timeout))
        return True
    except socket.error:
        return False
