# Netutils

<<<<<<< HEAD
=======
<!--
Developer Note - Remove Me!

The README will have certain links/images broken until the PR is merged into `develop`. Update the GitHub links with whichever branch you're using (main etc.) if different.

The logo of the project is a placeholder (docs/images/icon-netutils.png) - please replace it with your app icon, making sure it's at least 200x200px and has a transparent background!

To avoid extra work and temporary links, make sure that publishing docs (or merging a PR) is done at the same time as setting up the docs site on RTD, then test everything.
-->

>>>>>>> 725e2d2 (Cookie updated by NetworkToCode Cookie Drift Manager Tool)
<p align="center">
  <img src="https://raw.githubusercontent.com/networktocode/netutils/develop/docs/images/icon-Netutils.png" class="logo" height="200px">
  <br>
  <a href="https://github.com/networktocode/netutils/actions"><img src="https://github.com/networktocode/netutils/actions/workflows/ci.yml/badge.svg?branch=main"></a>
<<<<<<< HEAD
  <a href="https://netutils.readthedocs.io/en/latest"><img src="https://readthedocs.org/projects/netutils/badge/"></a>
=======
  <a href="https://netutils.readthedocs.io/en/latest/"><img src="https://readthedocs.org/projects/netutils/badge/"></a>
>>>>>>> 725e2d2 (Cookie updated by NetworkToCode Cookie Drift Manager Tool)
  <a href="https://pypi.org/project/netutils/"><img src="https://img.shields.io/pypi/v/netutils"></a>
  <a href="https://pypi.org/project/netutils/"><img src="https://img.shields.io/pypi/dm/netutils"></a>
  <br>
</p>

## Overview

<<<<<<< HEAD
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
=======
> Developer Note: Add a long (2-3 paragraphs) description of what the library does, what problems it solves, etc.

## Documentation

Full documentation for this library can be found over on the [Netutils Docs](https://netutils.readthedocs.io/) website:

- [User Guide](https://netutils.readthedocs.io/user/app_overview/) - Overview, Using the Library, Getting Started.
- [Administrator Guide](https://netutils.readthedocs.io/admin/install/) - How to Install, Configure, Upgrade, or Uninstall the Library.
- [Developer Guide](https://netutils.readthedocs.io/dev/contributing/) - Extending the Library, Code Reference, Contribution Guide.
- [Release Notes / Changelog](https://netutils.readthedocs.io/admin/release_notes/).
- [Frequently Asked Questions](https://netutils.readthedocs.io/user/faq/).

### Contributing to the Documentation

You can find all the Markdown source for the App documentation under the [`docs`](https://github.com/networktocode/netutils/tree/develop/docs) folder in this repository. For simple edits, a Markdown capable editor is sufficient: clone the repository and edit away.

If you need to view the fully-generated documentation site, you can build it with [MkDocs](https://www.mkdocs.org/). A container hosting the documentation can be started using the `invoke` commands (details in the [Development Environment Guide](https://netutils/dev/dev_environment/#docker-development-environment)) on [http://localhost:8001](http://localhost:8001). Using this container, as your changes to the documentation are saved, they will be automatically rebuilt and any pages currently being viewed will be reloaded in your browser.
>>>>>>> 725e2d2 (Cookie updated by NetworkToCode Cookie Drift Manager Tool)

Any PRs with fixes or improvements are very welcome!

## Questions

For any questions or comments, please check the [FAQ](https://netutils.readthedocs.io/en/latest/user/faq/) first. Feel free to also swing by the [Network to Code Slack](https://networktocode.slack.com/) (channel `#networktocode`), sign up [here](http://slack.networktocode.com/) if you don't have an account.
