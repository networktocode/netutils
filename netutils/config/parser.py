"""Parsers for different network operating systems."""

# pylint: disable=no-member,super-with-arguments,invalid-overridden-method,raise-missing-from,invalid-overridden-method,inconsistent-return-statements,super-with-arguments,redefined-argument-from-local,no-else-break,useless-super-delegation,too-many-lines

import re
import typing as t
from collections import namedtuple

from netutils.banner import normalise_delimiter_caret_c
from netutils.config.conversion import paloalto_panos_brace_to_set

ConfigLine = namedtuple("ConfigLine", "config_line,parents")


class BaseConfigParser:
    """Base class for parsers."""

    comment_chars = ["!"]
    banner_start = ["banner", "vacant-message"]

    def __init__(self, config: str):
        """Create ConfigParser Object.

        Args:
            config: The config text to parse.
        """
        self.config = config
        self._config: t.Optional[str] = None
        self._current_parents: t.Tuple[str, ...] = ()
        self.generator_config = (line for line in self.config_lines_only.splitlines())
        self.config_lines: t.List[ConfigLine] = []
        self.build_config_relationship()

    @property
    def config_lines_only(self) -> str:
        """Remove lines not related to config."""
        raise NotImplementedError()

    @property
    def banner_end(self) -> str:
        """Demarcate End of Banner char(s)."""
        raise NotImplementedError()

    def build_config_relationship(self) -> t.List[ConfigLine]:
        """Parse text tree of config lines and their parents."""
        raise NotImplementedError()


class BaseSpaceConfigParser(BaseConfigParser):
    """Base parser class for config syntax that demarcates using spaces/indentation."""

    # TODO: Review if this can be removed
    # pylint: disable=abstract-method

    comment_chars = ["!"]
    banner_start = ["banner", "vacant-message"]

    def __init__(self, config: str):
        """Create ConfigParser Object.

        Args:
            config (str): The config text to parse.
        """
        self._indent_level = 0
        super(BaseSpaceConfigParser, self).__init__(config)

    @property
    def indent_level(self) -> int:
        """Count the number of spaces a config line is indented."""
        return self._indent_level

    @indent_level.setter
    def indent_level(self, value: int) -> None:
        self._indent_level = value

    def is_banner_end(self, line: str) -> bool:
        """Determine if line ends the banner config.

        Args:
            line: The current config line in iteration.

        Returns:
            True if line ends banner, else False.
        """
        if self.banner_end in line:
            return True
        return False

    def is_banner_start(self, line: str) -> bool:
        """Determine if the line starts a banner config.

        Args:
            line: The current config line in iteration.

        Returns:
            True if line starts banner, else False.
        """
        for banner_start in self.banner_start:
            if not line:
                return False
            if line.lstrip().startswith(banner_start):
                return True
        return False

    def is_comment(self, line: str) -> bool:
        """Determine if line is a comment.

        Args:
            line: A config line from the device.

        Returns:
            True if line is a comment, else False.

        Examples:
            >>> from netutils.config.parser import BaseSpaceConfigParser
            >>> BaseSpaceConfigParser("interface Ethernet1/1").is_comment("interface Ethernet1/1")
            False
            >>> BaseSpaceConfigParser("!").is_comment("!")
            True
            >>>
        """
        for comment_char in self.comment_chars:
            if line.lstrip().startswith(comment_char):
                return True
        return False

    @property
    def config_lines_only(self) -> str:
        """Remove spaces and comments from config lines.

        Returns:
            The non-space and non-comment lines from ``config``.

        Examples:
            >>> from netutils.config.parser import BaseSpaceConfigParser
            >>> config = '''!
            ... aaa group server tacacs+ auth
            ...  server 10.1.1.1
            ...  server 10.2.2.2
            ...
            ... !
            ... '''
            >>> config_parser = BaseSpaceConfigParser(config)
            >>> print(config_parser.config_lines_only)
            aaa group server tacacs+ auth
             server 10.1.1.1
             server 10.2.2.2
            >>>
        """
        if self._config is None:
            config_lines = (
                line.rstrip()
                for line in self.config.splitlines()
                if line and not self.is_comment(line) and not line.isspace()
            )
            self._config = "\n".join(config_lines)
        return self._config

    @staticmethod
    def get_leading_space_count(config_line: str) -> int:
        r"""Determine how many spaces the ``config_line`` is indented.

        Args:
           config_line: A line of text in the config.

        Returns:
            The number of leading spaces.

        Examples:
            >>> from netutils.config.parser import BaseSpaceConfigParser
            >>> config = '''interface GigabitEthernet1\n description link to ISP'''
            >>> config_line = " description link to ISP"
            >>> indent_level = BaseSpaceConfigParser(config).get_leading_space_count(config_line)
            >>> indent_level
            1
            >>>
        """
        return len(config_line) - len(config_line.lstrip())

    def _remove_parents(self, line: str, current_spaces: int) -> t.Tuple[str, ...]:
        """Remove parents from ``self._curent_parents`` based on indent levels.

        Args:
            config_line: A line of text in the config.

        Returns:
            The config lines parent config lines.
        """
        deindent_level = 1
        try:
            previous_parent = self._current_parents[-1]
            previous_indent = self.get_leading_space_count(previous_parent)
            while previous_indent > current_spaces:
                deindent_level += 1
                previous_parent = self._current_parents[-deindent_level]
                previous_indent = self.get_leading_space_count(previous_parent)
        except IndexError:
            raise IndexError(f"\nValidate the first line does not begin with a space\n{line}\n")
        parents = self._current_parents[:-deindent_level] or (self._current_parents[0],)
        return parents

    def _build_banner(self, config_line: str) -> t.Optional[str]:
        """Handle banner config lines.

        Args:
            config_line: The start of the banner config.

        Returns:
            The next configuration line in the configuration text or None

        Raises:
            ValueError: When the parser is unable to identify the end of the Banner.
        """
        self._update_config_lines(config_line)
        self._current_parents += (config_line,)
        banner_config = []
        for line in self.generator_config:
            if not self.is_banner_end(line):
                banner_config.append(line)
            else:
                line = normalise_delimiter_caret_c(self.banner_end, line)
                banner_config.append(line)
                line = "\n".join(banner_config)
                if line.endswith("^C"):
                    banner, end, _ = line.rpartition("^C")
                    line = banner.rstrip() + end
                self._update_config_lines(line)
                self._current_parents = self._current_parents[:-1]
                try:
                    return next(self.generator_config)
                except StopIteration:
                    return None

        raise ValueError("Unable to parse banner end.")

    def _build_nested_config(self, line: str) -> t.Optional[str]:
        """Handle building child config sections.

        Args:
            line: A configuration line from the configuration text.

        Returns:
            The next top-level configuration line in the configuration text or None when the last line of configuration
            text is a nested configuration line.

        Raises:
            IndexError: When the number of parents does not match the expected deindent level.
        """
        self._update_config_lines(line)
        for line in self.generator_config:
            if not line[0].isspace():
                self._current_parents = ()
                self.indent_level = 0
                return line

            spaces = self.get_leading_space_count(line)
            if spaces == self.indent_level:
                pass
            elif spaces > self.indent_level:
                previous_config = self.config_lines[-1]
                self._current_parents += (previous_config.config_line,)
            else:
                self._current_parents = self._remove_parents(line, spaces)

            if spaces != self.indent_level:
                self.indent_level = spaces

            if self.is_banner_start(line):
                banner_line = self._build_banner(line)
                if banner_line is None or not banner_line[0].isspace():
                    self._current_parents = ()
                    self.indent_level = 0
                    return banner_line
                line = banner_line

            self._update_config_lines(line)
        return None

    def _update_config_lines(self, config_line: str) -> None:
        """Add a ``ConfigLine`` object to ``self.config_lines``.

        Args:
            config_line: The current config line being evaluated.

        Returns:
            None
        """
        entry = ConfigLine(config_line, self._current_parents)
        self.config_lines.append(entry)

    def build_config_relationship(self) -> t.List[ConfigLine]:
        r"""Parse text tree of config lines and their parents.

        Examples:
            >>> from netutils.config.parser import BaseSpaceConfigParser, ConfigLine
            >>> config = (
            ...     "interface Ethernet1/1\n"
            ...     "  vlan 10\n"
            ...     "  no shutdown\n"
            ...     "interface Ethernet1/2\n"
            ...     "  shutdown\n"
            ... )
            >>> config_tree = BaseSpaceConfigParser(config)
            >>> config_tree.build_config_relationship() == \
            ... [
            ...     ConfigLine(config_line='interface Ethernet1/1', parents=()),
            ...     ConfigLine(config_line='  vlan 10', parents=('interface Ethernet1/1',)),
            ...     ConfigLine(config_line='  no shutdown', parents=('interface Ethernet1/1',)),
            ...     ConfigLine(config_line='interface Ethernet1/2', parents=(),),
            ...     ConfigLine(config_line='  shutdown', parents=('interface Ethernet1/2',))
            ... ]
            True
        """
        for line in self.generator_config:
            if not line[0].isspace():
                self._current_parents = ()
                if self.is_banner_start(line):
                    line = self._build_banner(line)  # type: ignore
            else:
                previous_config = self.config_lines[-1]
                self._current_parents = (previous_config.config_line,)
                self.indent_level = self.get_leading_space_count(line)
                if not self.is_banner_start(line):
                    line = self._build_nested_config(line)  # type: ignore
                else:
                    line = self._build_banner(line)  # type: ignore
                    if line is not None and line[0].isspace():
                        line = self._build_nested_config(line)  # type: ignore
                    else:
                        self._current_parents = ()

            if line is None:
                break
            elif self.is_banner_start(line):
                line = self._build_banner(line)  # type: ignore
                # line can potentially be another banner start therefore we do a secondary check.
                if self.is_banner_start(line):
                    line = self._build_banner(line)  # type: ignore

            self._update_config_lines(line)
        return self.config_lines

    @staticmethod
    def _match_type_check(line: str, pattern: str, match_type: str) -> bool:
        """Checks pattern for exact match or regex."""
        if match_type == "exact" and line == pattern:
            return True
        if match_type == "startswith" and line.startswith(pattern):
            return True
        if match_type == "endswith" and line.endswith(pattern):
            return True
        if match_type == "regex" and re.match(pattern, line):
            return True
        return False

    def find_all_children(self, pattern: str, match_type: str = "exact") -> t.List[str]:
        """Returns configuration part for a specific pattern not including parents.

        Args:
            pattern: pattern that describes parent.
            match_type (optional): Exact or regex. Defaults to "exact".

        Returns:
            configuration under that parent pattern.

        Examples:
            >>> from netutils.config.parser import BaseSpaceConfigParser
            >>> config = '''
            ... router bgp 45000
            ...   address-family ipv4 unicast
            ...    neighbor 192.168.1.2 activate
            ...    network 172.17.1.0 mask'''
            >>> bgp_conf = BaseSpaceConfigParser(str(config)).find_all_children(pattern="router bgp", match_type="startswith")
            >>> print(bgp_conf)
            ['router bgp 45000', '  address-family ipv4 unicast', '   neighbor 192.168.1.2 activate', '   network 172.17.1.0 mask']
        """
        config = []
        for cfg_line in self.build_config_relationship():
            parents = cfg_line.parents[0] if cfg_line.parents else None
            if (
                parents
                and self._match_type_check(parents, pattern, match_type)
                or self._match_type_check(cfg_line.config_line, pattern, match_type)
            ):
                config.append(cfg_line.config_line)
        return config

    def find_children_w_parents(
        self, parent_pattern: str, child_pattern: str, match_type: str = "exact"
    ) -> t.List[str]:
        """Returns configuration part for a specific pattern including parents and children.

        Args:
            parent_pattern: pattern that describes parent.
            child_pattern: pattern that describes child.
            match_type (optional): Exact or regex. Defaults to "exact".

        Returns:
            configuration under that parent pattern.

        Examples:
            >>> from netutils.config.parser import BaseSpaceConfigParser
            >>> config = '''
            ... router bgp 45000
            ...   address-family ipv4 unicast
            ...    neighbor 192.168.1.2 activate
            ...    network 172.17.1.0 mask'''
            >>> bgp_conf = BaseSpaceConfigParser(str(config)).find_children_w_parents(parent_pattern="router bgp", child_pattern="  address-family", match_type="regex")
            >>> print(bgp_conf)
            ['  address-family ipv4 unicast', '   neighbor 192.168.1.2 activate', '   network 172.17.1.0 mask']
        """
        config = []
        potential_parents = [
            elem.parents[0]
            for elem in self.build_config_relationship()
            if self._match_type_check(elem.config_line, child_pattern, match_type)
        ]
        for cfg_line in self.build_config_relationship():
            parents = cfg_line.parents[0] if cfg_line.parents else None
            if parents in potential_parents and self._match_type_check(parents, parent_pattern, match_type):
                config.append(cfg_line.config_line)
        return config


class BaseBraceConfigParser(BaseConfigParser):  # pylint: disable=abstract-method
    """Base parser class for config syntax that demarcates using braces."""

    multiline_delimiters: t.List[str] = []

    @property
    def config_lines_only(self) -> str:
        """Remove trailing spaces and empty lines from config lines.

        Returns:
            The non-space lines from ``config``.
        """
        config_lines = [line.rstrip() for line in self.config.splitlines() if line and not line.isspace()]
        return "\n".join(config_lines)

    def build_config_relationship(self) -> t.List[ConfigLine]:
        r"""Parse text tree of config lines and their parents.

        Examples:
            >>> from netutils.config.parser import BaseSpaceConfigParser, ConfigLine
            >>> config = '''auth ldap system-auth {
            ...         port ldaps
            ...         servers { ams-lda01.ntc.com }
            ...     }
            ...     auth partition Common {
            ...         description "Repository for system objects and shared objects."
            ...     }
            ...     auth password-policy { }'''
            >>> config_tree = BaseBraceConfigParser(config)
            >>> config_tree.build_config_relationship() == \
            ... [
            ...     ConfigLine(config_line='auth ldap system-auth {', parents=()),
            ...     ConfigLine(config_line='        port ldaps', parents=('auth ldap system-auth {',)),
            ...     ConfigLine(config_line='        servers { ams-lda01.ntc.com }', parents=('auth ldap system-auth {',)),
            ...     ConfigLine(config_line='    }', parents=('auth ldap system-auth {',)),
            ...     ConfigLine(config_line='    auth partition Common {', parents=()),
            ...     ConfigLine(config_line='        description "Repository for system objects and shared objects."', parents=('    auth partition Common {',)), ConfigLine(config_line='    }', parents=('    auth partition Common {',)),
            ...     ConfigLine(config_line='    auth password-policy { }', parents=())
            ... ]
            True
        """
        for line in self.generator_config:
            self.config_lines.append(ConfigLine(line, self._current_parents))
            line_end = line[-1]
            if line.endswith("{"):
                self._current_parents += (line,)
            elif line.lstrip() == "}":
                self._current_parents = self._current_parents[:-1]
            elif line_end in self.multiline_delimiters and line.count(line_end) == 1:
                self._current_parents += (line,)
                self._build_multiline_config(line_end)

        return self.config_lines

    def _build_multiline_config(self, delimiter: str) -> t.Optional[ConfigLine]:
        r"""Build config sections between characters demarcating multiline strings.

        Args:
            delimiter: The text to look for to end multiline config.

        Returns:
            The multiline string text that was added to ``self.config_lines``.

        Examples:
            >>> from netutils.config.parser import BaseSpaceConfigParser, ConfigLine
            >>> config = (
            ...     'sys syslog {\n'
            ...     '    include "\n'
            ...     '        filter f_local0 {\n'
            ...     '        facility(local0) and not match(\"DEBUG");\n'
            ...     '    "\n'
            ...     '}'
            ... )
            >>> parser = BaseBraceConfigParser(config)
            >>> # '    include "' started a multiline config
            >>> parser.config_lines == \
            ... [
            ...     ConfigLine(config_line='sys syslog {', parents=()),
            ...     ConfigLine(config_line='    include "', parents=('sys syslog {',)),
            ...     ConfigLine(config_line='        filter f_local0 {', parents=('sys syslog {',)),
            ...     ConfigLine(config_line='        facility(local0) and not match("DEBUG");', parents=('sys syslog {', '        filter f_local0 {')),
            ...     ConfigLine(config_line='    "', parents=('sys syslog {', '        filter f_local0 {')),
            ...     ConfigLine(config_line='}', parents=('sys syslog {', '        filter f_local0 {'))
            ... ]
            True
        """
        multiline_config = []
        for line in self.generator_config:
            multiline_config.append(line)
            if line.lstrip() == delimiter:
                multiline_entry = ConfigLine("\n".join(multiline_config), self._current_parents)
                self.config_lines.append(multiline_entry)
                self._current_parents = self._current_parents[:-1]
                return multiline_entry
        return None


class CiscoConfigParser(BaseSpaceConfigParser):
    """Cisco Implementation of ConfigParser Class."""

    regex_banner = re.compile(r"^(banner\s+\S+|\s*vacant-message)\s+(?P<banner_delimiter>\^C|.)")

    def __init__(self, config: str):
        """Create ConfigParser Object.

        Args:
            config (str): The config text to parse.
        """
        self._banner_end: t.Optional[str] = None
        super(CiscoConfigParser, self).__init__(config)

    def _build_banner(self, config_line: str) -> t.Optional[str]:
        """Handle banner config lines.

        Args:
            config_line: The start of the banner config.

        Returns:
            The next configuration line in the configuration text or None when banner end is the end of the config text.

        Raises:
            ValueError: When the parser is unable to identify the End of the Banner.
        """
        if self.is_banner_one_line(config_line):
            self._update_config_lines(config_line)
            try:
                return next(self.generator_config)
            except StopIteration:
                return None
        return super(CiscoConfigParser, self)._build_banner(config_line)

    @staticmethod
    def is_banner_one_line(config_line: str) -> bool:
        """Determine if all banner config is on one line."""
        _, delimeter, banner = config_line.partition("^C")
        # if the banner is the delimeter is a single line empty banner. e.g banner motd ^C^C which ios allows.
        if banner == "^C":
            return True
        # Based on NXOS configs, the banner delimeter is ignored until another char is used
        banner_config_start = banner.lstrip(delimeter)
        if delimeter not in banner_config_start:
            return False
        return True

    def is_banner_start(self, line: str) -> bool:
        """Determine if the line starts a banner config."""
        state = super(CiscoConfigParser, self).is_banner_start(line)
        if state:
            self.banner_end = line
        return state

    @property
    def banner_end(self) -> str:
        """Demarcate End of Banner char(s)."""
        if self._banner_end is None:
            raise RuntimeError("Banner end not yet set.")
        return self._banner_end

    @banner_end.setter
    def banner_end(self, banner_start_line: str) -> None:
        banner_parsed = self.regex_banner.match(banner_start_line)
        if not banner_parsed:
            raise ValueError("There was an error parsing your banner, the end of the banner could not be found")
        self._banner_end = banner_parsed.groupdict()["banner_delimiter"]


class IOSConfigParser(CiscoConfigParser, BaseSpaceConfigParser):
    """Cisco IOS implementation of ConfigParser Class."""

    def __init__(self, config: str):
        """Create ConfigParser Object.

        Args:
            config (str): The config text to parse.
        """
        self.unique_config_lines: t.Set[ConfigLine] = set()
        self.same_line_children: t.Set[ConfigLine] = set()
        super(IOSConfigParser, self).__init__(config)

    def _build_banner(self, config_line: str) -> t.Optional[str]:
        """Handle banner config lines.

        Args:
            config_line: The start of the banner config.

        Returns:
            The next configuration line in the configuration text or None when banner end is the end of the config text.

        Raises:
            ValueError: When the parser is unable to identify the End of the Banner.
        """
        config_line = normalise_delimiter_caret_c(self.banner_end, config_line)
        return super(IOSConfigParser, self)._build_banner(config_line)

    def _update_same_line_children_configs(self) -> None:
        """Update parents in ``self.config_lines`` per ``self.same_line_children``."""
        new_config_lines: t.List[ConfigLine] = []
        for line in self.config_lines:
            if line in self.same_line_children:
                previous_line = new_config_lines[-1]
                previous_config_line = previous_line.config_line
                current_parents = previous_line.parents + (previous_config_line,)
                line = ConfigLine(line.config_line, current_parents)
            new_config_lines.append(line)
        self.config_lines = new_config_lines

    def _update_config_lines(self, config_line: str) -> None:
        """Add a ``ConfigLine`` object to ``self.config_lines``.

        In addition to adding entries to config_lines, this also updates:
          * self.same_line_children
          * self.unique_config_lines

        Args:
            config_line: The current config line being evaluated.

        Returns:
            None
        """
        super(IOSConfigParser, self)._update_config_lines(config_line)
        entry = self.config_lines[-1]
        if entry in self.unique_config_lines:
            self.same_line_children.add(entry)
        self.unique_config_lines.add(entry)

    def build_config_relationship(self) -> t.List[ConfigLine]:
        r"""Parse text tree of config lines and their parents.

        Examples:
            >>> from netutils.config.parser import IOSConfigParser, ConfigLine
            >>> config = '''
            ... interface Ethernet1/1
            ...   vlan 10
            ...   no shutdown
            ... interface Ethernet1/2
            ...   shutdown'''
            >>> config_tree = IOSConfigParser(str(config))
            >>> config_tree.build_config_relationship() == \
            ... [
            ...     ConfigLine(config_line='interface Ethernet1/1', parents=()),
            ...     ConfigLine(config_line='  vlan 10', parents=('interface Ethernet1/1',)),
            ...     ConfigLine(config_line='  no shutdown', parents=('interface Ethernet1/1',)),
            ...     ConfigLine(config_line='interface Ethernet1/2', parents=()),
            ...     ConfigLine(config_line='  shutdown', parents=('interface Ethernet1/2',))
            ... ]
            True
        """
        super(IOSConfigParser, self).build_config_relationship()
        self._update_same_line_children_configs()
        return self.config_lines


class NXOSConfigParser(CiscoConfigParser, BaseSpaceConfigParser):
    """NXOS implementation of ConfigParser Class."""

    regex_banner = re.compile(r"^banner\s+\S+\s+(?P<banner_delimiter>\S)")

    def __init__(self, config: str):
        """Create ConfigParser Object.

        Args:
            config (str): The config text to parse.
        """
        self.unique_config_lines: t.Set[ConfigLine] = set()
        self.same_line_children: t.Set[ConfigLine] = set()
        super(NXOSConfigParser, self).__init__(config)

    def _build_banner(self, config_line: str) -> t.Optional[str]:
        """Handle banner config lines.

        Args:
            config_line: The start of the banner config.

        Returns:
            The next configuration line in the configuration text or None when banner end is the end of the config text.

        Raises:
            ValueError: When the parser is unable to identify the end of the Banner.
        """
        config_line = normalise_delimiter_caret_c(self.banner_end, config_line)
        return super(NXOSConfigParser, self)._build_banner(config_line)


class EOSConfigParser(BaseSpaceConfigParser):
    """EOSConfigParser implementation fo ConfigParser Class."""

    banner_end = "EOF"

    def _build_banner(self, config_line: str) -> t.Optional[str]:
        """Handle banner config lines.

        Args:
            config_line: The start of the banner config.

        Returns:
            The next configuration line in the configuration text or None when banner end is the end of the config text.

        Raises:
            ValueError: When the parser is unable to identify the End of the Banner.
        """
        self._update_config_lines(config_line)
        self._current_parents += (config_line,)
        banner_config = []
        for line in self.generator_config:
            if not self.is_banner_end(line):
                banner_config.append(line)
            else:
                banner_config.append(line)
                line = "\n".join(banner_config)
                self._update_config_lines(line)
                self._current_parents = self._current_parents[:-1]
                try:
                    return next(self.generator_config)
                except StopIteration:
                    return None
        raise ValueError("Unable to parse banner end.")


class AIREOSConfigParser(CiscoConfigParser, BaseSpaceConfigParser):
    """AireOSConfigParser implementation fo ConfigParser Class."""

    banner_start: t.List[str] = []

    def _build_banner(self, config_line: str) -> None:
        raise NotImplementedError()


class LINUXConfigParser(BaseSpaceConfigParser):
    """Linux config parser."""

    comment_chars: t.List[str] = ["#"]

    @property
    def banner_end(self) -> str:
        """Demarcate End of Banner char(s)."""
        raise NotImplementedError("Linux platform doesn't have a banner.")


class F5ConfigParser(BaseBraceConfigParser):
    """F5ConfigParser implementation for ConfigParser Class."""

    multiline_delimiters: t.List[str] = ['"']

    @property
    def banner_end(self) -> str:
        """Demarcate End of Banner char(s)."""
        raise NotImplementedError("F5 platform doesn't have a banner.")

    def __init__(self, config: str):
        """Create ConfigParser Object.

        Args:
            config: The config text to parse.
        """
        super().__init__(self._clean_config_f5(config))

    def _clean_config_f5(self, config_text: str) -> str:
        """Removes all configuration items with 'ltm rule'.

        iRules are essentially impossible to parse with the lack of uniformity,
        therefore, this method ensures they are not included in ``self.config``.

        Args:
            config_text: The entire config as a string.

        Returns:
            The sanitized config with all iRules (ltm rule) stanzas removed.
        """
        config_split = config_text.split("ltm rule")
        if len(config_split) > 1:
            start_config = config_split[0]
            end_config = config_split[-1]
            _, ltm, clean_config = end_config.partition("ltm")
            final_config = start_config + ltm + clean_config
        else:
            final_config = config_text
        return final_config

    def build_config_relationship(self) -> t.List[ConfigLine]:
        r"""Parse text tree of config lines and their parents.

        Examples:
            >>> from netutils.config.parser import F5ConfigParser, ConfigLine
            >>> config = '''apm resource webtop-link aShare {
            ...     application-uri http://funshare.example.com
            ...     customization-group a_customization_group
            ... }
            ... apm sso form-based portal_ext_sso_form_based {
            ...     form-action /Citrix/Example/ExplicitAuth/LoginAttempt
            ...     form-field "LoginBtn Log+On
            ... StateContext "
            ...     form-password password
            ...     form-username username
            ...     passthru true
            ...     start-uri /Citrix/Example/ExplicitAuth/Login*
            ...     success-match-type cookie
            ...     success-match-value CtxsAuthId
            ... }
            ... '''
            >>>
            >>> config_tree = F5ConfigParser(config)
            >>> print(config_tree.build_config_relationship())
            [ConfigLine(config_line='apm resource webtop-link aShare {', parents=()), ConfigLine(config_line='    application-uri http://funshare.example.com', parents=('apm resource webtop-link aShare {',)), ConfigLine(config_line='    customization-group a_customization_group', parents=('apm resource webtop-link aShare {',)), ConfigLine(config_line='}', parents=('apm resource webtop-link aShare {',)), ConfigLine(config_line='apm sso form-based portal_ext_sso_form_based {', parents=()), ConfigLine(config_line='    form-action /Citrix/Example/ExplicitAuth/LoginAttempt', parents=('apm sso form-based portal_ext_sso_form_based {',)), ConfigLine(config_line='    form-field "LoginBtn Log+On\nStateContext "', parents=('apm sso form-based portal_ext_sso_form_based {',)), ConfigLine(config_line='    form-password password', parents=()), ConfigLine(config_line='    form-username username', parents=()), ConfigLine(config_line='    passthru true', parents=()), ConfigLine(config_line='    start-uri /Citrix/Example/ExplicitAuth/Login*', parents=()), ConfigLine(config_line='    success-match-type cookie', parents=()), ConfigLine(config_line='    success-match-value CtxsAuthId', parents=()), ConfigLine(config_line='}', parents=())]
        """
        for line in self.generator_config:
            self.config_lines.append(ConfigLine(line, self._current_parents))
            line_end = line[-1]
            if line.endswith("{"):
                self._current_parents += (line,)
            elif line.lstrip() == "}":
                self._current_parents = self._current_parents[:-1]
            elif any(
                delimiters in self.multiline_delimiters and line.count(delimiters) == 1
                for delimiters in self.multiline_delimiters
            ):
                for delimiter in self.multiline_delimiters:
                    if line.count(delimiter) == 1:
                        self._build_multiline_single_configuration_line(delimiter, line)
            elif line_end in self.multiline_delimiters and line.count(line_end) == 1:
                self._current_parents += (line,)
                self._build_multiline_config(line_end)

        return self.config_lines

    def _build_multiline_single_configuration_line(self, delimiter: str, prev_line: str) -> t.Optional[ConfigLine]:
        r"""Concatenate Multiline strings between delimiter when newlines causes string to traverse multiple lines.

        Args:
            delimiter: The text to look for to end multiline config.
            prev_line: The text from the previously analyzed line.

        Returns:
            The multiline string text that was added to ``self.config_lines``.

        Examples:
            >>> from netutils.config.parser import F5ConfigParser, ConfigLine
            >>> config = '''apm resource webtop-link aShare {
            ...     application-uri http://funshare.example.com
            ...     customization-group a_customization_group
            ... }
            ... apm sso form-based portal_ext_sso_form_based {
            ...     form-action /Citrix/Example/ExplicitAuth/LoginAttempt
            ...     form-field "LoginBtn Log+On
            ... StateContext "
            ...     form-password password
            ...     form-username username
            ...     passthru true
            ...     start-uri /Citrix/Example/ExplicitAuth/Login*
            ...     success-match-type cookie
            ...     success-match-value CtxsAuthId
            ... }
            ... '''
            >>>
            >>>
            >>> config_tree = F5ConfigParser(str(config))
            >>> print(config_tree.build_config_relationship())
            [ConfigLine(config_line='apm resource webtop-link aShare {', parents=()), ConfigLine(config_line='    application-uri http://funshare.example.com', parents=('apm resource webtop-link aShare {',)), ConfigLine(config_line='    customization-group a_customization_group', parents=('apm resource webtop-link aShare {',)), ConfigLine(config_line='}', parents=('apm resource webtop-link aShare {',)), ConfigLine(config_line='apm sso form-based portal_ext_sso_form_based {', parents=()), ConfigLine(config_line='    form-action /Citrix/Example/ExplicitAuth/LoginAttempt', parents=('apm sso form-based portal_ext_sso_form_based {',)), ConfigLine(config_line='    form-field "LoginBtn Log+On\nStateContext "', parents=('apm sso form-based portal_ext_sso_form_based {',)), ConfigLine(config_line='    form-password password', parents=()), ConfigLine(config_line='    form-username username', parents=()), ConfigLine(config_line='    passthru true', parents=()), ConfigLine(config_line='    start-uri /Citrix/Example/ExplicitAuth/Login*', parents=()), ConfigLine(config_line='    success-match-type cookie', parents=()), ConfigLine(config_line='    success-match-value CtxsAuthId', parents=()), ConfigLine(config_line='}', parents=())]
        """
        multiline_config = [prev_line]
        for line in self.generator_config:
            multiline_config.append(line)
            if line.endswith(delimiter):
                multiline_entry = ConfigLine("\n".join(multiline_config), self._current_parents)
                self.config_lines[-1] = multiline_entry
                self._current_parents = self._current_parents[:-1]
                return multiline_entry
        return None


class JunosConfigParser(BaseSpaceConfigParser):
    """Junos config parser."""

    comment_chars: t.List[str] = []
    banner_start: t.List[str] = []

    @property
    def banner_end(self) -> str:
        """Demarcate End of Banner char(s)."""
        raise NotImplementedError("Junos platform doesn't have a banner.")


class ASAConfigParser(CiscoConfigParser):
    """Cisco ASA implementation of ConfigParser Class."""

    comment_chars: t.List[str] = ["!", ":"]

    def __init__(self, config: str):
        """Create ConfigParser Object.

        Args:
            config: The config text to parse.
        """
        self.unique_config_lines: t.Set[ConfigLine] = set()
        self.same_line_children: t.Set[ConfigLine] = set()
        super(ASAConfigParser, self).__init__(config)

    def _update_config_lines(self, config_line: str) -> None:
        """Add a ``ConfigLine`` object to ``self.config_lines``.

        In addition to adding entries to config_lines, this also updates:
          * self.same_line_children
          * self.unique_config_lines

        Args:
            config_line (str): The current config line being evaluated.

        Returns:
            None
        """
        super(ASAConfigParser, self)._update_config_lines(config_line)
        entry = self.config_lines[-1]
        if entry in self.unique_config_lines:
            self.same_line_children.add(entry)
        self.unique_config_lines.add(entry)

    def build_config_relationship(self) -> t.List[ConfigLine]:
        r"""Parse text tree of config lines and their parents.

        Examples:
            >>> from netutils.config.parser import ASAConfigParser, ConfigLine
            >>> config = '''
            ... interface Management0/0
            ...  management-only
            ...  nameif Management
            ...  security-level 100
            ...  ip address 10.1.1.10 255.255.255.0'''
            >>> config_tree = ASAConfigParser(str(config))
            >>> config_tree.build_config_relationship() == \
            ... [
            ...     ConfigLine(config_line="interface Management0/0", parents=()),
            ...     ConfigLine(config_line=" management-only", parents=("interface Management0/0",)),
            ...     ConfigLine(config_line=" nameif Management", parents=("interface Management0/0",)),
            ...     ConfigLine(config_line=" security-level 100", parents=("interface Management0/0",)),
            ...     ConfigLine(config_line=" ip address 10.1.1.10 255.255.255.0", parents=("interface Management0/0",)),
            ... ]
            True
        """
        for line in self.generator_config:
            if not line[0].isspace():
                self._current_parents = ()
            else:
                previous_config = self.config_lines[-1]
                self._current_parents = (previous_config.config_line,)
                self.indent_level = self.get_leading_space_count(line)
                if line is not None and line[0].isspace():
                    line = self._build_nested_config(line)  # type: ignore
                else:
                    self._current_parents = ()

            if line is None:
                break

            self._update_config_lines(line)

        return self.config_lines


class FortinetConfigParser(BaseSpaceConfigParser):
    """Fortinet Fortios config parser."""

    comment_chars: t.List[str] = []
    banner_start: t.List[str] = []

    @property
    def banner_end(self) -> str:
        """Demarcate End of Banner char(s)."""
        raise NotImplementedError("Fortinet FortiOS platform doesn't have a banner.")

    def __init__(self, config: str):
        """Create ConfigParser Object.

        Args:
            config (str): The config text to parse.
        """
        self.uncommon_data = self._get_uncommon_lines(config)
        super(FortinetConfigParser, self).__init__(config)

    def is_end_next(self, line: str) -> bool:
        """Determine if line has 'end' or 'next' in it.

        Args:
            line: A config line from the device.

        Returns:
            True if line has 'end' or 'next', else False.

        Examples:
            >>> from netutils.config.parser import FortinetConfigParser
            >>> FortinetConfigParser("config system virtual-switch").is_end_next("config system virtual-switch")
            False
            >>> FortinetConfigParser("end").is_end_next("end")
            True
            >>>
        """
        for end_next in ["end", "next"]:
            if line.lstrip() == end_next:
                return True
        return False

    def _parse_out_offending(self, config: str) -> str:
        """Preprocess out strings that offend the normal spaced configuration syntax.

        Args:
            config (str): full config as a string.
        """
        # This will grab everything between quotes after the 'set buffer' sub-command.
        # Its explicitly looking for "\n to end the captured data.  This is to support html
        # data that is supported in Fortinet config with double quotes within the html.
        pattern = r"(config system replacemsg.*(\".*\")\n)(\s{4}set\sbuffer\s\"[\S\s]*?\"\n)"
        return re.sub(pattern, r"\1    [\2]\n", config)

    @property
    def config_lines_only(self) -> str:
        """Remove spaces and comments from config lines.

        Returns:
            The non-space and non-comment lines from ``config``.
        """
        # Specific to fortinet to remove uncommon data patterns for use later in _build_nested_config.
        self.config = self._parse_out_offending(self.config)
        if self._config is None:
            config_lines = (
                line.rstrip()
                for line in self.config.splitlines()
                if line and not self.is_comment(line) and not line.isspace() and not self.is_end_next(line)
            )
            self._config = "\n".join(config_lines)
        return self._config

    def _get_uncommon_lines(self, config: str) -> t.Dict[str, str]:
        """Regex to find replacemsg lines which can contain html/css data.

        Args:
            config: Original config before parsing.

        Returns:
            dict: dictionary with replace message name as key, html/css data as value.
        """
        pattern = r"(config system replacemsg.*\n)(\s{4}set\sbuffer\s\"[\S\s]*?\"\n)"
        regex_result = re.findall(pattern, config)
        result = {}
        for group_match in regex_result:
            result.update({group_match[0].split('"')[1]: group_match[1]})
        return result

    def _build_nested_config(self, line: str) -> t.Optional[str]:
        """Handle building child config sections.

        Args:
            line: A configuration line from the configuration text.

        Returns:
            The next top-level configuration line in the configuration text or None when the last line of configuration
            text is a nested configuration line.

        Raises:
            IndexError: When the number of parents does not match the expected deindent level.
        """
        if "[" in line:
            updated_line = self.uncommon_data.get(line.split('"')[1], None)
            if not updated_line:
                raise ValueError("Input line is malformed.")
            line = updated_line
        self._update_config_lines(line)
        for line in self.generator_config:
            if not line[0].isspace():
                self._current_parents = ()
                self.indent_level = 0
                return line

            spaces = self.get_leading_space_count(line)
            if spaces == self.indent_level:
                pass
            elif spaces > self.indent_level:
                previous_config = self.config_lines[-1]
                self._current_parents += (previous_config.config_line,)
            else:
                self._current_parents = self._remove_parents(line, spaces)

            if spaces != self.indent_level:
                self.indent_level = spaces

            self._update_config_lines(line)
        return None


class NokiaConfigParser(BaseSpaceConfigParser):
    """Nokia SrOS config parser."""

    comment_chars: t.List[str] = ["#"]
    banner_start: t.List[str] = []

    @property
    def banner_end(self) -> str:
        """Demarcate End of Banner char(s)."""
        raise NotImplementedError("Nokia SROS platform doesn't have a banner.")

    def _is_section_title(self, line: str) -> bool:
        """Determine if line is a section title in banner.

        Args:
            line: A config line from the device.

        Returns:
            True if line is a section, else False.
        """
        if re.match(r"^echo\s\".+\"", string=line):
            return True
        return False

    def _get_section_title(self, line: str) -> t.Union[str, bool]:
        """Determine section title from banner.

        Args:
            line: A config line from the device that has been found to be a section title.

        Returns:
            The section's title from the section banner, else False.
        """
        section_title = re.match(r"^echo\s\"(?P<section_name>.+)\"", string=line)
        if section_title:
            return section_title.group("section_name")
        return False

    @property
    def config_lines_only(self) -> str:
        """Remove spaces and comments from config lines.

        Returns:
            The non-space and non-comment lines from ``config``.
        """
        if self._config is None:
            config_lines = []
            for line in self.config.splitlines():
                if line and not self.is_comment(line) and not line.isspace():
                    if self._is_section_title(line):
                        section_title = self._get_section_title(line)
                        # At this point it is safe to assume that self._get_section_title returns a string, not a bool.
                        # The following line passes this assumption to Mypy.
                        assert isinstance(section_title, str)  # nosec
                        config_lines.append(section_title)
                    else:
                        config_lines.append(line.rstrip())
            self._config = "\n".join(config_lines)
        return self._config


class NetscalerConfigParser(BaseSpaceConfigParser):
    """Netscaler config parser."""

    comment_chars: t.List[str] = []
    banner_start: t.List[str] = []

    @property
    def banner_end(self) -> str:
        """Demarcate End of Banner char(s)."""
        raise NotImplementedError("Netscaler platform doesn't have a banner.")


class ArubaConfigParser(BaseSpaceConfigParser):
    """Aruba AOS-CX implementation fo ConfigParser Class."""

    banner_end = "!"
    comment_chars = ["!"]

    def _build_banner(self, config_line: str) -> t.Optional[str]:
        """Handle banner config lines.

        Args:
            config_line: The start of the banner config.

        Returns:
            The next configuration line in the configuration text or None when banner end is the end of the config text.

        Raises:
            ValueError: When the parser is unable to identify the End of the Banner.
        """
        self._update_config_lines(config_line)
        self._current_parents += (config_line,)
        banner_config = []
        for line in self.generator_config:
            if not self.is_banner_end(line):
                banner_config.append(line)
            else:
                banner_config.append(line)
                line = "\n".join(banner_config)
                self._update_config_lines(line)
                self._current_parents = self._current_parents[:-1]
                try:
                    return next(self.generator_config)
                except StopIteration:
                    return None
        raise ValueError("Unable to parse banner end.")

    def _parse_out_comments(self, config: str) -> str:
        """Remove comments while retaining the banner end.

        Args:
            config (str): full config as a string.

        Returns:
            The non-comment lines from ``config``.
        """
        # Aruba AOS-CX uses "!" as both comments and the banner delimiter.
        # Even if another delimiter is used while creating the banner, show run changes the delimiter to use "!".
        # We need to remove comments while retaining the banner delimiter.

        config_lines = []
        banner_started = False
        banner_ended = False
        for line in config.splitlines():
            if self.is_banner_start(line):
                banner_started = True
                banner_ended = False
            if line and banner_started and not banner_ended:
                config_lines.append(line.rstrip())
                if line.lstrip().startswith(self.banner_end):
                    banner_ended = True
                    banner_started = False
            else:
                if line and not self.is_comment(line):
                    config_lines.append(line.rstrip())
        full_config = "\n".join(config_lines)
        return full_config

    @property
    def config_lines_only(self) -> str:
        """Remove spaces and unwanted lines from config lines.

        Returns:
            The non-space and non-comment lines from ``config``.
        """
        if self._config is None:
            config_lines = []
            for line in self.config.splitlines():
                if line and not line.isspace():
                    config_lines.append(line.rstrip())
            self._config = self._parse_out_comments("\n".join(config_lines))
        return self._config


class IOSXRConfigParser(CiscoConfigParser):
    """IOS-XR config parser."""

    comment_chars: t.List[str] = ["!"]
    banner_start: t.List[str] = ["banner "]

    regex_banner = re.compile(r"^banner\s+\S+\s+(?P<banner_delimiter>\S)")

    def __init__(self, config: str):
        """Create ConfigParser Object.

        Args:
            config (str): The config text to parse.
        """
        self.delimiter = ""
        super(IOSXRConfigParser, self).__init__(config)

    def _build_banner(self, config_line: str) -> t.Optional[str]:
        """Handle banner config lines.

        Args:
            config_line: The start of the banner config.

        Returns:
            The next configuration line in the configuration text or None

        Raises:
            ValueError: When the parser is unable to identify the end of the Banner.
        """
        self._update_config_lines(config_line)
        self._current_parents += (config_line,)
        banner_config = []
        for line in self.generator_config:
            if not self.is_banner_end(line):
                banner_config.append(line)
            else:
                banner_config.append(line)
                line = "\n".join(banner_config)
                if line.endswith(self.delimiter):
                    banner, end, _ = line.rpartition(self.delimiter)
                    line = banner.rstrip() + end
                self._update_config_lines(line)
                self._current_parents = self._current_parents[:-1]
                try:
                    return next(self.generator_config)
                except StopIteration:
                    return None

        raise ValueError("Unable to parse banner end.")

    def set_delimiter(self, config_line: str) -> None:
        """Find delimiter character in banner and set self.delimiter to be it."""
        banner_parsed = self.regex_banner.match(config_line)
        if banner_parsed and "banner_delimiter" in banner_parsed.groupdict():
            self.delimiter = banner_parsed.groupdict()["banner_delimiter"]
            return None
        raise ValueError("Unable to find banner delimiter.")

    def build_config_relationship(self) -> t.List[ConfigLine]:
        r"""Parse text tree of config lines and their parents.

        Examples:
            >>> from netutils.config.parser import IOSXRConfigParser, ConfigLine
            >>> config = (
            ...     "interface Ethernet1/1\n"
            ...     "  vlan 10\n"
            ...     "  no shutdown"
            ...     "interface Ethernet1/2\n"
            ...     "  shutdown\n"
            ... )
            >>> config_tree = IOSXRConfigParser(config)
            >>> config_tree.build_config_relationship() == \
            ... [
            ...     ConfigLine(config_line='interface Ethernet1/1', parents=()),
            ...     ConfigLine(config_line='  vlan 10', parents=('interface Ethernet1/1',)),
            ...     ConfigLine(config_line='  no shutdowninterface Ethernet1/2', parents=('interface Ethernet1/1',)),
            ...     ConfigLine(config_line='  shutdown', parents=('interface Ethernet1/1',))
            ... ]
            True
        """
        for line in self.generator_config:
            if not line[0].isspace():
                self._current_parents = ()
                if self.is_banner_start(line):
                    if not self.delimiter:
                        self.set_delimiter(line)
                    line = self._build_banner(line)  # type: ignore
            else:
                previous_config = self.config_lines[-1]
                self._current_parents = (previous_config.config_line,)
                self.indent_level = self.get_leading_space_count(line)
                line = self._build_nested_config(line)  # type: ignore

            if line is None:
                break
            elif self.is_banner_start(line):
                line = self._build_banner(line)  # type: ignore

            self._update_config_lines(line)
        return self.config_lines


class OptiswitchConfigParser(BaseSpaceConfigParser):
    """MRV Optiswitch config parser."""

    comment_chars: t.List[str] = ["#", "!"]
    banner_start: t.List[str] = []

    @property
    def banner_end(self) -> str:
        """Demarcate End of Banner char(s)."""
        raise NotImplementedError("MRV Optiswitch platform doesn't have a banner.")


class NetironConfigParser(BaseSpaceConfigParser):
    """Extreme Netiron config parser."""

    comment_chars: t.List[str] = ["#", "!"]
    banner_start: t.List[str] = []

    @property
    def banner_end(self) -> str:
        """Demarcate End of Banner char(s)."""
        raise NotImplementedError("Extreme Netiron platform doesn't have a banner.")


class RouterOSConfigParser(BaseSpaceConfigParser):
    """Mikrotik RouterOS config parser."""

    comment_chars: t.List[str] = ["#"]
    banner_start: t.List[str] = ["/system note set note=", "set note="]

    @property
    def banner_end(self) -> str:
        """Demarcate End of Banner char(s)."""
        raise NotImplementedError("Mikrotik platform uses system note as a banner.")

    def is_banner_end(self, line: str) -> bool:
        """Determine if end of banner."""
        if line.endswith('"') or line.startswith("/"):
            return True
        return False

    def _build_banner(self, config_line: str) -> t.Optional[str]:
        """Handle banner config lines.

        Args:
            config_line: The start of the banner (system note) config.

        Returns:
            The next configuration line in the configuration text or None when banner end is the end of the config text.

        Raises:
            ValueError: When the parser is unable to identify the End of the Banner.
        """
        banner_config = [config_line]
        for line in self.generator_config:
            if not self.is_banner_end(line):
                banner_config.append(line)
            else:
                banner_config.append(line)
                line = "\n".join(banner_config)
                self._update_config_lines(line)
                try:
                    return next(self.generator_config)
                except StopIteration:
                    return None
        raise ValueError("Unable to parse banner (system note) end.")


class PaloAltoNetworksConfigParser(BaseSpaceConfigParser):
    """Palo Alto Networks config parser."""

    comment_chars: t.List[str] = []
    banner_start: t.List[str] = [
        'set system login-banner "',
        'login-banner "',
        'set deviceconfig system login-banner "',
    ]
    banner_end = '"'

    def is_banner_end(self, line: str) -> bool:
        """Determine if end of banner."""
        if line.endswith('"') or line.startswith('";') or line.startswith("set") or line.endswith(self.banner_end):
            return True
        return False

    def _build_banner(self, config_line: str) -> t.Optional[str]:
        """Handle banner config lines.

        Args:
            config_line: The start of the banner config.

        Returns:
            The next configuration line in the configuration text or None

        Raises:
            ValueError: When the parser is unable to identify the end of the Banner.
        """
        self._update_config_lines(config_line)
        self._current_parents += (config_line,)
        banner_config = []
        for line in self.generator_config:
            if not self.is_banner_end(line):
                banner_config.append(line)
            else:
                line = normalise_delimiter_caret_c(self.banner_end, line)
                banner_config.append(line.strip())
                line = "\n".join(banner_config)
                if line.endswith("^C"):
                    banner, end, _ = line.rpartition("^C")
                    line = banner.rstrip() + end
                self._update_config_lines(line.strip())
                self._current_parents = self._current_parents[:-1]
                try:
                    return next(self.generator_config)
                except StopIteration:
                    return None

        raise ValueError("Unable to parse banner end.")

    def build_config_relationship(self) -> t.List[ConfigLine]:  # pylint: disable=too-many-branches
        r"""Parse text of config lines and find their parents.

        Examples:
            >>> from netutils.config.parser import PaloAltoNetworksConfigParser, ConfigLine
            >>> config = (
            ...     "set deviceconfig system hostname firewall1\n"
            ...     "set deviceconfig system panorama local-panorama panorama-server 10.0.0.1\n"
            ...     "set deviceconfig system panorama local-panorama panorama-server-2 10.0.0.2\n"
            ...     "set deviceconfig setting config rematch yes\n"
            ... )
            >>> config_tree = PaloAltoNetworksConfigParser(config)
            >>> config_tree.build_config_relationship() == \
            ... [
            ...     ConfigLine(config_line="set deviceconfig system hostname firewall1", parents=()),
            ...     ConfigLine(config_line="set deviceconfig system panorama local-panorama panorama-server 10.0.0.1", parents=()),
            ...     ConfigLine(config_line="set deviceconfig system panorama local-panorama panorama-server-2 10.0.0.2", parents=()),
            ...     ConfigLine(config_line="set deviceconfig setting config rematch yes", parents=()),
            ... ]
            True
        """
        # assume configuration does not need conversion
        _needs_conversion = False

        # if config is in palo brace format, convert to set
        if self.config_lines_only is not None:
            for line in self.config_lines_only:
                if line.endswith("{"):
                    _needs_conversion = True
        if _needs_conversion:
            converted_config = paloalto_panos_brace_to_set(cfg=self.config, cfg_type="string")
            list_config = converted_config.splitlines()
            self.generator_config = (line for line in list_config)

        # build config relationships
        for line in self.generator_config:
            if not line[0].isspace():
                self._current_parents = ()
                if self.is_banner_start(line):
                    line = self._build_banner(line)  # type: ignore
            else:
                previous_config = self.config_lines[-1]
                self._current_parents = (previous_config.config_line,)
                self.indent_level = self.get_leading_space_count(line)
                if not self.is_banner_start(line):
                    line = self._build_nested_config(line)  # type: ignore
                else:
                    line = self._build_banner(line)  # type: ignore
                    if line is not None and line[0].isspace():
                        line = self._build_nested_config(line)  # type: ignore
                    else:
                        self._current_parents = ()

            if line is None:
                break
            elif self.is_banner_start(line):
                line = self._build_banner(line)  # type: ignore

            self._update_config_lines(line)
        return self.config_lines


class FastironConfigParser(CiscoConfigParser):
    """Ruckus FastIron ICX config parser."""

    comment_chars: t.List[str] = ["!"]
    banner_start: t.List[str] = ["banner motd", "banner"]
    regex_banner = re.compile(r"^banner(\smotd)?\s+(?P<banner_delimiter>\S)")

    def __init__(self, config: str):
        """Create ConfigParser Object.

        Args:
            config (str): The config text to parse.
        """
        super(FastironConfigParser, self).__init__(config)

    def _build_banner(self, config_line: str) -> t.Optional[str]:
        """Handle banner config lines.

        Args:
            config_line: The start of the banner config.

        Returns:
            The next configuration line in the configuration text or None

        Raises:
            ValueError: When the parser is unable to identify the end of the Banner.
        """
        self._update_config_lines(config_line)
        self._current_parents += (config_line,)
        banner_config = []
        for line in self.generator_config:
            if not self.is_banner_end(line):
                banner_config.append(line)
            else:
                banner_config.append(line)
                line = "\n".join(banner_config)
                if line.endswith(self.banner_end):
                    banner, end, _ = line.rpartition(self.banner_end)
                    line = banner.rstrip() + end
                self._update_config_lines(line)
                self._current_parents = self._current_parents[:-1]
                try:
                    return next(self.generator_config)
                except StopIteration:
                    return None
        raise ValueError("Unable to parse banner end.")


class UbiquitiAirOSConfigParser(BaseSpaceConfigParser):
    """Ubiquiti airOS config parser."""

    comment_chars: t.List[str] = ["#", "###"]
    banner_start: t.List[str] = []

    @property
    def banner_end(self) -> str:
        """Demarcate End of Banner char(s)."""
        raise NotImplementedError("Ubiquiti airOS platform doesn't have a banner.")

    @property
    def config_lines_only(self) -> str:
        """Remove spaces and unwanted lines from config lines.

        Returns:
            The non-space and non-comment lines from ``config``.
        """
        config_lines = []
        config = self.config.strip()
        for line in config.splitlines():
            if line.startswith("##A"):
                config_lines.append(line)
            if line and line != "##" and not self.is_comment(line):
                config_lines.append(line)

        return "\n".join(config_lines)


class HPEConfigParser(BaseSpaceConfigParser):
    """HPE Implementation of ConfigParser Class."""

    regex_banner = re.compile(r"^header\s(\w+)\s+(?P<banner_delimiter>\^C|\S?)")

    def __init__(self, config: str):
        """Initialize the HPEConfigParser object."""
        self.delimiter = ""
        self._banner_end: t.Optional[str] = None
        super(HPEConfigParser, self).__init__(config)

    def _build_banner(self, config_line: str) -> t.Optional[str]:
        """
        Builds a banner configuration based on the given config_line.

        Args:
            config_line (str): The configuration line to process.

        Returns:
            Optional[str]: The next configuration line, or None if there are no more lines.

        Raises:
            ValueError: If the banner end cannot be parsed.
        """
        if self.is_banner_one_line(config_line):
            self._update_config_lines(config_line)
            try:
                return next(self.generator_config)
            except StopIteration:
                return None
        self._update_config_lines(config_line)
        self._current_parents += (config_line,)
        banner_config = []
        for line in self.generator_config:
            if not self.is_banner_end(line):
                banner_config.append(line)
            else:
                banner_config.append(line)
                line = "\n".join(banner_config)
                if line.endswith(self.delimiter):
                    banner, end, _ = line.rpartition(self.delimiter)
                    line = banner.rstrip() + end
                self._update_config_lines(line)
                self._current_parents = self._current_parents[:-1]
                try:
                    return next(self.generator_config)
                except StopIteration:
                    return None
        raise ValueError("Unable to parse banner end.")

    def set_delimiter(self, config_line: str) -> None:
        """Find delimiter character in banner and set self.delimiter to be it."""
        banner_parsed = self.regex_banner.match(config_line)
        if banner_parsed and "banner_delimiter" in banner_parsed.groupdict():
            self.delimiter = banner_parsed.groupdict()["banner_delimiter"]
            return None
        raise ValueError("Unable to find banner delimiter.")

    def is_banner_one_line(self, config_line: str) -> bool:
        """Checks if the given configuration line represents a one-line banner."""
        self.set_delimiter(config_line.strip())
        _, _delimeter, banner = config_line.partition(self.delimiter)
        banner_config_start = banner.lstrip(_delimeter)
        if _delimeter not in banner_config_start:
            return False
        return True

    def is_banner_start(self, line: str) -> bool:
        """Checks if the given line is the start of a banner."""
        state = super(HPEConfigParser, self).is_banner_start(line)
        if state:
            self.banner_end = line
        return state

    @property
    def banner_end(self) -> str:
        """Get the banner end."""
        if self._banner_end is None:
            raise RuntimeError("Banner end not yet set.")
        return self._banner_end

    @banner_end.setter
    def banner_end(self, banner_start_line: str) -> None:
        """Sets the delimiter for the end of the banner."""
        self.set_delimiter(banner_start_line.strip())
        self._banner_end = self.delimiter


class HPComwareConfigParser(HPEConfigParser, BaseSpaceConfigParser):
    """HP Comware Implementation of ConfigParser Class."""

    banner_start: t.List[str] = ["header "]
    comment_chars: t.List[str] = ["#"]

    def _build_banner(self, config_line: str) -> t.Optional[str]:
        """Build a banner from the given config line."""
        return super(HPComwareConfigParser, self)._build_banner(config_line)
