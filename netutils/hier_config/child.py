from __future__ import annotations
from typing import (
    Optional,
    Set,
    Union,
    Iterator,
    List,
    TYPE_CHECKING,
    Type,
    Iterable,
    Tuple,
)
from logging import getLogger
from itertools import chain

from netutils.hier_config.base import HConfigBase
from netutils.hier_config import text_match

if TYPE_CHECKING:
    from .root import HConfig


logger = getLogger(__name__)


# pylint: disable=too-many-instance-attributes,too-many-public-methods
class HConfigChild(HConfigBase):
    def __init__(self, parent: Union[HConfig, HConfigChild], text: str):
        super().__init__()
        self.parent = parent
        self.host = self.root.host
        self._text: str = text.strip()
        self.real_indent_level: int
        # The intent is for self.order_weight values to range from 1 to 999
        # with the default weight being 500
        self.order_weight: int = 500
        self._tags: Set[str] = set()
        self.comments: Set[str] = set()
        self.new_in_config: bool = False
        self.instances: List[dict] = []
        self.facts: dict = {}  # To store externally inserted facts

    def __repr__(self) -> str:
        return f"HConfigChild(HConfig{'' if self.parent is self.root else 'Child'}, {self.text})"

    def __lt__(self, other: HConfigChild) -> bool:
        return self.order_weight < other.order_weight

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HConfigChild):
            return NotImplemented

        if (
            self.text != other.text
            or self.tags != other.tags
            or self.comments != other.comments
            or self.new_in_config != other.new_in_config
        ):
            return False
        return super().__eq__(other)

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        """
        Used for when self.text is changed after the object
        is instantiated to rebuild the children dictionary
        """
        self._text = value.strip()
        self.parent.rebuild_children_dict()

    @property
    def root(self) -> HConfig:
        """returns the HConfig object at the base of the tree"""
        return self.parent.root

    @property
    def logs(self) -> List[str]:
        return self.root.logs

    @property
    def options(self) -> dict:
        return self.root.options

    @property
    def _child_class(self) -> Type[HConfigChild]:
        return HConfigChild

    def depth(self) -> int:
        """Returns the distance to the root HConfig object i.e. indent level"""
        return self.parent.depth() + 1

    def move(self, new_parent: Union[HConfig, HConfigChild]) -> None:
        """
        move one HConfigChild object to different HConfig parent object

        .. code:: python

            hier1 = HConfig(host=host)
            interface1 = hier1.add_child('interface Vlan2')
            interface1.add_child('ip address 10.0.0.1 255.255.255.252')

            hier2 = Hconfig(host)

            interface1.move(hier2)

        :param new_parent: HConfigChild object -> type list
        :return: None
        """
        new_parent.children.append(self)
        new_parent.rebuild_children_dict()
        self.delete()

    def lineage(self) -> Iterator[HConfigChild]:
        """Yields the lineage of parent objects, up to but excluding the root"""
        yield from self.parent.lineage()
        yield self

    def path(self) -> Iterator[str]:
        """Return a list of the text instance variables from self.lineage"""
        for hier_object in self.lineage():
            yield hier_object.text

    def cisco_style_text(self, style: str = "without_comments", tag: Optional[str] = None) -> str:
        """Return a Cisco style formated line i.e. indentation_level + text ! comments"""

        comments = []
        if style == "without_comments":
            pass
        elif style == "merged":
            # count the number of instances that have the tag
            instance_count = 0
            instance_comments: Set[str] = set()
            for instance in self.instances:
                if tag is None or tag in instance["tags"]:
                    instance_count += 1
                    instance_comments.update(instance["comments"])

            # should the word 'instance' be plural?
            word = "instance" if instance_count == 1 else "instances"

            comments.append(f"{instance_count} {word}")
            comments.extend(instance_comments)
        elif style == "with_comments":
            comments.extend(self.comments)

        comments_str = f" !{', '.join(sorted(comments))}" if comments else ""
        return f"{self.indentation}{self.text}{comments_str}"

    @property
    def indentation(self) -> str:
        return "  " * (self.depth() - 1)

    def delete(self) -> None:
        """Delete the current object from its parent"""
        self.parent.del_child(self)

    def append_tag(self, tag: str) -> None:
        """
        Add a tag to self._tags on all leaf nodes
        """
        if self.is_branch:
            for child in self.children:
                child.append_tag(tag)
        else:
            self._tags.add(tag)

    def append_tags(self, tags: Union[str, List[str], Set[str]]) -> None:
        """
        Add tags to self._tags on all leaf nodes
        """
        tags = self._to_set(tags)
        if self.is_branch:
            for child in self.children:
                child.append_tags(tags)
        else:
            self._tags.update(tags)

    def remove_tag(self, tag: str) -> None:
        """
        Remove a tag from self._tags on all leaf nodes
        """
        if self.is_branch:
            for child in self.children:
                child.remove_tag(tag)
        else:
            self._tags.remove(tag)

    def remove_tags(self, tags: Union[str, List[str], Set[str]]) -> None:
        """
        Remove tags from self._tags on all leaf nodes
        """
        tags = self._to_set(tags)
        if self.is_branch:
            for child in self.children:
                child.remove_tags(tags)
        else:
            self._tags.difference_update(tags)

    def negate(self) -> HConfigChild:
        """Negate self.text"""
        for rule in self.options["negation_negate_with"]:
            if self.lineage_test(rule):
                self.text = rule["use"]
                return self

        for rule in self.options["negation_default_when"]:
            if self.lineage_test(rule):
                return self._default()

        return self._swap_negation()

    @property
    def is_leaf(self) -> bool:
        """returns True if there are no children and is not an instance of HConfig"""
        return not self.is_branch

    @property
    def is_branch(self) -> bool:
        """returns True if there are children or is an instance of HConfig"""
        return bool(self.children)

    @property
    def tags(self) -> Set[Optional[str]]:
        """Recursive access to tags on all leaf nodes"""
        if self.is_branch:
            found_tags = set()
            for child in self.children:
                found_tags.update(child.tags)
            return found_tags

        # The getter can return a set containing None
        # while the setter only accepts a set containing strs.
        # mypy doesn't like this
        return self._tags or {None}  # type: ignore

    @tags.setter
    def tags(self, value: Set[str]) -> None:
        """Recursive access to tags on all leaf nodes"""
        if self.is_branch:
            for child in self.children:
                # see comment in getter
                child.tags = value  # type: ignore
        else:
            self._tags = value

    def is_idempotent_command(self, other_children: Iterable[HConfigChild]) -> bool:
        """Determine if self.text is an idempotent change."""
        # Blacklist commands from matching as idempotent
        for rule in self.options["idempotent_commands_blacklist"]:
            if self.lineage_test(rule, True):
                return False

        # Handles idempotent acl entry identification
        if self._idempotent_acl_check():
            if self.host.os in {"iosxr"}:
                self_sn = self.text.split(" ", 1)[0]
                for other_child in other_children:
                    other_sn = other_child.text.split(" ", 1)[0]
                    if self_sn == other_sn:
                        return True

        # Idempotent command identification
        return bool(self.idempotent_for(other_children))

    def idempotent_for(self, other_children: Iterable[HConfigChild]) -> Optional[HConfigChild]:
        for rule in self.options["idempotent_commands"]:
            if self.lineage_test(rule, True):
                for other_child in other_children:
                    if other_child.lineage_test(rule, True):
                        return other_child
        return None

    def sectional_overwrite_no_negate_check(self) -> bool:
        """
        Check self's text to see if negation should be handled by
        overwriting the section without first negating it
        """
        for rule in self.options["sectional_overwrite_no_negate"]:
            if self.lineage_test(rule):
                return True
        return False

    def sectional_overwrite_check(self) -> bool:
        """Determines if self.text matches a sectional overwrite rule"""
        for rule in self.options["sectional_overwrite"]:
            if self.lineage_test(rule):
                return True
        return False

    def overwrite_with(
        self,
        other: HConfigChild,
        delta: Union[HConfig, HConfigChild],
        negate: bool = True,
    ) -> None:
        """Deletes delta.child[self.text], adds a deep copy of self to delta"""
        if other.children != self.children:
            if negate:
                delta.del_child_by_text(self.text)
                deleted = delta.add_child(self.text).negate()
                deleted.comments.add("dropping section")
            if self.children:
                delta.del_child_by_text(self.text)
                new_item = delta.add_deep_copy_of(self)
                new_item.comments.add("re-create section")

    def line_inclusion_test(self, include_tags: Set[str], exclude_tags: Set[str]) -> bool:
        """
        Given the line_tags, include_tags, and exclude_tags,
        determine if the line should be included
        """
        include_line = False

        if include_tags:
            include_line = bool(self.tags.intersection(include_tags))
        if exclude_tags and (include_line or not include_tags):
            include_line = not bool(self.tags.intersection(exclude_tags))

        return include_line

    def all_children_sorted_by_tags(self, include_tags: Set[str], exclude_tags: Set[str]) -> Iterator[HConfigChild]:
        """Yield all children recursively that match include/exclude tags"""
        if self.is_leaf:
            if self.line_inclusion_test(include_tags, exclude_tags):
                yield self
        else:
            self_iter = iter((self,))
            for child in sorted(self.children):
                included_children = child.all_children_sorted_by_tags(include_tags, exclude_tags)
                if peek := next(included_children, None):
                    yield from chain(self_iter, (peek,), included_children)

    def lineage_test(self, rule: dict, strip_negation: bool = False) -> bool:
        """A generic test against a lineage of HConfigChild objects"""
        if rule.get("match_leaf", False):
            lineage_obj: Iterator[HConfigChild] = (o for o in (self,))
            lineage_depth = 1
        else:
            lineage_obj = self.lineage()
            lineage_depth = self.depth()

        rule_lineage_len = len(rule["lineage"])
        if rule_lineage_len != lineage_depth:
            return False

        matches = 0
        for lineage_rule, section in zip(rule["lineage"], lineage_obj):
            object_rules, text_match_rules = self._explode_lineage_rule(lineage_rule)

            if not self._lineage_eval_object_rules(object_rules, section):
                return False

            # This removes negations for each section but honestly,
            # we really only need to do this on the last one
            if strip_negation:
                if section.text.startswith(self._negation_prefix):
                    text = section.text[len(self._negation_prefix) :]  # noqa: E203
                elif section.text.startswith("default "):
                    text = section.text[8:]
                else:
                    text = section.text
            else:
                text = section.text

            if self._lineage_eval_text_match_rules(text_match_rules, text):
                matches += 1
                continue
            return False

        return matches == rule_lineage_len

    def _swap_negation(self) -> HConfigChild:
        """Swap negation of a self.text"""
        if self.text.startswith(self._negation_prefix):
            self.text = self.text[len(self._negation_prefix) :]  # noqa: E203
        else:
            self.text = self._negation_prefix + self.text

        return self

    def _default(self) -> HConfigChild:
        """Default self.text"""
        if self.text.startswith(self._negation_prefix):
            self.text = "default " + self.text[len(self._negation_prefix) :]  # noqa: E203
        else:
            self.text = "default " + self.text
        return self

    def _idempotent_acl_check(self) -> bool:
        """
        Handle conditional testing to determine if idempotent acl handling for iosxr should be used
        """
        if self.host.os in {"iosxr"}:
            if isinstance(self.parent, HConfigChild):
                acl = ("ipv4 access-list ", "ipv6 access-list ")
                if self.parent.text.startswith(acl):
                    return True
        return False

    @staticmethod
    def _explode_lineage_rule(rule: dict) -> Tuple[list, list]:
        text_match_rules: List[dict] = []
        object_rules = []
        for test, expression in rule.items():
            if test in {"new_in_config", "negative_intersection_tags"}:
                object_rules.append({"test": test, "expression": expression})
            elif test == "equals":
                if isinstance(expression, list):
                    text_match_rules.append({"test": test, "expression": set(expression)})
                else:
                    text_match_rules.append({"test": test, "expression": {expression}})
            elif test in {"startswith", "endswith"}:
                if isinstance(expression, list):
                    text_match_rules.append({"test": test, "expression": tuple(expression)})
                else:
                    text_match_rules.append({"test": test, "expression": (expression,)})
            elif isinstance(expression, list):
                text_match_rules += [{"test": test, "expression": e} for e in expression]
            else:
                text_match_rules += [{"test": test, "expression": expression}]
        return object_rules, text_match_rules

    def _lineage_eval_object_rules(self, rules: list, section: HConfigChild) -> bool:
        """
        Evaluate a list of lineage object rules.

        All object rules must match in order to return True

        """
        matches = 0
        for rule in rules:
            if rule["test"] == "new_in_config":
                if rule["expression"] == section.new_in_config:
                    matches += 1
                    continue
                return False
            if rule["test"] == "negative_intersection_tags":
                rule["expression"] = self._to_list(rule["expression"])
                if not set(rule["expression"]).intersection(section.tags):
                    matches += 1
                    continue
                return False
        return matches == len(rules)

    @staticmethod
    def _lineage_eval_text_match_rules(rules: list, text: str) -> bool:
        """
        Evaluate a list of lineage text_match rules.

        Only one text_match rule must match in order to return True
        """
        for rule in rules:
            if text_match.dict_call(rule["test"], text, rule["expression"]):
                return True
        return False

    @staticmethod
    def _to_list(obj: Union[list, object]) -> list:
        return obj if isinstance(obj, list) else [obj]

    @staticmethod
    def _to_set(items: Union[str, List[str], Set[str]]) -> Set[str]:
        # There's code out in the wild that passes List[str] or str, need to normalize for now
        if isinstance(items, list):
            return set(items)
        if isinstance(items, str):
            return {items}
        # Assume it's a set of str
        return items

    def _duplicate_child_allowed_check(self) -> bool:
        """Determine if duplicate(identical text) children are allowed under the parent"""
        for rule in self.options["parent_allows_duplicate_child"]:
            if self.lineage_test(rule):
                return True
        return False
