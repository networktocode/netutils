import itertools
import sys
from html.parser import HTMLParser


class HTMLTableParser(HTMLParser):
    """This class serves as a html table parser. It is able to parse multiple
    tables which you feed in. You can access the result per .tables field.
    """

    def __init__(self, decode_html_entities=False, data_separator=" "):
        HTMLParser.__init__(self)
        self._data_separator = data_separator
        self._in_td = False
        self._in_th = False
        self._current_table = []
        self._current_row = []
        self._current_cell = []
        self.tables = []
        self.named_tables = {}
        self.name = ""

    def handle_starttag(self, tag, attrs):
        """We need to remember the opening point for the content of interest.
        The other tags (<table>, <tr>) are only handled at the closing point.
        """
        if tag == "table":
            name = [a[1] for a in attrs if a[0] == "id"]
            if len(name) > 0:
                self.name = name[0]
        if tag == "td":
            self._in_td = True
        if tag == "th":
            self._in_th = True

    def handle_data(self, data):
        """This is where we save content to a cell"""
        if self._in_td or self._in_th:
            self._current_cell.append(data)

    def handle_endtag(self, tag):
        """Here we exit the tags. If the closing tag is </tr>, we know that we
        can save our currently parsed cells to the current table as a row and
        prepare for a new row. If the closing tag is </table>, we save the
        current table and prepare for a new one.
        """
        if tag == "td":
            self._in_td = False
        elif tag == "th":
            self._in_th = False
        if tag in ["td", "th"]:
            final_cell = self._data_separator.join(self._current_cell).strip()
            self._current_row.append(final_cell)
            self._current_cell = []
        elif tag == "tr":
            self._current_table.append(self._current_row)
            self._current_row = []
        elif tag == "table":
            self.tables.append(self._current_table)
            if len(self.name) > 0:
                self.named_tables[self.name] = self._current_table
            self._current_table = []
            self.name = ""


if __name__ == "__main__":

    print("argv :", sys.argv)

    with open(sys.argv[0], "r") as response:
        response_text = response.read()

    p = HTMLTableParser()
    p.feed(response_text)
    merged = list(itertools.chain(*p.tables[8]))
    cleaned = [result for result in merged if result.strip()]
    done = {cleaned[i]: cleaned[i + 1 : i + 8] for i in range(0, len(cleaned), 8)}

    with open(sys.argv[0], "w") as getters:
        getters.write(str(done))
