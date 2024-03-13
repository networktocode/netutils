"""Classes to help manage ACLs ."""

import itertools
import copy
import types
import typing as t
from netutils.protocol_mapper import PROTO_NAME_TO_NUM, TCP_NAME_TO_NUM, UDP_NAME_TO_NUM
from netutils.ip import is_ip_within

try:
    import jsonschema

    HAS_JSON_SCHEMA = True
except ImportError:
    HAS_JSON_SCHEMA = False

INPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": ["string", "null"]},
        "src_zone": {"type": ["string", "array", "null"]},
        "src_ip": {"$ref": "#/definitions/arrayOrIP"},
        "dst_ip": {"$ref": "#/definitions/arrayOrIP"},
        "dst_port": {
            "oneOf": [
                {
                    "type": "null"
                },
                {
                    "$ref": "#/definitions/port",
                },
                {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/port",
                    },
                    "minItems": 1,
                    "uniqueItems": True,
                },
            ],
        },
        "dst_zone": {"type": ["string", "array", "null"]},
        "action": {"type": "string"},
        "protocol": {"type": ["string", "null"]},
    },
    "definitions": {
        "ipv4": {"type": "string", "pattern": "^(?:\\d{1,3}\\.){3}\\d{1,3}$"},
        "ipv4_cidr": {"type": "string", "pattern": "^(?:\\d{1,3}\\.){3}\\d{1,3}\\/\\d{1,2}$"},
        "ipv4_range": {"type": "string", "pattern": "^(?:\\d{1,3}\\.){3}\\d{1,3}\\-(?:\\d{1,3}\\.){3}\\d{1,3}$"},
        "ipv6": {"type": "string", "pattern": "^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"},
        "ipv6_cidr": {"type": "string", "pattern": "^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}/[0-9]{1,3}$"},
        "ipv6_range": {
            "type": "string",
            "pattern": "^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}-([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$",
        },
        "oneIP": {
            "oneOf": [
                {
                    "$ref": "#/definitions/ipv4",
                },
                {
                    "$ref": "#/definitions/ipv4_cidr",
                },
                {
                    "$ref": "#/definitions/ipv4_range",
                },
                {
                    "$ref": "#/definitions/ipv6",
                },
                {
                    "$ref": "#/definitions/ipv6_cidr",
                },
                {
                    "$ref": "#/definitions/ipv6_range",
                },
            ],
        },
        "arrayOrIP": {
            "oneOf": [
                {
                    "$ref": "#/definitions/oneIP",
                },
                {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/oneIP",
                    },
                },
            ],
        },
        "port": {
            "oneOf": [
                {
                    "type": "integer",
                    "minimum": 0,
                    "maximum": 65535,
                },
                {
                    "type": "string",
                    "pattern": "^\d+$",
                },
            ]
        },
    },
    "required": [],
}


RESULT_SCHEMA = copy.deepcopy(INPUT_SCHEMA)
# RESULT_SCHEMA["definitions"]["port"]["pattern"] = "^\\d+\\/\\d+$"  # type: ignore


def _cartesian_product(data: t.Dict[str, str]) -> t.List[t.Dict[str, t.Any]]:
    """Function to create the Cartesian product/permutations from a data dictionary.

    Args:
        data: A dictionary with string keys and either string or list of string values

    Returns:
        A list of dictionaries that extrapolates the product to individual items.

    Examples:
        >>> from netutils.acl import _cartesian_product
        >>> rule = dict(
        ...         name="Allow to internal web",
        ...         src_ip=["192.168.0.0/24", "10.0.0.0/16"],
        ...         dst_ip=["172.16.0.0/16", "192.168.250.10-192.168.250.20"],
        ...         dst_port=["tcp/80", "udp/53"],
        ...         action="permit",
        ...     )
        >>> for item in _cartesian_product(rule):
        ...   print(item)
        ...
        {'name': 'Allow to internal web', 'src_ip': '192.168.0.0/24', 'dst_ip': '172.16.0.0/16', 'dst_port': 'tcp/80', 'action': 'permit'}
        {'name': 'Allow to internal web', 'src_ip': '192.168.0.0/24', 'dst_ip': '172.16.0.0/16', 'dst_port': 'udp/53', 'action': 'permit'}
        {'name': 'Allow to internal web', 'src_ip': '192.168.0.0/24', 'dst_ip': '192.168.250.10-192.168.250.20', 'dst_port': 'tcp/80', 'action': 'permit'}
        {'name': 'Allow to internal web', 'src_ip': '192.168.0.0/24', 'dst_ip': '192.168.250.10-192.168.250.20', 'dst_port': 'udp/53', 'action': 'permit'}
        {'name': 'Allow to internal web', 'src_ip': '10.0.0.0/16', 'dst_ip': '172.16.0.0/16', 'dst_port': 'tcp/80', 'action': 'permit'}
        {'name': 'Allow to internal web', 'src_ip': '10.0.0.0/16', 'dst_ip': '172.16.0.0/16', 'dst_port': 'udp/53', 'action': 'permit'}
        {'name': 'Allow to internal web', 'src_ip': '10.0.0.0/16', 'dst_ip': '192.168.250.10-192.168.250.20', 'dst_port': 'tcp/80', 'action': 'permit'}
        {'name': 'Allow to internal web', 'src_ip': '10.0.0.0/16', 'dst_ip': '192.168.250.10-192.168.250.20', 'dst_port': 'udp/53', 'action': 'permit'}
        >>>
    """
    keys = []
    values = []
    for key, value in data.items():
        keys.append(key)
        if isinstance(value, (str, int)):
            values.append([value])
        elif value is None:
            values.append([None])
        else:
            values.append(value)
    product = list(itertools.product(*values))
    return [dict(zip(keys, item)) for item in product]


def _check_schema(data: t.Any, schema: t.Any, verify: bool) -> None:
    """Checks the schema provided."""
    if not verify:
        return
    if HAS_JSON_SCHEMA:
        jsonschema.validate(data, schema)
    else:
        if not isinstance(data, dict):
            raise ValueError()


def _get_attributes(obj):
    """Function that describes class attributes."""
    result = {
        # name for name in dir(cls)
        attr: getattr(obj, attr)
        for attr in dir(obj)
        if not attr.startswith("_")
        and not callable(getattr(obj, attr))
        and not isinstance(getattr(obj, attr), types.FunctionType)
    }
    return result


def _get_match_funcs(obj):
    """Returns {'attr': match_attr_funct, ...} dict."""
    attrs = {}
    for attr_name in dir(obj):
        if attr_name.startswith("match_") and attr_name not in ["match_details"]:
            match_name = attr_name[len("match_"):]  # noqa: E203
            # When an attribute is not defined, can skip it
            if not hasattr(obj, match_name):
                continue
            attrs[match_name] = getattr(obj, attr_name)

    return attrs


class ACLRule:
    """A class that helps you imagine an acl rule via methodologies."""

    name: t.Any = None
    src_ip: t.Any = None
    src_zone: t.Any = None
    dst_ip: t.Any = None
    dst_port: t.Any = None
    dst_zone: t.Any = None
    protocol: t.Any = None
    action: t.Any = None

    class Meta:  # pylint: disable=too-few-public-methods
        """Default meta class."""

        permit: str = "permit"
        deny: str = "deny"

        input_data_verify: bool = False
        input_data_schema: t.Any = INPUT_SCHEMA

        result_data_verify: bool = False
        result_data_schema: t.Any = RESULT_SCHEMA

        matrix: t.Any = {}
        matrix_enforced: bool = False
        matrix_definition: t.Any = {}

        dst_port_process: bool = False

        order_validate: t.List[str] = []
        order_enforce: t.List[str] = []
        filter_same_ip: bool = True

    def __init__(self, **kwargs):  # pylint: disable=unused-argument
        """Initialize and load data.

        Args:
            data: A dictionary with string keys and either string or list of string values

        Examples:
            >>> from netutils.acl import ACLRule
            >>>
            >>> rule = ACLRule(
            ...     name="Check no match",
            ...     src_ip=["10.1.1.1"],
            ...     src_zone="internal",
            ...     dst_ip="172.16.0.10",
            ...     dst_port="6/80",
            ...     dst_zone="external",
            ...     protocol='tcp',
            ...     action="permit",
            ... )
            >>>
            >>>
            >>> rule._expanded_rules
            [{'name': 'Check no match', 'src_ip': '10.1.1.1', 'src_zone': 'internal', 'dst_ip': '172.16.0.10', 'dst_port': '6/80', 'dst_zone': 'external', 'protocol': 'tcp', 'action': 'permit'}]
            >>>
        """
        self._load_data(kwargs=kwargs)

    def _load_data(self, kwargs) -> None:
        """Load the data into the rule while verifying input data, result data, and processing data."""
        # Remaining kwargs stored under ACLRule.Meta
        pop_kwargs = []
        for key, val in kwargs.items():
            if key not in _get_attributes(self):
                setattr(self.Meta, key, val)
                pop_kwargs.append(key)

        # Pop unneeded keys
        for key in pop_kwargs:
            kwargs.pop(key)

        # Ensure each class attr is in init kwargs.
        for attr in _get_attributes(self):
            if attr not in kwargs:
                kwargs[attr] = getattr(self, attr)

        # Store the init input
        self._preprocessed_data = copy.deepcopy(kwargs)
        self._processed_data = copy.deepcopy(self._preprocessed_data)

        # Input check
        self.input_data_check()

        for attr in _get_attributes(self):
            processor_func = getattr(self, f"process_{attr}", None)  # todo(mzb): remove special case for dst_port !
            if processor_func:
                _attr_data = processor_func(self._processed_data[attr])
            else:
                _attr_data = self._processed_data[attr]

            self._processed_data[attr] = _attr_data
            setattr(self, attr, _attr_data)

        self.result_data_check()
        self.validate()
        self._set_expanded_rules()

    def _set_expanded_rules(self):
        """Expanded rule setter."""
        _expanded_rules = _cartesian_product(self._processed_data)
        if self.Meta.filter_same_ip:
            _expanded_rules = [item for item in _expanded_rules if item["dst_ip"] != item["src_ip"]]

        self._expanded_rules = _expanded_rules

    def input_data_check(self) -> None:
        """Verify the input data against the specified JSONSchema or using a simple dictionary check."""
        return _check_schema(self._preprocessed_data, self.Meta.input_data_schema, self.Meta.input_data_verify)

    def result_data_check(self) -> None:
        """Verify the result data against the specified JSONSchema or using a simple dictionary check."""
        return _check_schema(self._processed_data, self.Meta.result_data_schema, self.Meta.result_data_verify)

    def validate(self) -> t.Any:
        """Run through any method that startswith('validate_') and run that method."""
        if self.Meta.order_validate:
            method_order = self.Meta.order_validate
        else:
            method_order = dir(self)
        results = []
        for name in method_order:
            if name.startswith("validate_"):
                result = getattr(self, name)()
                if not result:
                    continue
                if result and isinstance(result, dict):
                    results.append(result)
                elif result and isinstance(result, list):
                    results.extend(result)
        return results

    def enforce(self) -> t.List[t.Dict[str, t.Any]]:
        """Run through any method that startswith('enforce_') and run that method.

        Returns:
            A list of dictionaries that explains the results of the enforcement.
        """
        if self.Meta.order_enforce:
            method_order = self.Meta.order_enforce
        else:
            method_order = dir(self)
        results = []
        for name in method_order:
            if name.startswith("enforce_"):
                result = getattr(self, name)()
                if not result:
                    continue
                if result and isinstance(result, dict):
                    results.append(result)
                elif result and isinstance(result, list):
                    results.extend(result)
        return results

    def enforce_matrix(self) -> t.Union[t.List[t.Dict[str, t.Any]], None]:
        """A simple `matrix` or grid style check of a rule.

        Returns:
            A list of dictionaries that explains the results of the matrix being enforced.
        """
        if not self.Meta.matrix_enforced:
            return None
        if not self.Meta.matrix:
            raise ValueError("You must set a matrix dictionary to use the matrix feature.")
        if not self.Meta.matrix_definition:
            raise ValueError("You must set a matrix definition dictionary to use the matrix feature.")
        actions = []
        for rule in self._expanded_rules:
            source = rule["src_ip"]
            destination = rule["dst_ip"]
            port = rule["dst_port"]
            src_zone = ""
            dst_zone = ""
            as_tuple = (source, destination, port)
            for zone, ips in self.Meta.matrix_definition.items():
                if is_ip_within(source, ips):
                    src_zone = zone
                if is_ip_within(destination, ips):
                    dst_zone = zone
            if port in self.Meta.matrix.get(src_zone, {}).get(dst_zone, {}).get("allow", []):
                actions.append({"obj": as_tuple, "action": "allow"})
            elif port in self.Meta.matrix.get(src_zone, {}).get(dst_zone, {}).get("notify", []):
                actions.append({"obj": as_tuple, "action": "notify"})
            else:
                actions.append({"obj": as_tuple, "action": "deny"})
        return actions

    def match_action(self, existing_action: str, check_action: str) -> bool:
        """Match the action for equality.

        Args:
            existing_action: The existing action value to be matched.
            check_action: The action value to be checked against the existing action.

        Returns:
            True if `existing_action` matches `check_action`, False otherwise.
        """
        return existing_action == check_action

    def match_src_ip(self, existing_ip: str, check_ip: str) -> bool:
        """Determined if source `check_ip` is within `existing_ip`.

        Args:
            existing_ip: The existing source IP address or IP range to be matched against.
            check_ip: The source IP address to be checked.

        Returns:
            True if `check_ip` is within the range of `existing_ip`, False otherwise.
        """
        if existing_ip == check_ip:  # None cases
            return True
        else:
            return is_ip_within(check_ip, existing_ip)

    def match_src_zone(self, existing_src_zone: str, check_src_zone: str) -> bool:
        """Match the source zone for equality.

        Args:
            existing_src_zone: The existing source zone value to be matched.
            check_src_zone: The source zone value to be checked against the existing zone.

        Returns:
            True if `existing_src_zone` matches `check_src_zone`, False otherwise.
        """
        return existing_src_zone == check_src_zone

    def match_dst_ip(self, existing_ip: str, check_ip: str) -> bool:
        """Determined if destination `check_ip` is within `existing_ip.

        Args:
            existing_ip: The existing destination IP address or IP range to be matched against.
            check_ip: The destination IP address to be checked.

        Returns:
            True if `check_ip` is within the range of `existing_ip`, False otherwise.
        """
        if existing_ip == check_ip:  # None cases
            return True
        else:
            return is_ip_within(check_ip, existing_ip)

    def match_dst_zone(self, existing_dst_zone: str, check_dst_zone: str) -> bool:
        """Match the destination zone for equality.

        Args:
            existing_dst_zone: The existing destination zone value to be matched.
            check_dst_zone: The destination zone value to be checked against the existing zone.

        Returns:
            True if `existing_dst_zone` matches `check_dst_zone`, False otherwise.
        """
        return existing_dst_zone == check_dst_zone

    def match_dst_port(self, existing_port: str, check_port: str) -> bool:
        """Match the destination port for equality.

        Args:
            existing_port: The existing destination port value to be matched.
            check_port: The destination port value to be checked against the existing port.

        Returns:
            True if `existing_port` matches `check_port`, False otherwise.
        """
        return existing_port == check_port

    def match_detail(self, match_rule: "ACLRule") -> t.Dict[str, t.Any]:  # pylint: disable=too-many-locals
        """Verbose way of verifying match details.

        Args:
            match_rule: The rule which you are testing against.

        Returns:
            A dictionary with root keys of `rules_matched` and `rules_matched`.
        """

        products_matched: t.List[t.Dict[str, t.Any]] = []
        products_unmatched: t.List[t.Dict[str, t.Any]] = []

        if not match_rule._expanded_rules:  # pylint: disable=protected-access
            raise ValueError("There is no expanded rules to test against.")
        elif not self._expanded_rules:  # pylint: disable=protected-access
            raise ValueError("There is no expanded rules to test.")

        for match_product in match_rule._expanded_rules:  # pylint: disable=protected-access
            for existing_product in self._expanded_rules:
                comparison_results = []
                for attr_name, attr_func in _get_match_funcs(self).items():
                    comparison_results.append(rattr_func(existing_product[attr_name], match_product[attr_name]))
                # We found match_product in existing_product (all matchers returned True)
                if all(comparison_results):
                    products_matched.append(match_product)
                    break  # No need to compare remaining existing products. Performance improvement.
            else:
                products_unmatched.append(match_product)

        return {
            "match": True if products_matched and not products_unmatched else False,
            "existing_rule": self.serialize(),
            "match_rule": match_rule.serialize(),
            "products_matched": products_matched,
            "products_unmatched": products_unmatched,
        }

    def match(self, match_rule: "ACLRule") -> bool:
        """Simple boolean way of verifying match or not.

        Args:
            match_rule: The rule which you are testing against.

        Returns:
            A boolean if there was a full match or not.
        """
        details = self.match_detail(match_rule)

        return details["match"]

    def __repr__(self) -> str:
        """Set repr of the object to be sane."""
        return self.name

    def serialize(self) -> dict:
        """Primitive Serializer."""
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}


class ACLRules:
    """Class to help match multiple ACLRule objects."""

    rules: t.List[t.Any] = []

    class Meta:  # pylint: disable=too-few-public-methods
        """Default meta class."""

        class_obj = ACLRule

    def __init__(self, data: t.Any, *args: t.Any, **kwargs: t.Any):  # pylint: disable=unused-argument
        """Class to help match multiple ACLRule.

        Args:
            data: A list of `ACLRule` rules.
        """
        self.rules: t.List[t.Any] = []
        self.load_data(data=data)

    def load_data(self, data) -> None:
        """Load the data for multiple rules."""
        for item in data:
            self.rules.append(self.Meta.class_obj(**item))

    def serialize(self) -> list:
        """Primitive Serializer."""
        return [rule.serialize() for rule in self.rules]

    def match(self, rule: ACLRule) -> str:
        """Check the rules loaded in `load_data` match against a new `rule`.

        Args:
            rule: The `ACLRule` rule to test against the list of `ACLRule`s loaded in initiation.

        Returns:
            The response from the rule that matched, or `deny` by default.
        """
        for item in self.rules:
            if item.match(rule):  # mzb: bugfix
                return True  # mzb: change to bool
        return False  # pylint: disable=undefined-loop-variable

    def detailed_match(self, rule: ACLRule) -> t.Any:
        """Verbosely check the rules loaded in `load_data` match against a new `rule`.

        Args:
            rule: The `ACLRule` rule to test against the list of `ACLRule`s loaded in initiation.

        Returns:
            The details from the `ACLRule.detailed_match` results.
        """
        output = []
        for item in self.rules:
            output.append(item.match_detail(rule))  # mzb: bugfix
        return output
