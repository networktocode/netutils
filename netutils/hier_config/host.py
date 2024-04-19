from functools import lru_cache
from typing import List, Set, Union, Optional

import yaml

from netutils.hier_config.root import HConfig
from netutils.hier_config.options import options_for


class Host:
    """
    A host object is a convenient way to loading host inventory
    items into a single object.

    The default is to load "hostname", "os", and "options" to the host object,
    however, it can easily be extended for developer needs.

    .. code:: python

        import yaml
        from hier_config.host import Host

        options = yaml.load(open("./tests/fixtures/options_ios.yml"), loader=yaml.SafeLoader())
        host = Host("example.rtr", "ios", options)

        # Example of loading running config and generated configs into a host object
        host.load_running_config_from_file("./tests/files/running_config.conf)
        host.load_generated_config_from_file("./tests/files/generated_config.conf)

        # Example of loading hier-config tags into a host object
        host.load_tags("./tests/fixtures/tags_ios.yml")

        # Example of creating a remediation config without a tag targeting specific config
        host.remediation_config()

        # Example of creating a remediation config with a tag ("safe") targeting a specific config.
        host.remediation_config_filtered_text({"safe"}, set()})
    """

    def __init__(  # pylint: disable=dangerous-default-value
        self,
        hostname: str,
        os: str,
        hconfig_options: dict = {},
    ):
        self.hostname = hostname
        self.os = os
        self.hconfig_options = hconfig_options if hconfig_options else options_for(self.os)
        self._hconfig_tags: List[dict] = []
        self._running_config: Optional[HConfig] = None
        self._generated_config: Optional[HConfig] = None

    def __repr__(self) -> str:
        return f"Host(hostname={self.hostname})"

    @property
    def running_config(self) -> Optional[HConfig]:
        """running configuration property"""
        if self._running_config is None:
            self._running_config = self._get_running_config()
        return self._running_config

    @property
    def generated_config(self) -> Optional[HConfig]:
        """generated configuration property"""
        if self._generated_config is None:
            self._generated_config = self._get_generated_config()
        return self._generated_config

    @lru_cache()
    def remediation_config(self) -> HConfig:
        """
        Once self.running_config and self.generated_config have been created,
        create self.remediation_config
        """
        if self.running_config and self.generated_config:
            remediation = self.running_config.config_to_get_to(self.generated_config)
        else:
            raise AttributeError("Missing host.running_config or host.generated_config")

        remediation.add_sectional_exiting()
        remediation.set_order_weight()
        remediation.add_tags(self.hconfig_tags)

        return remediation

    @lru_cache()
    def rollback_config(self) -> HConfig:
        """
        Once a self.running_config and self.generated_config have been created,
        generate a self.rollback_config
        """
        if self.running_config and self.generated_config:
            rollback = self.generated_config.config_to_get_to(self.running_config)
        else:
            raise AttributeError("Missing host.running_config or host.generated_config")

        rollback.add_sectional_exiting()
        rollback.set_order_weight()
        rollback.add_tags(self.hconfig_tags)

        return rollback

    @property
    def hconfig_tags(self) -> List[dict]:
        """hier-config tags property"""
        return self._hconfig_tags

    def load_running_config_from_file(self, file: str) -> None:
        config = self._load_from_file(file)
        if not isinstance(config, str):
            raise TypeError
        self.load_running_config(config)

    def load_running_config(self, config_text: str) -> None:
        self._running_config = self._load_config(config_text)

    def load_generated_config_from_file(self, file: str) -> None:
        config = self._load_from_file(file)
        if not isinstance(config, str):
            raise TypeError
        self.load_generated_config(config)

    def load_generated_config(self, config_text: str) -> None:
        self._generated_config = self._load_config(config_text)

    def remediation_config_filtered_text(self, include_tags: Set[str], exclude_tags: Set[str]) -> str:
        config = self.remediation_config()
        if include_tags or exclude_tags:
            children = config.all_children_sorted_by_tags(include_tags, exclude_tags)
        else:
            children = config.all_children_sorted()

        return "\n".join(c.cisco_style_text() for c in children)

    def load_tags(self, tags: list) -> None:
        """
        Loads lineage rules that set tags

        Example:
            Specify to load lineage rules from a dictionary.

        .. code:: python

            tags = [{"lineage": [{"startswith": "interface"}], "add_tags": "interfaces"}]
            host.load_tags(tags)

        :param tags: tags
        """
        self._hconfig_tags = tags

    def load_tags_from_file(self, file: str) -> None:
        tags_from_file = self._load_from_file(file, True)
        if not isinstance(tags_from_file, list):
            raise TypeError
        self.load_tags(tags_from_file)

    def _load_config(self, config_text: str) -> HConfig:
        hier = HConfig(host=self)
        hier.load_from_string(config_text)
        return hier

    @staticmethod
    def _load_from_file(name: str, parse_yaml: bool = False) -> Union[list, dict, str]:
        """Opens a config file and loads it as a string."""
        with open(name) as file:  # pylint: disable=unspecified-encoding
            content = file.read()

        if parse_yaml:
            content = yaml.safe_load(content)

        return content

    def _get_running_config(self) -> HConfig:
        return NotImplemented

    def _get_generated_config(self) -> HConfig:
        return NotImplemented
