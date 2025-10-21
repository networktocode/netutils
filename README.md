<<<<<<< HEAD
# Netutils

<p align="center">
  <img src="https://raw.githubusercontent.com/networktocode/netutils/develop/docs/images/icon-Netutils.png" class="logo" height="200px">
  <br>
  <a href="https://github.com/networktocode/netutils/actions"><img src="https://github.com/networktocode/netutils/actions/workflows/ci.yml/badge.svg?branch=main"></a>
  <a href="https://netutils.readthedocs.io/en/latest"><img src="https://readthedocs.org/projects/netutils/badge/"></a>
  <a href="https://pypi.org/project/netutils/"><img src="https://img.shields.io/pypi/v/netutils"></a>
  <a href="https://pypi.org/project/netutils/"><img src="https://img.shields.io/pypi/dm/netutils"></a>
  <br>
</p>

## Overview

A Python library that is a collection of functions that are used in the common network automation tasks. Tasks such as converting a BGP ASN to and from dotted format, normalizing an interface name, or "type 5" encrypting a password. The intention is to centralize these functions while keeping the library light.

## Documentation

Full web-based HTML documentation for this library can be found over on the [Netutils Docs](https://netutils.readthedocs.io) website:

- [User Guide](https://netutils.readthedocs.io/en/latest/user/lib_overview/) - Overview, Using the library, Getting Started.
- [Administrator Guide](https://netutils.readthedocs.io/en/latest/admin/install/) - How to Install, Configure, Upgrade, or Uninstall the library.
- [Developer Guide](https://netutils.readthedocs.io/en/latest/dev/contributing/) - Extending the library, Code Reference, Contribution Guide.
- [Release Notes / Changelog](https://netutils.readthedocs.io/en/latest/admin/release_notes/).
- [Frequently Asked Questions](https://netutils.readthedocs.io/en/latest/user/faq/).

### Contributing to the Docs

All the Markdown source for the library documentation can be found under the [docs](https://github.com/networktocode/netutils/tree/develop/docs) folder in this repository. For simple edits, a Markdown capable editor is sufficient - clone the repository and edit away.

If you need to view the fully generated documentation site, you can build it with [mkdocs](https://www.mkdocs.org/). A container hosting the docs will be started using the invoke commands (details in the [Development Environment Guide](https://netutils.readthedocs.io/en/latest/dev/dev_environment/#docker-development-environment)) on [http://localhost:8001](http://localhost:8001). As your changes are saved, the live docs will be automatically reloaded.

Any PRs with fixes or improvements are very welcome!

## Questions

For any questions or comments, please check the [FAQ](https://netutils.readthedocs.io/en/latest/user/faq/) first. Feel free to also swing by the [Network to Code Slack](https://networktocode.slack.com/) (channel `#networktocode`), sign up [here](http://slack.networktocode.com/) if you don't have an account.
=======
# netutils

## Documentation

The documentation of each repo and its APIs can be found in the [netutils Page](https://https://networktocode-llc.github.io/netutils). It is created and published by Github actions every time you cut a new release, as long as all tests are passing. The action name is `pages` and can be found in `.github/workflows/ci.yml`.

### Requirements

If you want to build the documentation on a GitHub page:

1. Ensure that all tests are passing.

2. Follow the release and tagging process.

3. Go to the repository "Settings", then go to "Pages", and select the source branch: `ntc-pages`.

---
**NOTE**

The page url uses the repository name to formulate the url: `https://https://networktocode-llc.github.io/{ repo_name }`. For consistency, we recommend that the repository name should be the same as the project slug from the cookie cutter template: `https://https://networktocode-llc.github.io/netutils`

---


### Local Doc Build

If you want to build the documentation locally, follow these steps:

1. Run poetry to install all necessary packages: 

```bash
$ poetry install
$ poetry shell
```

2. Create local docs:

```bash
$ sphinx-build -vvv -b html ./docs public
``

3. Run a local python server to check your documentation rendering:

```bash
cd public
python -m http.server &
```


>>>>>>> c52d641 (Cookie initialy baked by NetworkToCode Cookie Drift Manager Tool)
