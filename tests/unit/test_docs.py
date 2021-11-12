"""Test for the sphinx documentation."""
import subprocess
import glob
import os
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
        "start_line": 1,
        "start_value": "# netutils\n",
        "end_line": 33,
        "end_value": "* VLANs - Provide the ability to convert configuration into lists or lists into configuration.\n",
    },
    {
        "name": "installation",
        "start_line": 37,
        "start_value": "Option 1: Install from PyPI.\n",
        "end_line": 47,
        "end_value": "```\n",
    },
    {
        "name": "examples",
        "start_line": 49,
        "start_value": "# Examples\n",
        "end_line": 102,
        "end_value": "These are just some examples of the many functions provided by this library.\n",
    },
    {
        "name": "attribution",
        "start_line": 106,
        "start_value": "The library was built to be a centralized place for common network automation code to be accessed. While in most cases it is\n",
        "end_line": 140,
        "end_value": "* https://github.com/ansible/ansible/pull/26566\n",
    },
    {
        "name": "contribution",
        "start_line": 145,
        "start_value": "Pull requests are welcomed and automatically built and tested against multiple versions of Python through TravisCI.\n",
        "end_line": 228,
        "end_value": "Sign up [here](http://slack.networktocode.com/)\n",
    },
]


with open("README.md", "r") as file:
    README_LIST = file.readlines()
README_LIST.insert(0, "")


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
    assert README_LIST[start_end["start_line"]] == start_end["start_value"]
    assert README_LIST[start_end["end_line"]] == start_end["end_value"]
