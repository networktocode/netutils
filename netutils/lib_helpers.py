"""Helpers to expose network automation library functionality support."""

import inspect
import typing as t

from netutils.lib_mapper import NAPALM_LIB_MAPPER


def get_napalm_getters() -> t.Dict[str, t.Dict[str, bool]]:
    """Utility to return a dictionary of napalm getters based on install napalm version.

    Returns:
        Keys are OS and values are a dictionary of supported napalm getters.

    Raises:
        ImportError: If optional dependency Napalm is not installed.

    Examples:
        >>> from netutils.lib_helpers import get_napalm_getters
        >>> napalm_getters = get_napalm_getters()  # doctest: +SKIP
        >>> napalm_getters["eos"]["get_arp_table"]  # doctest: +SKIP
        >>> True  # doctest: +SKIP
        >>> napalm_getters["eos"]["get_ipv6_neighbors_table"]  # doctest: +SKIP
        >>> False  # doctest: +SKIP
    """
    try:
        # Import NAPALM here at call time, rather than at import time, as importing NAPALM is rather time consuming
        # pylint: disable=import-outside-toplevel
        from napalm import get_network_driver
        from napalm.base.exceptions import ModuleImportError
    except ImportError as err:
        raise ImportError("Napalm must be installed for this function to operate.") from err

    napalm_dict: t.Dict[str, t.Dict[str, bool]] = {}
    oses = NAPALM_LIB_MAPPER.keys()
    for my_os in oses:
        try:
            get_network_driver(my_os)
        except ModuleImportError:
            continue
        napalm_dict[my_os] = {}
        for getter in inspect.getmembers(get_network_driver(my_os), predicate=inspect.isfunction):
            if getter[0].startswith("get_"):
                # If the module is only in the base class it has not been implemented by the child class.
                state = bool(getter[1].__module__ == "napalm.base.base")
                napalm_dict[my_os][getter[0]] = state
    return napalm_dict
