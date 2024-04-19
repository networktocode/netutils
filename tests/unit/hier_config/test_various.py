from netutils.hier_config import HConfig, Host


def test_issue104() -> None:
    running_config_raw = "tacacs-server deadtime 3\n" "tacacs-server host 192.168.1.99 key 7 Test12345\n"
    generated_config_raw = (
        "tacacs-server host 192.168.1.98 key 0 Test135 timeout 3\n"
        "tacacs-server host 192.168.100.98 key 0 test135 timeout 3\n"
    )

    host = Host(hostname="test", os="nxos")
    running_config = HConfig(host=host)
    running_config.load_from_string(running_config_raw)
    generated_config = HConfig(host=host)
    generated_config.load_from_string(generated_config_raw)
    rem = running_config.config_to_get_to(generated_config)
    expected_rem_lines = {
        "no tacacs-server deadtime 3",
        "no tacacs-server host 192.168.1.99 key 7 Test12345",
        "tacacs-server host 192.168.1.98 key 0 Test135 timeout 3",
        "tacacs-server host 192.168.100.98 key 0 test135 timeout 3",
    }
    rem_lines = {line.cisco_style_text() for line in rem.all_children()}
    assert expected_rem_lines == rem_lines


def test_issue_113() -> None:
    running_config_raw = (
        "interface Ethernet1/1\n" "  description test\n" "  ip address 192.0.2.1 255.255.255.0\n" "  switchport\n"
    )
    generated_config_raw = "interface Ethernet1/1\n" "  ip address 192.0.2.1 255.255.255.0\n" "  switchport\n"

    host = Host(hostname="test", os="ios")
    running_config = HConfig(host=host)
    running_config.load_from_string(running_config_raw)
    generated_config = HConfig(host=host)
    generated_config.load_from_string(generated_config_raw)
    rem = running_config.config_to_get_to(generated_config)
    expected_rem_lines = {
        "interface Ethernet1/1",
        "  no description test",
    }
    rem_lines = {line.cisco_style_text() for line in rem.all_children()}
    assert expected_rem_lines == rem_lines
