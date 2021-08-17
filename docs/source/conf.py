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

sys.path.insert(0, os.path.abspath("../.."))
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

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_context = {
    "css_files": [
        "_static/theme_overrides.css",  # override wide tables in RTD theme
        "_static/schema-page.css",  # Add css from jschemer
    ]
}

html_sidebars = {"**": ["globaltoc.html", "relations.html", "sourcelink.html", "searchbox.html"]}
