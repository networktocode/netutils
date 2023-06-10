"""Classes to help manage ACLs ."""

import itertools
import copy
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
        "name": {"type": "string"},
        "src_zone": {"type": ["string", "array"]},
        "src_ip": {"$ref": "#/definitions/arrayOrIP"},
        "dst_ip": {"$ref": "#/definitions/arrayOrIP"},
        "dst_port": {
            "oneOf": [
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
        "dst_zone": {"type": ["string", "array"]},
        "action": {"type": "string"},
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
        "port": {"type": "string", "pattern": "^\\S+\\/\\S+$"},
    },
    "required": [],
}


RESULT_SCHEMA = copy.deepcopy(INPUT_SCHEMA)
RESULT_SCHEMA["definitions"]["port"]["pattern"] = "^\\d+\\/\\d+$"  # type: ignore


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


class ACLRule:
    """A class that helps you imagine an acl rule via methodologies."""

    attrs: t.List[str] = ["name", "src_ip", "src_zone", "dst_ip", "dst_port", "dst_zone", "action"]
    permit: str = "permit"
    deny: str = "deny"

    input_data_verify: bool = False
    input_data_schema: t.Any = INPUT_SCHEMA

    result_data_verify: bool = False
    result_data_schema: t.Any = RESULT_SCHEMA

    matrix: t.Any = {}
    matrix_enforced: bool = False
    matrix_definition: t.Any = {}

    dst_port_process: bool = True

    order_validate: t.List[str] = []
    order_enforce: t.List[str] = []
    filter_same_ip: bool = True

    def __init__(self, data: t.Any, *args: t.Any, **kwargs: t.Any):  # pylint: disable=unused-argument
        """Initialize and load data.

        Args:
            data: A dictionary with string keys and either string or list of string values

        Examples:
            >>> from netutils.acl import ACLRule
            >>>
            >>> acl_data = dict(
            ...     name="Check no match",
            ...     src_ip=["10.1.1.1"],
            ...     dst_ip="172.16.0.10",
            ...     dst_port="tcp/www-http",
            ...     action="permit",
            ... )
            >>>
            >>> rule = ACLRule(acl_data)
            >>>
            >>> rule.expanded_rules
            [{'name': 'Check no match', 'src_ip': '10.1.1.1', 'dst_ip': '172.16.0.10', 'dst_port': '6/80', 'action': 'permit'}]
            >>>
        """
        self.processed: t.Dict[str, str] = {}
        self.data = data
        self.load_data()

    def load_data(self) -> None:
        """Load the data into the rule while verifying input data, result data, and processing data."""
        self.input_data_check()
        for attr in self.attrs:
            if not self.data.get(attr):
                continue
            if hasattr(self, f"process_{attr}"):
                proccessor = getattr(self, f"process_{attr}")
                _attr_data = proccessor(self.data[attr])
            else:
                _attr_data = self.data[attr]
            self.processed[attr] = _attr_data
            setattr(self, attr, _attr_data)
        self.result_data_check()
        self.validate()
        self.expanded_rules = _cartesian_product(self.processed)
        if self.filter_same_ip:
            self.expanded_rules = [item for item in self.expanded_rules if item["dst_ip"] != item["src_ip"]]

    def input_data_check(self) -> None:
        """Verify the input data against the specified JSONSchema or using a simple dictionary check."""
        return _check_schema(self.data, self.input_data_schema, self.input_data_verify)

    def result_data_check(self) -> None:
        """Verify the result data against the specified JSONSchema or using a simple dictionary check."""
        return _check_schema(self.processed, self.result_data_schema, self.result_data_verify)

    def validate(self) -> t.Any:
        """Run through any method that startswith('validate_') and run that method."""
        if self.order_validate:
            method_order = self.order_validate
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

    def process_dst_port(
        self, dst_port: t.Any
    ) -> t.Union[t.List[str], None]:  # pylint: disable=inconsistent-return-statements
        """Convert port and protocol information.

        Method supports a single format of `{protocol}/{port}`, and will translate the
        protocol for all IANA defined protocols. The port will be translated for TCP and
        UDP ports only. For all other protocols should use port of 0, e.g. `ICMP/0` for ICMP
        or `50/0` for ESP. Similarly, IANA defines the port mappings, while these are mostly
        staying unchanged, but sourced from
        https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv.
        """
        output = []
        if not self.dst_port_process:
            return None
        if not isinstance(dst_port, list):
            dst_port = [dst_port]
        for item in dst_port:
            protocol = item.split("/")[0]
            port = item.split("/")[1]
            if protocol.isalpha():
                if not PROTO_NAME_TO_NUM.get(protocol.upper()):
                    raise ValueError(
                        f"Protocol {protocol} was not found in netutils.protocol_mapper.PROTO_NAME_TO_NUM."
                    )
                protocol = PROTO_NAME_TO_NUM[protocol.upper()]
            # test port[0] vs port, since dashes do not count, e.g. www-http
            if int(protocol) == 6 and port[0].isalpha():
                if not TCP_NAME_TO_NUM.get(port.upper()):
                    raise ValueError(f"Port {port} was not found in netutils.protocol_mapper.TCP_NAME_TO_NUM.")
                port = TCP_NAME_TO_NUM[port.upper()]
            if int(protocol) == 17 and port[0].isalpha():
                if not UDP_NAME_TO_NUM.get(port.upper()):
                    raise ValueError(f"Port {port} was not found in netutils.protocol_mapper.UDP_NAME_TO_NUM.")
                port = UDP_NAME_TO_NUM[port.upper()]
            output.append(f"{protocol}/{port}")
        return output

    def enforce(self) -> t.List[t.Dict[str, t.Any]]:
        """Run through any method that startswith('enforce_') and run that method.

        Returns:
            A list of dictionaries that explains the results of the enforcement.
        """
        if self.order_enforce:
            method_order = self.order_enforce
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
        if not self.matrix_enforced:
            return None
        if not self.matrix:
            raise ValueError("You must set a matrix dictionary to use the matrix feature.")
        if not self.matrix_definition:
            raise ValueError("You must set a matrix definition dictionary to use the matrix feature.")
        actions = []
        for rule in self.expanded_rules:
            source = rule["src_ip"]
            destination = rule["dst_ip"]
            port = rule["dst_port"]
            src_zone = ""
            dst_zone = ""
            as_tuple = (source, destination, port)
            for zone, ips in self.matrix_definition.items():
                if is_ip_within(source, ips):
                    src_zone = zone
                if is_ip_within(destination, ips):
                    dst_zone = zone
            if port in self.matrix.get(src_zone, {}).get(dst_zone, {}).get("allow", []):
                actions.append({"obj": as_tuple, "action": "allow"})
            elif port in self.matrix.get(src_zone, {}).get(dst_zone, {}).get("notify", []):
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

    def match_details(self, match_rule: "ACLRule") -> t.Dict[str, t.Any]:  # pylint: disable=too-many-locals
        """Verbose way of verifying match details.

        Args:
            match_rule: The rule which you are testing against.

        Returns:
            A dictionary with root keys of `rules_matched` and `rules_matched`.
        """
        attrs = []
        for name in dir(self):
            if name.startswith("match_"):
                obj_name = name[len("match_") :]  # noqa: E203
                # When an attribute is not defined, can skip it
                if not hasattr(match_rule, obj_name):
                    continue
                attrs.append(obj_name)

        rules_found: t.List[bool] = []
        rules_unmatched: t.List[t.Dict[str, t.Any]] = []
        rules_matched: t.List[t.Dict[str, t.Any]] = []

        if not match_rule.expanded_rules:
            raise ValueError("There is no expanded rules to test against.")
        for rule in match_rule.expanded_rules:
            rules_found.append(False)
            for existing_rule in self.expanded_rules:
                missing = False
                for attr in attrs:
                    # Examples of obj are match_rule.src_ip, match_rule.dst_port
                    rule_value = rule[attr]
                    existing_value = existing_rule[attr]
                    # Examples of getter are self.match_src_ip, self.match_dst_port
                    getter = getattr(self, f"match_{attr}")(existing_value, rule_value)
                    if not getter and getter is not None:
                        missing = True
                        break
                # If the loop gets through with each existing rule not flagging
                # the `missing` value, we know everything was matched, and the rule has
                # found a complete match, we can break out of the loop at this point.
                if not missing:
                    rules_found[-1] = True
                    break
            detailed_info = {
                "existing_rule_product": existing_rule,  # pylint: disable=undefined-loop-variable
                "match_rule": match_rule.processed,
                "existing_rule": self.processed,
            }
            if rules_found[-1]:
                detailed_info["match_rule_product"] = rule
                rules_matched.append(detailed_info)
            else:
                rules_unmatched.append(detailed_info)
        return {"rules_matched": rules_matched, "rules_unmatched": rules_unmatched}

    def match(self, match_rule: "ACLRule") -> bool:
        """Simple boolean way of verifying match or not.

        Args:
            match_rule: The rule which you are testing against.

        Returns:
            A boolean if there was a full match or not.
        """
        details = self.match_details(match_rule)
        return not bool(details["rules_unmatched"])

    def __repr__(self) -> str:
        """Set repr of the object to be sane."""
        output = []
        for attr in self.attrs:
            if self.processed.get(attr):
                output.append(f"{attr}: {self.processed[attr]}")
        return ", ".join(output)


class ACLRules:
    """Class to help match multiple ACLRule objects."""

    class_obj = ACLRule

    def __init__(self, data: t.Any, *args: t.Any, **kwargs: t.Any):  # pylint: disable=unused-argument
        """Class to help match multiple ACLRule.

        Args:
            data: A list of `ACLRule` rules.
        """
        self.data: t.Any = data
        self.rules: t.List[t.Any] = []
        self.load_data()

    def load_data(self) -> None:
        """Load the data for multiple rules."""
        for item in self.data:
            self.rules.append(self.class_obj(item))

    def match(self, rule: ACLRule) -> str:
        """Check the rules loaded in `load_data` match against a new `rule`.

        Args:
            rule: The `ACLRule` rule to test against the list of `ACLRule`s loaded in initiation.

        Returns:
            The response from the rule that matched, or `deny` by default.
        """
        for item in self.rules:
            if item.match(self.class_obj(rule)):
                return str(item.action)
        return str(item.deny)  # pylint: disable=undefined-loop-variable

    def match_details(self, rule: ACLRule) -> t.Any:
        """Verbosely check the rules loaded in `load_data` match against a new `rule`.

        Args:
            rule: The `ACLRule` rule to test against the list of `ACLRule`s loaded in initiation.

        Returns:
            The details from the `ACLRule.match_details` results.
        """
        output = []
        for item in self.rules:
            output.append(item.match_details(self.class_obj(rule)))
        return output
