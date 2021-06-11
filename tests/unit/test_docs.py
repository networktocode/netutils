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
        "overview": {
            "start_line": 0,
            "start_value": "# netutils\n",
            "end_line": 32,
            "end_value": "* VLANs - Provide the ability to convert configuration into lists or lists into configuration.\n",
        },
    },
    {
        "attribution": {
            "start_line": 91,
            "start_value": "The library was built to be a centralized place for common network automation code to be accessed. While in most cases it is\n",
            "end_line": 125,
            "end_value": "* https://github.com/ansible/ansible/pull/26566\n",
        },
    },
    {
        "contribution": {
            "start_line": 130,
            "start_value": "Pull requests are welcomed and automatically built and tested against multiple versions of Python through TravisCI.\n",
            "end_line": 177,
            "end_value": "Sign up [here](http://slack.networktocode.com/)\n",
        }
    },
]


@pytest.fixture
def load_readme_into_lines():
    """Loads README.md file into a list of lines."""
    with open("README.md", "r") as file:
        return file.readlines()


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


@pytest.mark.parametrize("start_end", START_END_LINES, ids=[list(x.keys())[0] for x in START_END_LINES])
def test_docs_start_end_lines(start_end, load_readme_into_lines):  # pylint: disable=redefined-outer-name
    readme_data = load_readme_into_lines
    section = list(start_end.keys())[0]
    assert readme_data[start_end[section]["start_line"]] == start_end[section]["start_value"]
    assert readme_data[start_end[section]["end_line"]] == start_end[section]["end_value"]
