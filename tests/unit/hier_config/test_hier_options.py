import pytest

from netutils.hier_config.options import options_for, base_options


class TestHConfigOptions:
    @pytest.fixture(autouse=True)
    def setup(self, options_ios, options_junos):
        self.ios_options = options_ios
        self.junos_options = options_junos

    def test_options(self):
        assert self.ios_options == options_for("ios")
        assert self.junos_options == options_for("junos")
        assert {**base_options, **{"style": "example"}} == options_for("example")
