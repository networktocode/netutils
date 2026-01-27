from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="vlan 10", parents=()),
    ConfigLine(config_line="    name management", parents=("vlan 10",)),
    ConfigLine(config_line="    description management vlan", parents=("vlan 10",)),
    ConfigLine(config_line=" rsa peer-public-key 192.0.2.5", parents=()),
    ConfigLine(config_line="  public-key-code begin", parents=(" rsa peer-public-key 192.0.2.5",)),
    ConfigLine(config_line="   ABCDEF01", parents=(" rsa peer-public-key 192.0.2.5", "  public-key-code begin")),
    ConfigLine(
        config_line="     12345678",
        parents=(" rsa peer-public-key 192.0.2.5", "  public-key-code begin", "   ABCDEF01"),
    ),
    ConfigLine(
        config_line="       A1B2C3D4 E5F6A7B8 C9D0E1F2 1A2B3C4D 5E6F7A8B 9C0D1E2F 3A4B5C6D 7E8F9A0B",
        parents=(" rsa peer-public-key 192.0.2.5", "  public-key-code begin", "   ABCDEF01", "     12345678"),
    ),
    ConfigLine(
        config_line="       C1D2E3F4 A5B6C7D8 E9F0A1B2 3C4D5E6F 7A8B9C0D 1E2F3A4B 5C6D7E8F 9A0B1C2D",
        parents=(" rsa peer-public-key 192.0.2.5", "  public-key-code begin", "   ABCDEF01", "     12345678"),
    ),
    ConfigLine(
        config_line="       1A2B3C4D 5E6F7A8B 9C0D1E2F 3A4B5C6D 7E8F9A0B C1D2E3F4 A5B6C7D8 E9F0A1B2",
        parents=(" rsa peer-public-key 192.0.2.5", "  public-key-code begin", "   ABCDEF01", "     12345678"),
    ),
    ConfigLine(
        config_line="       3C4D5E6F 7A8B9C0D 1E2F3A4B 5C6D7E8F 9A0B1C2D 1A2B3C4D 5E6F7A8B 9C0D1E2F",
        parents=(" rsa peer-public-key 192.0.2.5", "  public-key-code begin", "   ABCDEF01", "     12345678"),
    ),
    ConfigLine(
        config_line="       8A9B0C1D 2E3F4A5B 6C7D8E9F 0A1B2C3D 4E5F6A7B 8C9D0E1F 2A3B4C5D 6E7F8A9B",
        parents=(" rsa peer-public-key 192.0.2.5", "  public-key-code begin", "   ABCDEF01", "     12345678"),
    ),
    ConfigLine(
        config_line="       0C1D2E3F 4A5B6C7D 8E9F0A1B 2C3D4E5F 6A7B8C9D 0E1F2A3B 4C5D6E7F 8A9B0C1D",
        parents=(" rsa peer-public-key 192.0.2.5", "  public-key-code begin", "   ABCDEF01", "     12345678"),
    ),
    ConfigLine(
        config_line="       2E3F4A5B 6C7D8E9F 0A1B2C3D 4E5F6A7B 8C9D0E1F 2A3B4C5D 6E7F8A9B 0C1D2E3F",
        parents=(" rsa peer-public-key 192.0.2.5", "  public-key-code begin", "   ABCDEF01", "     12345678"),
    ),
    ConfigLine(
        config_line="       1B2C3D4E 5F6A7B8C 9D0E1F2A 3B4C5D6E 7F8A9B0C 1D2E3F4A 5B6C7D8E 9F0A1B2C",
        parents=(" rsa peer-public-key 192.0.2.5", "  public-key-code begin", "   ABCDEF01", "     12345678"),
    ),
    ConfigLine(
        config_line="     8810", parents=(" rsa peer-public-key 192.0.2.5", "  public-key-code begin", "   ABCDEF01")
    ),
    ConfigLine(
        config_line="       FACED",
        parents=(" rsa peer-public-key 192.0.2.5", "  public-key-code begin", "   ABCDEF01", "     8810"),
    ),
    ConfigLine(config_line="  public-key-code end", parents=(" rsa peer-public-key 192.0.2.5",)),
    ConfigLine(config_line=" peer-public-key end", parents=(" rsa peer-public-key 192.0.2.5",)),
    ConfigLine(config_line="sysname NTC-Router", parents=()),
]
