"""Test for the sphinx documentation."""
import subprocess
import glob
import os
import re
import pytest

UNDOCUMENTED_FILES = ["__init__", "constants", "lib_mapper", "protocol_mapper", "variables"]

SPHINX_DIRECTORIES = [
    {
        "source_dir": "docs/source/",
        "build_dir": "docs/build/",
    }
]

MODULE_FOLDERS = [{"doc_module_folder": "../../docs/source/netutils/", "netutils_module_folder": "../../netutils/"}]

START_END_LINES = [
    {
        "name": "overview",
        "start_value": "# netutils\n",
        "end_value": "* VLANs - Provide the ability to convert configuration into lists or lists into configuration.\n",
    },
    {
        "name": "installation",
        "start_value": "Option 1: Install from PyPI.\n",
        "end_value": "```\n",
    },
    {
        "name": "examples",
        "start_value": "While all functions come with examples in the docstrings, for quick reference of the types of problems this library intends to\n",
        "end_value": "These are just some examples of the many functions provided by this library.\n",
    },
    {
        "name": "attribution",
        "start_value": "The library was built to be a centralized place for common network automation code to be accessed. While in most cases it is\n",
        "end_value": "In building out the time conversion, the regex patterns are based on NAPALM implementation with their consent.\n",
    },
    {
        "name": "contributing",
        "start_value": "Pull requests are welcomed and automatically built and tested against multiple versions of Python through TravisCI.\n",
        "end_value": "Sign up [here](http://slack.networktocode.com/)\n",
    },
]


with open("README.md", "r", encoding="utf-8") as file:
    README_LIST = file.readlines()


def _get_readme_line(folder_name, start_end):

    regex_dict = {"start": r"(:start-line:\s+(?P<value>\d+))", "end": r"(:end-line:\s+(?P<value>\d+))"}
    with open(f"{SPHINX_DIRECTORIES[0]['source_dir']}/{folder_name}/index.rst", "r", encoding="utf-8") as index_file:
        for line in index_file.readlines():
            match = re.search(regex_dict[start_end], line)
            if match:
                break

        if match:
            int_value = int(match.groupdict()["value"])
            return int_value

        raise Exception(
            f"Not able to find {start_end} line value from {SPHINX_DIRECTORIES[0]['source_dir']}/{folder_name}/index.rst. Ensure each line is spelled correctly and exists. "
        )


@pytest.mark.parametrize("data", SPHINX_DIRECTORIES)
def test_sphinx_build(data):
    sphinx_dummy_build = subprocess.run(  # pylint: disable=W1510
        ["sphinx-build", "-b", "dummy", "-W", data["source_dir"], data["build_dir"]], stdout=subprocess.PIPE
    )
    assert sphinx_dummy_build.returncode == 0


@pytest.mark.parametrize("data", MODULE_FOLDERS)
def test_folders_present_for_module(data):
    netutils_modules = [file[15:-3] for file in glob.glob(data["netutils_module_folder"] + "*.py")]
    netutils_modules = list(set(netutils_modules).difference(set(UNDOCUMENTED_FILES)))
    doc_module_folders = [folder[27:-1] for folder in glob.glob(data["doc_module_folder"] + "*/")]

    for module in netutils_modules:
        assert module in doc_module_folders


@pytest.mark.parametrize("data", MODULE_FOLDERS)
def test_folders_contain_index(data):
    doc_module_folders = glob.glob(data["doc_module_folder"])

    for folder in doc_module_folders:
        assert "index.rst" in os.listdir(folder)


@pytest.mark.parametrize("start_end", START_END_LINES, ids=[section["name"] for section in START_END_LINES])
def test_docs_start_end_lines(start_end):
    start_line_value = _get_readme_line(start_end["name"], "start")
    end_line_value = _get_readme_line(start_end["name"], "end")
    assert README_LIST[start_line_value] == start_end["start_value"]
    assert README_LIST[end_line_value - 1] == start_end["end_value"]


def test_docs_start_end_lines_fail():
    end_line_value = _get_readme_line("overview", "end")
    overview = {
        "name": "overview",
        "start_value": "# netutils\n",
        "end_value": "This is what I think the last line of the overview section will be.\n",
    }
    assert README_LIST[end_line_value - 1] != overview["end_value"]
