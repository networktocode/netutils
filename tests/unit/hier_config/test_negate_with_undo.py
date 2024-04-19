import pytest

from netutils.hier_config.host import Host


class TestNegateWithUndo:
    @pytest.fixture(autouse=True)
    def setUpClass(self, options_negate_with_undo):
        self.os = "comware5"
        self.running_config = "test_for_undo\nundo test_for_redo"
        self.generated_config = "undo test_for_undo\ntest_for_redo"
        self.remediation = "undo test_for_undo\ntest_for_redo"
        self.host = Host("example1.rtr", self.os, options_negate_with_undo)

    def test_merge(self):
        self.host.load_running_config(self.running_config)
        self.host.load_generated_config(self.generated_config)
        self.host.remediation_config()
        assert self.remediation == str(self.host.remediation_config())
