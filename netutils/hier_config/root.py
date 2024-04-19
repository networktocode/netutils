from __future__ import annotations
from itertools import islice
import re
from pathlib import Path
from typing import Optional, Set, Union, Iterator, List, TYPE_CHECKING, Tuple, Type
from logging import getLogger

from netutils.hier_config.exceptions import HostAttrError, HierConfigError
from netutils.hier_config.base import HConfigBase
from netutils.hier_config.child import HConfigChild

if TYPE_CHECKING:
    from .host import Host

logger = getLogger(__name__)


class HConfig(HConfigBase):  # pylint: disable=too-many-public-methods
    """
    A class for representing and comparing Cisco configurations in a
    hierarchical tree data structure.

    Example usage:

    .. code:: python

        # Setup basic environment

        from hier_config import HConfig, Host
        import yaml

        options = yaml.safe_load(open('./tests/fixtures/options_ios.yml'))
        host = Host('example.rtr', 'ios', options)

        # Build HConfig object for the Running Config

        running_config_hier = HConfig(host=host)
        running_config_hier.load_from_file('./tests/fixtures/running_config.conf')

        # Build Hierarchical Configuration object for the Generated Config

        generated_config_hier = HConfig(host=host)
        generated_config_hier.load_from_file('./tests/fixtures/generated_config.conf')

        # Build Hierarchical Configuration object for the Remediation Config

        remediation_config_hier = running_config_hier.config_to_get_to(generated_config_hier)

        for line in remediation_config_hier.all_children():
            print(line.cisco_style_text())

    See:

        ./tests/fixtures/tags_ios.yml and ./tests/fixtures/options_ios.yml

        for test examples of options and tags.
    """

    def __init__(self, host: Host):
        super().__init__()
        if not all([hasattr(host, "hostname"), hasattr(host, "os"), hasattr(host, "hconfig_options")]):
            raise HostAttrError(host, "Missing attributes - hostname, os, hconfig_options.")

        self.host = host
        self.parent = self
        self.real_indent_level = -1

        self.options.setdefault("negation", "no")
        self.options.setdefault("syntax_style", "cisco")
        self._logs: List[str] = []

    def __repr__(self) -> str:
        return f"HConfig(host={self.host})"

    def __hash__(self) -> int:
        return id(self)

    @property
    def root(self) -> HConfig:
        """returns the HConfig object at the base of the tree"""
        return self

    @property
    def options(self) -> dict:
        return self.host.hconfig_options

    @property
    def is_leaf(self) -> bool:
        """returns True if there are no children and is not an instance of HConfig"""
        return False

    @property
    def logs(self) -> List[str]:
        return self._logs

    @property
    def is_branch(self) -> bool:
        """returns True if there are children or is an instance of HConfig"""
        return True

    @property
    def _child_class(self) -> Type[HConfigChild]:
        return HConfigChild

    @property
    def tags(self) -> Set[Optional[str]]:
        """Recursive access to tags on all leaf nodes"""
        found_tags: Set[Optional[str]] = set()
        for child in self.children:
            found_tags.update(child.tags)
        return found_tags

    @tags.setter
    def tags(self, value: Set[str]) -> None:
        """Recursive access to tags on all leaf nodes"""
        for child in self.children:
            child.tags = value  # type: ignore

    def merge(self, other: HConfig) -> None:
        """Merges two HConfig objects"""
        for child in other.children:
            self.add_deep_copy_of(child, merged=True)

    def lineage(self) -> Iterator[HConfigChild]:
        """
        Yields the lineage of parent objects, up to but excluding the root
        """
        yield from ()

    def load_from_file(self, file_path: Union[str, Path]) -> None:
        """Load configuration text from a file"""
        with open(file_path) as file:  # pylint: disable=unspecified-encoding
            config_text = file.read()
        self.load_from_string(config_text)

    def load_from_string(self, config_text: str) -> None:
        """Create Hierarchical Configuration nested objects from text"""
        config_text = self._convert_to_set_commands(config_text)

        for sub in self.options["full_text_sub"]:
            config_text = re.sub(sub["search"], sub["replace"], config_text)

        self._load_from_string_lines(config_text)

        if self.host.os == "ios":
            self._remove_acl_remarks()
            self._add_acl_sequence_numbers()
            self._rm_ipv6_acl_sequence_numbers()

    def load_from_dump(self, dump: List[dict]) -> None:
        """Load an HConfig dump"""
        last_item: Union[HConfig, HConfigChild] = self
        for item in dump:
            # parent is the root
            if item["depth"] == 1:
                parent: Union[HConfig, HConfigChild] = self
            # has the same parent
            elif last_item.depth() == item["depth"]:
                parent = last_item.parent
            # is a child object
            elif last_item.depth() + 1 == item["depth"]:
                parent = last_item
            # has a parent somewhere closer to the root but not the root
            else:
                # last_item.lineage() = (a, b, c, d, e), new_item['depth'] = 2,
                # parent = a
                parent = next(islice(last_item.lineage(), item["depth"] - 2, item["depth"] - 1))
            # also accept 'line'
            # obj = parent.add_child(item.get('text', item['line']), force_duplicate=True)
            obj = parent.add_child(item["text"], force_duplicate=True)
            obj.tags = set(item["tags"])
            obj.comments = set(item["comments"])
            obj.new_in_config = item["new_in_config"]
            last_item = obj

    def dump(self, lineage_rules: Optional[List[dict]] = None) -> List[dict]:
        """Dump a list of loaded HConfig data"""
        if lineage_rules:
            children = self.all_children_sorted_with_lineage_rules(lineage_rules)
        else:
            children = self.all_children_sorted()

        output = []
        for child in children:
            output.append(
                {
                    "depth": child.depth(),
                    "text": child.text,
                    "tags": list(child.tags),
                    "comments": list(child.comments),
                    "new_in_config": child.new_in_config,
                }
            )

        return output

    def add_tags(self, tag_rules: list, strip_negation: bool = False) -> None:
        """
        Handler for tagging sections of Hierarchical Configuration data structure
        for inclusion and exclusion.
        """
        for rule in tag_rules:
            for child in self.all_children():
                if child.lineage_test(rule, strip_negation):
                    if "add_tags" in rule:
                        child.append_tags(rule["add_tags"])
                    if "remove_tags" in rule:
                        child.remove_tags(rule["remove_tags"])

    def depth(self) -> int:
        """Returns the distance to the root HConfig object i.e. indent level"""
        return 0

    def difference(self, target: HConfig) -> HConfig:
        """
        Creates a new HConfig object with the config from self that is not in target

        Example usage:
        whats in the config.lines v.s. in running config
        i.e. did all my configuration changes get written to the running config

        :param target: HConfig - The configuration to check against
        :return: HConfig - missing config additions
        """
        delta = HConfig(host=self.host)
        difference = self._difference(target, delta)
        # Makes mypy happy
        if not isinstance(difference, HConfig):
            raise TypeError
        return difference

    def config_to_get_to(self, target: HConfig, delta: Optional[HConfig] = None) -> HConfig:
        """
        Figures out what commands need to be executed to transition from self to target.
        self is the source data structure(i.e. the running_config),
        target is the destination(i.e. generated_config)

        """
        if delta is None:
            delta = HConfig(host=self.host)

        root_config = self._config_to_get_to(target, delta)
        if not isinstance(root_config, HConfig):
            raise TypeError

        return root_config

    def add_ancestor_copy_of(self, parent_to_add: HConfigChild) -> Union[HConfig, HConfigChild]:
        """
        Add a copy of the ancestry of parent_to_add to self
        and return the deepest child which is equivalent to parent_to_add
        """
        base: Union[HConfig, HConfigChild] = self
        for parent in parent_to_add.lineage():
            base = base.add_shallow_copy_of(parent)

        return base

    def set_order_weight(self) -> None:
        """Sets self.order integer on all children"""
        for child in self.all_children():
            for rule in self.options["ordering"]:
                if child.lineage_test(rule):
                    child.order_weight = rule["order"]

    def add_sectional_exiting(self) -> None:
        """
        Adds the sectional exiting text as a child
        """
        for child in self.all_children():
            for rule in self.options["sectional_exiting"]:
                if child.lineage_test(rule):
                    exit_line = child.get_child("equals", rule["exit_text"])
                    if exit_line is None:
                        exit_line = child.add_child(rule["exit_text"])

                    exit_line.tags = child.tags
                    exit_line.order_weight = 999

    def future(self, config: HConfig) -> HConfig:
        """
        EXPERIMENTAL - predict the future config after config is applied to self

        The quality of the this method's output will in part depend on how well
        the OS options are tuned. Ensuring that idempotency rules are accurate is
        especially important.
        """
        future_config = HConfig(host=self.host)
        self._future(config, future_config)
        return future_config

    def with_tags(self, tags: Set[str]) -> HConfig:
        """
        Returns a new instance containing only sub-objects
        with one of the tags in tags
        """
        new_instance = HConfig(self.host)
        result = self._with_tags(tags, new_instance)
        # Makes mypy happy
        if not isinstance(result, HConfig):
            raise ValueError
        return new_instance

    def all_children_sorted_by_tags(self, include_tags: Set[str], exclude_tags: Set[str]) -> Iterator[HConfigChild]:
        """Yield all children recursively that match include/exclude tags"""
        for child in sorted(self.children):
            yield from child.all_children_sorted_by_tags(include_tags, exclude_tags)

    @staticmethod
    def _load_from_string_lines_end_of_banner_test(
        config_line: str, banner_end_lines: Set[str], banner_end_contains: List[str]
    ) -> bool:
        if config_line.startswith("^"):
            return True
        if config_line in banner_end_lines:
            return True
        if any([c in config_line for c in banner_end_contains]):
            return True
        return False

    # pylint: disable=too-many-locals,too-many-branches,too-many-statements
    def _load_from_string_lines(self, config_text: str) -> None:
        current_section: Union[HConfig, HConfigChild] = self
        most_recent_item: Union[HConfig, HConfigChild] = current_section
        indent_adjust = 0
        end_indent_adjust = []
        temp_banner = []
        banner_end_lines = {"EOF", "%", "!"}
        banner_end_contains: List[str] = []
        in_banner = False

        for line in config_text.splitlines():
            # Process banners in configuration into one line
            if in_banner:
                if line != "!":
                    temp_banner.append(line)

                # Test if this line is the end of a banner
                if self._load_from_string_lines_end_of_banner_test(str(line), banner_end_lines, banner_end_contains):
                    in_banner = False
                    most_recent_item = self.add_child("\n".join(temp_banner), True)
                    most_recent_item.real_indent_level = 0
                    current_section = self
                    temp_banner = []
                continue

            # Test if this line is the start of a banner and not an empty banner
            # Empty banners matching the below expression have been seen on NX-OS
            if line.startswith("banner ") and line != "banner motd ##":
                in_banner = True
                temp_banner.append(line)
                banner_words = line.split()
                try:
                    banner_end_contains.append(banner_words[2])
                    banner_end_lines.add(banner_words[2][:1])
                    banner_end_lines.add(banner_words[2][:2])
                except IndexError:
                    pass
                continue

            actual_indent = len(line) - len(line.lstrip())
            line = " " * actual_indent + " ".join(line.split())
            for sub in self.options["per_line_sub"]:
                line = re.sub(sub["search"], sub["replace"], line)
            line = line.rstrip()

            # If line is now empty, move to the next
            if not line:
                continue

            # Determine indentation level
            this_indent = len(line) - len(line.lstrip()) + indent_adjust

            line = line.lstrip()

            # Walks back up the tree
            while this_indent <= current_section.real_indent_level:
                current_section = current_section.parent

            # Walks down the tree by one step
            if this_indent > most_recent_item.real_indent_level:
                current_section = most_recent_item

            most_recent_item = current_section.add_child(line, True)
            most_recent_item.real_indent_level = this_indent

            for expression in self.options["indent_adjust"]:
                if re.search(expression["start_expression"], line):
                    indent_adjust += 1
                    end_indent_adjust.append(expression["end_expression"])
                    break
            if end_indent_adjust and re.search(end_indent_adjust[0], line):
                indent_adjust -= 1
                del end_indent_adjust[0]

        if in_banner:
            raise HierConfigError("we are still in a banner for some reason.")

    def _add_acl_sequence_numbers(self) -> None:
        """
        Add ACL sequence numbers for use on configurations with a style of 'ios'
        """
        ipv4_acl_sw = "ip access-list"
        # ipv6_acl_sw = ('ipv6 access-list')
        if self.host.os in ["ios"]:
            acl_line_sw: Tuple[str, ...] = ("permit", "deny")
        else:
            acl_line_sw = ("permit", "deny", "remark")
        for child in self.children:
            if child.text.startswith(ipv4_acl_sw):
                sequence_number = 10
                for sub_child in child.children:
                    if sub_child.text.startswith(acl_line_sw):
                        sub_child.text = f"{sequence_number} {sub_child.text}"
                        sequence_number += 10

    def _rm_ipv6_acl_sequence_numbers(self) -> None:
        """If there are sequence numbers in the IPv6 ACL, remove them"""
        for acl in self.get_children("startswith", "ipv6 access-list "):
            for entry in acl.children:
                if entry.text.startswith("sequence"):
                    entry.text = " ".join(entry.text.split()[2:])

    def _remove_acl_remarks(self) -> None:
        for acl in self.get_children("startswith", "ip access-list "):
            for entry in acl.children:
                if entry.text.startswith("remark"):
                    acl.children.remove(entry)

    def _duplicate_child_allowed_check(self) -> bool:
        """Determine if duplicate(identical text) children are allowed under the parent"""
        return False

    def _convert_to_set_commands(self, config_str: str) -> str:
        """
        Convert a Junupier style config string into a list of set commands.

        Args:
            config_str (str): The config string to convert to set commands
        Returns:
            config_str (str): Configuration string
        """
        if self.options["syntax_style"] == "juniper":
            lines = config_str.split("\n")
            path: List[str] = []
            set_commands: List[str] = []

            for line in lines:
                stripped_line = line.strip()

                # Skip empty lines
                if not stripped_line:
                    continue

                # Strip ; from the end of the line
                if stripped_line.endswith(";"):
                    stripped_line = stripped_line.replace(";", "")

                # Count the number of spaces at the beginning to determine the level
                level = line.find(stripped_line) // 4

                # Adjust the current path based on the level
                path = path[:level]

                # If the line ends with '{' or '}', it starts a new block
                if stripped_line.endswith(("{", "}")):
                    path.append(stripped_line[:-1].strip())
                elif stripped_line.startswith(("set", "delete")):
                    # It's already a set command, so just add it to the list
                    set_commands.append(stripped_line)
                else:
                    # It's a command line, construct the full command
                    command = "set " + " ".join(path) + " " + stripped_line
                    set_commands.append(command)

            config_str = "\n".join(set_commands)

        return config_str
