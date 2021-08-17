"""File used to define sphinx exec directive."""
import sys
from os.path import basename

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from docutils.parsers.rst import Directive
from docutils import nodes, statemachine


class ExecDirective(Directive):
    """Execute the specified python code and insert the output into the document."""

    has_content = True

    def run(self):
        """Function used when adding the directive to an index.rst."""
        old_stdoutout, sys.stdout = sys.stdout, StringIO()

        tab_width = self.options.get("tab-width", self.state.document.settings.tab_width)
        source = self.state_machine.input_lines.source(self.lineno - self.state_machine.input_offset - 1)

        try:
            exec("\n".join(self.content))  # pylint: disable=exec-used
            text = sys.stdout.getvalue()
            lines = statemachine.string2lines(text, tab_width, convert_whitespace=True)
            self.state_machine.insert_input(lines, source)
            return []
        except Exception:  # pylint: disable=W0703
            return [
                nodes.error(
                    None,
                    nodes.paragraph(text="Unable to execute python code at %s:%d:" % (basename(source), self.lineno)),
                    nodes.paragraph(text=str(sys.exc_info()[1])),
                )
            ]
        finally:
            sys.stdout = old_stdoutout


def setup(app):
    """Adds class as sphinx directive."""
    app.add_directive("exec", ExecDirective)
