"""Test for the BGP ASN functions."""
# pylint: disable=use-dict-literal

import pytest

from netutils import acl

verify_acl = [
    {
        "sent": dict(
            name="Check multiple sources pass. Check conversion of non-alpha tcp, e.g. with a dash",
            src_ip=["192.168.1.10", "192.168.1.11", "192.168.1.15-192.168.1.20"],
            dst_ip="172.16.0.10",
            dst_port="tcp/www-http",
            action="permit",
        ),
        "received": "permit",
    },
    {
        "sent": dict(
            name="Check with number in port definition",
            src_ip="192.168.0.10",
            dst_ip="192.168.250.11",
            dst_port="6/80",
            action="permit",
        ),
        "received": "permit",
    },
    {
        "sent": dict(
            name="Check with subnets",
            src_ip="192.168.0.0/25",
            dst_ip="172.16.0.0/24",
            dst_port="6/80",
            action="permit",
        ),
        "received": "permit",
    },
    {
        "sent": dict(
            name="Test partial match on Source IP",
            src_ip=["192.168.1.10", "192.168.2.10"],
            dst_ip="172.16.0.11",
            dst_port="tcp/80",
            action="permit",
        ),
        "received": "deny",
    },
    {
        "sent": dict(
            name="Test an entry that is not found",
            src_ip="192.168.1.10",
            dst_ip="192.168.240.1",
            dst_port="tcp/80",
            action="permit",
        ),
        "received": "deny",
    },
    {
        "sent": dict(
            name="Test an action not permit or deny",
            src_ip="10.1.1.1",
            dst_ip="10.255.255.255",
            dst_port="tcp/443",
            action="permit",
        ),
        "received": "deny",
    },
]

acls = [
    dict(
        name="Allow to internal web",
        src_ip=["192.168.0.0/24", "10.0.0.0/16"],
        dst_ip=["172.16.0.0/16", "192.168.250.10-192.168.250.20"],
        dst_port=["tcp/80", "udp/53"],
        action="permit",
    ),
    dict(
        name="Allow to internal dns",
        src_ip=["192.168.1.0/24"],
        dst_ip=["172.16.0.0/16"],
        dst_port=["tcp/80", "udp/53"],
        action="permit",
    ),
    dict(
        name="Allow to internal https",
        src_ip=["10.0.0.0/8"],
        dst_ip=["172.16.0.0/16"],
        dst_port=["tcp/443"],
        action="deny",
    ),
    dict(
        name="Drop (not deny) this specfic packet",
        src_ip="10.1.1.1",
        dst_ip="10.255.255.255",
        dst_port="tcp/443",
        action="drop",
    ),
    dict(
        name="Allow External DNS",
        src_ip=["0.0.0.0/0"],
        dst_ip=["8.8.8.8/32", "8.8.4.4/32"],
        dst_port=["udp/53"],
        action="permit",
    ),
]

verify_matrix = [
    {
        "sent": dict(
            name="Check allow",
            src_ip="10.1.100.5",
            dst_ip="10.1.200.0",
            dst_port="tcp/www-http",
            action="permit",
        ),
        "received": [{"obj": ("10.1.100.5", "10.1.200.0", "6/80"), "action": "allow"}],
    },
    {
        "sent": dict(
            name="Check Notify",
            src_ip="10.1.100.5",
            dst_ip="10.1.200.0",
            dst_port="tcp/25",
            action="permit",
        ),
        "received": [{"obj": ("10.1.100.5", "10.1.200.0", "6/25"), "action": "notify"}],
    },
    {
        "sent": dict(
            name="Check not found and denied",
            src_ip="10.1.100.5",
            dst_ip="10.1.200.0",
            dst_port="tcp/53",
            action="permit",
        ),
        "received": [{"obj": ("10.1.100.5", "10.1.200.0", "6/53"), "action": "deny"}],
    },
    {
        "sent": dict(
            name="Check not found and denied",
            src_ip=["10.1.100.5", "10.1.100.6"],
            dst_ip="10.1.200.0",
            dst_port="tcp/80",
            action="permit",
        ),
        "received": [
            {"obj": ("10.1.100.5", "10.1.200.0", "6/80"), "action": "allow"},
            {"obj": ("10.1.100.6", "10.1.200.0", "6/80"), "action": "allow"},
        ],
    },
    {
        "sent": dict(
            name="Nothing found",
            src_ip="1.1.1.1",
            dst_ip="2.2.2.2",
            dst_port="tcp/53",
            action="permit",
        ),
        "received": [{"obj": ("1.1.1.1", "2.2.2.2", "6/53"), "action": "deny"}],
    },
]

verify_schema = [
    {
        "sent": dict(
            name="Bad IP",
            src_ip="10.1.100.A",
            dst_ip="10.1.200.0",
            dst_port="tcp/www-http",
            action="permit",
        ),
    },
    {
        "sent": dict(
            name="Bad port",
            src_ip="10.1.100.5",
            dst_ip="10.1.200.0",
            dst_port="tcp25",
            action="permit",
        ),
    },
    {
        "sent": dict(
            name="Bad IP in list",
            src_ip=["10.1.100.5", "10.1.100.A"],
            dst_ip="10.1.200.0",
            dst_port="tcp/25",
            action="permit",
        ),
    },
]

verify_schema2 = [
    {
        "sent": dict(
            name="Check allow",
            src_ip="10.1.100.1",
            dst_ip="10.1.200.0",
            dst_port="6/www-http",
            action=100,
        ),
    },
]

IP_DEFINITIONS = {
    "red": ["10.1.100.0/23", "10.1.102.0/24"],
    "blue": ["10.1.200.0/23", "10.1.202.0/24"],
    "orange": ["10.1.0.0/23", "10.1.2.0/24"],
}

MATRIX = {
    "red": {"blue": {"allow": ["6/80", "6/443"], "notify": ["6/25"]}, "orange": {"allow": ["6/80"]}},
    "blue": {"red": {"allow": ["6/80"]}},
}


class TestMatrix(acl.ACLRule):
    """ACLRule inherited class to test the matrix."""

    matrix = MATRIX
    matrix_enforced = True
    matrix_definition = IP_DEFINITIONS


class TestSchema(acl.ACLRule):
    """ACLRule inherited class to test the schema."""

    input_data_verify = True


class TestSchema2(acl.ACLRule):
    """ACLRule inherited class alternate to test the schema."""

    result_data_verify = True


@pytest.mark.parametrize("data", verify_acl)
def test_verify_acl(data):
    assert acl.ACLRules(acls).match(data["sent"]) == data["received"]


@pytest.mark.parametrize("data", verify_matrix)
def test_matrix(data):
    assert TestMatrix(data["sent"]).enforce() == data["received"]


@pytest.mark.parametrize("data", verify_schema)
def test_schema(data):
    pytest.importorskip("jsonschema")
    try:
        import jsonschema  # pylint: disable=import-outside-toplevel
    except ImportError:
        pass

    with pytest.raises(jsonschema.exceptions.ValidationError):
        TestSchema(data["sent"])


def test_schema_not_enforced_when_option_not_set():
    try:
        acl.ACLRule(dict(src_ip="10.1.1.1", dst_ip="10.2.2.2", dst_port="tcp/80", action=100))
    except Exception:  # pylint: disable=broad-exception-caught
        assert False, "No error should have been raised"


def test_schema_valid():
    try:
        TestSchema(dict(src_ip="10.1.1.1", dst_ip="10.2.2.2", dst_port="tcp/80", action="permit"))
    except Exception:  # pylint: disable=broad-exception-caught
        assert False, "No error should have been raised"


@pytest.mark.parametrize("data", verify_schema2)
def test_schema2(data):
    pytest.importorskip("jsonschema")
    try:
        import jsonschema  # pylint: disable=import-outside-toplevel
    except ImportError:
        pass

    with pytest.raises(jsonschema.exceptions.ValidationError):
        TestSchema2(data["sent"]).validate()


def test_schema2_valid():
    try:
        TestSchema2(dict(src_ip="10.1.1.1", dst_ip="10.2.2.2", dst_port="tcp/80", action="permit")).validate()
    except Exception:  # pylint: disable=broad-exception-caught
        assert False, "No error should have been raised"


class TestAddrGroups(acl.ACLRule):
    """ACLRule inherited class alternate to test expansions."""

    address_groups = {"red": ["white", "blue"], "blue": ["cyan"], "yellow": ["orange"]}

    addresses = {"white": ["10.1.1.1", "10.2.2.2"], "cyan": ["10.3.3.3"], "orange": ["10.4.4.4"]}

    def __init__(self, data, *args, **kwargs):
        self.flattened_addresses = self.flatten_addresses(self.address_groups, self.addresses)
        super().__init__(data, *args, **kwargs)

    def flatten_addresses(self, address_groups, addresses):
        """Go through and get the addresses given potential address groups."""

        flattened_addresses = {}

        for group, subgroups in address_groups.items():
            if group in addresses:
                flattened_addresses.setdefault(group, []).extend(addresses[group])
            for subgroup in subgroups:
                if subgroup in addresses:
                    flattened_addresses.setdefault(group, []).extend(addresses[subgroup])
                if subgroup in address_groups:
                    subgroup_addresses = self.flatten_addresses({subgroup: address_groups[subgroup]}, addresses)
                    for sub_group, ips in subgroup_addresses.items():
                        flattened_addresses.setdefault(sub_group, []).extend(ips)
                        if group != sub_group:
                            flattened_addresses.setdefault(group, []).extend(ips)

        return flattened_addresses

    def process_ip(self, ip):
        """Test ability to expand IP for both source and destination."""

        if not isinstance(ip, list):
            ip = [ip]
        output = []
        for ip_name in ip:
            if not ip_name[0].isalpha():
                output.append(ip_name)
            elif self.addresses.get(ip_name):
                output.extend(self.addresses[ip_name])
            elif self.flattened_addresses.get(ip_name):
                output.extend(self.flattened_addresses[ip_name])
        return sorted(list(set(output)))

    def process_src_ip(self, src_ip):
        """Test ability to expand IP for both source."""

        return self.process_ip(src_ip)

    def process_dst_ip(self, dst_ip):
        """Test ability to expand IP for both destination."""

        return self.process_ip(dst_ip)


add_group_check = [
    {
        "sent": dict(
            name="Check allow",
            src_ip=["red", "blue", "10.4.4.4"],
            dst_ip=["white"],
            dst_port="6/www-http",
            action="permit",
        ),
        "received": [
            {"action": "permit", "dst_ip": "10.2.2.2", "dst_port": "6/80", "name": "Check allow", "src_ip": "10.1.1.1"},
            {"action": "permit", "dst_ip": "10.1.1.1", "dst_port": "6/80", "name": "Check allow", "src_ip": "10.2.2.2"},
            {"action": "permit", "dst_ip": "10.1.1.1", "dst_port": "6/80", "name": "Check allow", "src_ip": "10.3.3.3"},
            {"action": "permit", "dst_ip": "10.2.2.2", "dst_port": "6/80", "name": "Check allow", "src_ip": "10.3.3.3"},
            {"action": "permit", "dst_ip": "10.1.1.1", "dst_port": "6/80", "name": "Check allow", "src_ip": "10.4.4.4"},
            {"action": "permit", "dst_ip": "10.2.2.2", "dst_port": "6/80", "name": "Check allow", "src_ip": "10.4.4.4"},
        ],
    }
]


@pytest.mark.parametrize("data", add_group_check)
def test_custom_address_group(data):
    obj = TestAddrGroups(data["sent"])
    assert obj.expanded_rules == data["received"]
