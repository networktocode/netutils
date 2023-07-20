"""Configuration conversion methods for different network operating systems."""

import typing as t

from netutils.config.utils import _open_file_config

conversion_map: t.Dict[str, t.List[str]] = {
    "paloalto_panos": ["paloalto_panos_brace_to_set"],
}


def paloalto_panos_brace_to_set(cfg: str, cfg_type: str = "file") -> str:
    r"""Convert Palo Alto Brace format configuration to set format.

    Args:
        cfg: Configuration as a string
        cfg_type: A string that is effectively a choice between `file` and `string`. Defaults to `file`.

    Returns:
        str: Converted configuration as a string.

    Examples:
            >>> config = '''
            ...     config {
            ...            mgt-config {
            ...                users {
            ...                  admin {
            ...                    phash *;
            ...                    permissions {
            ...                      role-based {
            ...                        superuser yes;
            ...                      }
            ...                    }
            ...                    public-key thisisasuperduperlongbase64encodedstring;
            ...                }
            ...                panadmin {
            ...                    permissions {
            ...                      role-based {
            ...                        superuser yes;
            ...                      }
            ...                    }
            ...                    phash passwordhash;
            ...                }
            ...              }
            ...            }
            ...         }'''
            >>> paloalto_panos_brace_to_set(cfg=config, cfg_type='string') == \
            ... '''set mgt-config users admin phash *
            ... set mgt-config users admin permissions role-based superuser yes
            ... set mgt-config users admin public-key thisisasuperduperlongbase64encodedstring
            ... set mgt-config users panadmin permissions role-based superuser yes
            ... set mgt-config users panadmin phash passwordhash'''
            True
    """
    stack: t.List[str] = []
    cfg_value: t.List[str] = []
    cfg_string: str = ""

    if cfg_type not in ["file", "string"]:
        raise ValueError("The variable `cfg_type` must be either `file` or `string`.")
    if cfg_type == "file":
        cfg_list = _open_file_config(cfg).splitlines()
    else:
        cfg_list = cfg.splitlines()

    for i, line in enumerate(cfg_list):
        line = line.strip()
        if line.endswith(";") and not line.endswith('";'):
            line = line.split(";", 1)[0]
            line = "".join(str(s) for s in stack) + line
            line = line.split("config ", 1)[1]
            line = "set " + line
            cfg_value.append(line.strip())
        elif line.endswith('login-banner "') or line.endswith('content "'):
            _first_banner_line = "".join(str(s) for s in stack) + line
            cfg_value.append("set " + _first_banner_line.split("config ", 1)[1])

            for banner_line in cfg_list[i + 1:]:  # fmt: skip
                if '"' in banner_line:
                    banner_line = banner_line.split(";", 1)[0]
                    cfg_value.append(banner_line.strip())
                    break
                cfg_value.append(banner_line.strip())
        elif line.endswith("{"):
            stack.append(line[:-1])
        elif line == "}" and len(stack) > 0:
            stack.pop()

    for _l, _line in enumerate(cfg_value):
        cfg_string += _line
        if _l < len(cfg_value) - 1:
            cfg_string += "\n"

    # Filter out 'devices localhost.local domain' from the entire cfg_string
    # FIXME: Add flagging capability to disable this behavior
    cfg_string = cfg_string.replace("devices localhost.localdomain ", "")

    return cfg_string
