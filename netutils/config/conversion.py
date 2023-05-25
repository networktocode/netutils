"""Configuraiton conversion methods for different network operating systems."""

from typing import Generator, List


def paloalto_panos_brace_to_set(config: Generator[str, None, None]) -> List[str]:
    """Convert Palo Alto Brace/JSON format configuration to set format."""
    stack: List[str] = []
    config_value: List[str] = []

    for line in config:
        line = line.strip()
        if line.endswith(";"):
            line = line.split(";", 1)[0]
            line = "".join(str(s) for s in stack) + line
            line = line.split("config ", 1)[1]
            line = "set " + line
            config_value.append(line.strip())
        elif line.endswith('login-banner "') or line.endswith('content "'):
            _first_banner_line = "".join(str(s) for s in stack) + line
            config_value.append("set " + _first_banner_line.split("config ", 1)[1])

            for _banner_line in config:
                if '"' in _banner_line:
                    _banner_line = _banner_line.split(";", 1)[0]
                    config_value.append(" " + _banner_line.strip())
                    break
                config_value.append(" " + _banner_line)
        elif line.endswith("{"):
            stack.append(line[:-1])
        elif line == "}" and len(stack) > 0:
            stack.pop()

    return config_value
