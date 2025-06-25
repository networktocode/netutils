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
            dst_port="80",
            action="permit",
        ),
        "received": True,
    },
    {
        "sent": dict(
            name="Check with number in port definition",
            src_ip="192.168.0.10",
            dst_ip="192.168.250.11",
            dst_port="80",
            action="permit",
        ),
        "received": True,
    },
    {
        "sent": dict(
            name="Check with subnets",
            src_ip="192.168.0.0/25",
            dst_ip="172.16.0.0/24",
            dst_port="80",
            action="permit",
        ),
        "received": True,
    },
    {
        "sent": dict(
            name="Test partial match on Source IP",
            src_ip=["192.168.1.10", "192.168.2.10"],
            dst_ip="172.16.0.11",
            dst_port="80",
            action="permit",
        ),
        "received": False,
    },
    {
        "sent": dict(
            name="Test an entry that is not found",
            src_ip="192.168.1.10",
            dst_ip="192.168.240.1",
            dst_port="80",
            action="permit",
        ),
        "received": False,
    },
    {
        "sent": dict(
            name="Test an action not permit or deny",
            src_ip="10.1.1.1",
            dst_ip="10.255.255.255",
            dst_port="443",
            action="permit",
        ),
        "received": False,
    },
]

acls = [
    dict(
        name="Allow to internal web",
        src_ip=["192.168.0.0/24", "10.0.0.0/16"],
        dst_ip=["172.16.0.0/16", "192.168.250.10-192.168.250.20"],
        dst_port=["80", "53"],
        action="permit",
    ),
    dict(
        name="Allow to internal dns",
        src_ip=["192.168.1.0/24"],
        dst_ip=["172.16.0.0/16"],
        dst_port=["80", "53"],
        action="permit",
    ),
    dict(
        name="Allow to internal https",
        src_ip=["10.0.0.0/8"],
        dst_ip=["172.16.0.0/16"],
        dst_port=["443"],
        action="deny",
    ),
    dict(
        name="Drop (not deny) this specfic packet",
        src_ip="10.1.1.1",
        dst_ip="10.255.255.255",
        dst_port="443",
        action="drop",
    ),
    dict(
        name="Allow External DNS",
        src_ip=["0.0.0.0/0"],
        dst_ip=["8.8.8.8/32", "8.8.4.4/32"],
        dst_port=["53"],
        action="permit",
    ),
]

verify_matrix = [
    {
        "sent": dict(
            name="Check allow",
            src_ip="10.1.100.5",
            dst_ip="10.1.200.0",
            dst_port="80",
            action="permit",
        ),
        "received": [{"obj": ("10.1.100.5", "10.1.200.0", "80"), "action": "allow"}],
    },
    {
        "sent": dict(
            name="Check Notify",
            src_ip="10.1.100.5",
            dst_ip="10.1.200.0",
            dst_port="25",
            action="permit",
        ),
        "received": [{"obj": ("10.1.100.5", "10.1.200.0", "25"), "action": "notify"}],
    },
    {
        "sent": dict(
            name="Check not found and denied",
            src_ip="10.1.100.5",
            dst_ip="10.1.200.0",
            dst_port="53",
            action="permit",
        ),
        "received": [{"obj": ("10.1.100.5", "10.1.200.0", "53"), "action": "deny"}],
    },
    {
        "sent": dict(
            name="Check not found and denied",
            src_ip=["10.1.100.5", "10.1.100.6"],
            dst_ip="10.1.200.0",
            dst_port="80",
            action="permit",
        ),
        "received": [
            {"obj": ("10.1.100.5", "10.1.200.0", "80"), "action": "allow"},
            {"obj": ("10.1.100.6", "10.1.200.0", "80"), "action": "allow"},
        ],
    },
    {
        "sent": dict(
            name="Nothing found",
            src_ip="1.1.1.1",
            dst_ip="2.2.2.2",
            dst_port="53",
            action="permit",
        ),
        "received": [{"obj": ("1.1.1.1", "2.2.2.2", "53"), "action": "deny"}],
    },
]

verify_schema = [
    {
        "sent": dict(
            name="Bad IP",
            src_ip="10.1.100.A",
            dst_ip="10.1.200.0",
            dst_port="80",
            action="permit",
        ),
    },
    {
        "sent": dict(
            name="Bad port",
            src_ip="10.1.100.5",
            dst_ip="10.1.200.0",
            dst_port="5o0",
            action="permit",
        ),
    },
    {
        "sent": dict(
            name="Bad IP in list",
            src_ip=["10.1.100.5", "10.1.100.A"],
            dst_ip="10.1.200.0",
            dst_port="25",
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
            dst_port="80",
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
    "red": {"blue": {"allow": ["80", "443"], "notify": ["25"]}, "orange": {"allow": ["80"]}},
    "blue": {"red": {"allow": ["80"]}},
}


class TestMatrixRule(acl.ACLRule):
    """ACLRule inherited class to test the matrix."""

    class Meta(acl.ACLRule.Meta):  # pylint: disable=too-few-public-methods
        matrix = MATRIX
        matrix_enforced = True
        matrix_definition = IP_DEFINITIONS


class TestSchemaRule(acl.ACLRule):
    """ACLRule inherited class to test the schema."""

    class Meta(acl.ACLRule.Meta):  # pylint: disable=too-few-public-methods
        input_data_verify = True


class TestSchema2Rule(acl.ACLRule):
    """ACLRule inherited class alternate to test the schema."""

    class Meta(acl.ACLRule.Meta):  # pylint: disable=too-few-public-methods
        result_data_verify = True


@pytest.mark.parametrize("data", verify_acl)
def test_verify_acl(data):
    assert acl.ACLRules(acls).match(acl.ACLRule(**data["sent"])) == data["received"]


@pytest.mark.parametrize("data", verify_matrix)
def test_matrix(data):
    assert TestMatrixRule(**data["sent"]).enforce() == data["received"]


@pytest.mark.parametrize("data", verify_schema)
def test_schema(data):
    pytest.importorskip("jsonschema")
    try:
        import jsonschema  # pylint: disable=import-outside-toplevel
    except ImportError:
        pass

    with pytest.raises(jsonschema.exceptions.ValidationError):
        TestSchemaRule(**data["sent"])


def test_schema_not_enforced_when_option_not_set():
    try:
        acl.ACLRule(src_ip="10.1.1.1", dst_ip="10.2.2.2", dst_port="80", action=100)
    except Exception:  # pylint: disable=broad-exception-caught
        assert False, "No error should have been raised"


def test_schema_valid():
    try:
        TestSchemaRule(src_ip="10.1.1.1", dst_ip="10.2.2.2", dst_port="80", action="permit")
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
        TestSchema2Rule(**data["sent"]).validate()


def test_schema2_valid():
    try:
        TestSchema2Rule(src_ip="10.1.1.1", dst_ip="10.2.2.2", dst_port="80", action="permit").validate()
    except Exception:  # pylint: disable=broad-exception-caught
        assert False, "No error should have been raised"


class TestAddrGroups(acl.ACLRule):
    """ACLRule inherited class alternate to test expansions."""

    def __init__(self, **kwargs):
        self._address_groups = {"red": ["white", "blue"], "blue": ["cyan"], "yellow": ["orange"]}
        self._addresses = {"white": ["10.1.1.1", "10.2.2.2"], "cyan": ["10.3.3.3"], "orange": ["10.4.4.4"]}

        self._flattened_addresses = self.flatten_addresses(self._address_groups, self._addresses)

        super().__init__(**kwargs)

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
            elif self._addresses.get(ip_name):
                output.extend(self._addresses[ip_name])
            elif self._flattened_addresses.get(ip_name):
                output.extend(self._flattened_addresses[ip_name])
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
            dst_port="80",
            action="permit",
        ),
        "received": [
            {
                "action": "permit",
                "dst_ip": "10.2.2.2",
                "dst_port": "80",
                "name": "Check allow",
                "src_ip": "10.1.1.1",
                "protocol": None,
                "src_zone": None,
                "dst_zone": None,
            },
            {
                "action": "permit",
                "dst_ip": "10.1.1.1",
                "dst_port": "80",
                "name": "Check allow",
                "src_ip": "10.2.2.2",
                "protocol": None,
                "src_zone": None,
                "dst_zone": None,
            },
            {
                "action": "permit",
                "dst_ip": "10.1.1.1",
                "dst_port": "80",
                "name": "Check allow",
                "src_ip": "10.3.3.3",
                "protocol": None,
                "src_zone": None,
                "dst_zone": None,
            },
            {
                "action": "permit",
                "dst_ip": "10.2.2.2",
                "dst_port": "80",
                "name": "Check allow",
                "src_ip": "10.3.3.3",
                "protocol": None,
                "src_zone": None,
                "dst_zone": None,
            },
            {
                "action": "permit",
                "dst_ip": "10.1.1.1",
                "dst_port": "80",
                "name": "Check allow",
                "src_ip": "10.4.4.4",
                "protocol": None,
                "src_zone": None,
                "dst_zone": None,
            },
            {
                "action": "permit",
                "dst_ip": "10.2.2.2",
                "dst_port": "80",
                "name": "Check allow",
                "src_ip": "10.4.4.4",
                "protocol": None,
                "src_zone": None,
                "dst_zone": None,
            },
        ],
    }
]


@pytest.mark.parametrize("data", add_group_check)
def test_custom_address_group(data):
    obj = TestAddrGroups(**data["sent"])
    assert obj.expanded_rules == data["received"]  # pylint: disable=protected-access
