# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# pylint: disable=W,C
import os
import sys
import toml
from jinja2 import Environment, FileSystemLoader


sys.path.insert(0, os.path.abspath("../.."))
from netutils import lib_mapper  # noqa: E402

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath("sphinxext"))
toml_dict = toml.load("../../pyproject.toml")

# -- Project information -----------------------------------------------------

project = toml_dict["tool"]["poetry"]["name"]
copyright = f"{toml_dict['tool']['poetry']['authors'][0]}, 2021"
author = ",".join(toml_dict["tool"]["poetry"]["authors"])

# The full version, including alpha/beta/rc tags
release = toml_dict["tool"]["poetry"]["version"]


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "m2r2", "exec"]

autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
    "special-members": "__init__",
    "undoc-members": True,
}


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


def build_mapping_tables(app):
    """Build the library mappings tables."""
    env = Environment(loader=FileSystemLoader(f"{DIR_PATH}"))
    template_file = env.get_template("table_template.j2")

    LIST_OF_MAP_DICTS = []
    for attr in dir(lib_mapper):
        if (attr.endswith("MAPPER_REVERSE") or attr.endswith("_MAPPER")) and not (
            attr.startswith("_") or attr.startswith("NETMIKO") or attr.startswith("MAIN")
        ):
            LIST_OF_MAP_DICTS.append(attr)

    for dict_name in LIST_OF_MAP_DICTS:
        lib_name = dict_name.split("_")[0]
        filename = f"{lib_name}_reverse" if "REVERSE" in dict_name else lib_name
        headers = ["NORMALIZED", lib_name] if "REVERSE" in dict_name else [lib_name, "NORMALIZED"]
        rendered_template = template_file.render(lib_names=headers, mappings=getattr(lib_mapper, dict_name))
        with open(f"{DIR_PATH}/netutils/lib_mapping/{filename}_table.rst", "w") as table_file:
            table_file.write(rendered_template)


def setup(app):
    """Call methods during builder initiated."""
    app.connect("builder-inited", build_mapping_tables)
