# netutils

A Python library that is a collection of objects for common network automation tasks.

This library intends to keep the following tenets:

* Must not be any dependencies required to run the library.
  * May be some optional dependencies, to be managed by the user in opt in fashion.
* Shall prefer functions over classes.
* Shall prefer a folder and file structure that is flat.
* Shall leverage docstrings as the primary documentation mechanism.
  * Must provide examples in every public function.
* Shall retain a high test coverage.

# Function Groupings

Functions are grouped with like functions, such as IP or MAC address based functions. Included to date are groupings of:

* Bandwidth - Provides the ability to convert between various bandwidth values.
* Banner - Provides the ability to normalize the various banner delimiters.
* BGP ASN - Provides the ability to convert BGP ASN from integer to dot notation.
* Configuration
  * Cleaning - Provides the ability to remove or replace lines based on regex matches.
  * Compliance - Provides the ability to compare two configurations to sanely understand the differences.
  * Parsing - Provides the ability to parse configuration for the minor differences that are there.
* DNS - Provides the ability to work with DNS, such as validating that a FQDN is resolvable.
* Interface - Provides the ability to work with interface names, expanding, abbreviating, and splitting the names.
* IP Address - Provides the ability to work with IP addresses, primarily exposing Python `ipaddress` functionality.
* Library Mapper - Provides mappings in expected vendor names between Netmiko, NAPALM, pyntc, ntc-templates, pyats, and scrapli.
* MAC Address - Provides the ability to work with MAC addresses such as validating or converting to integer.
* Password - Provides the ability to compare and encrypt common password schemas such as type5 and type7 Cisco passwords.
* Ping - Provides the ability to ping, currently only tcp ping.
* Protocol Mapper - Provides a mapping for protocol names to numbers and vice versa.
* Route - Provides the ability to provide a list of routes and an IP Address and return the longest prefix matched route.
* Time -Provides the ability to convert between integer time and string times.
* VLANs - Provide the ability to convert configuration into lists or lists into configuration.

# Installation

Option 1: Install from PyPI.

```bash
$ pip install netutils
```

Option 2: Install from a GitHub branch, such as develop as shown below.

```bash
$ pip install git+https://github.com/networktocode/netutils.git@develop
```

# Examples

While all functions come with examples in the docstrings, for quick reference of the types of problems this library intends to
solve the following examples are provided.

The following function will help in deploying list of VLANs and match the configuration style in a standard IOS-like configurations.

```python
>>> from netutils.vlan import vlanlist_to_config
>>>
>>> vlan_cfg = vlanlist_to_config([1, 2, 3, 5, 6, 1000, 1002, 1004, 1006, 1008, 1010, 1012, 1014, 1016, 1018])
>>>
>>> vlan_cfg
["1-3,5,6,1000,1002,1004,1006,1008,1010,1012,1014", "1016,1018"]
>>>
>>> for index, line in enumerate(vlan_cfg):
...     if index == 0:
...         print(f"  switchport trunk allowed vlan {line}")
...     else:
...         print(f"  switchport trunk allowed vlan add {line}")
...
  switchport trunk allowed vlan 1-3,5,6,1000,1002,1004,1006,1008,1010,1012,1014
  switchport trunk allowed vlan add 1016,1018
>>>
```

You may want to compare a known password with a given encrypted password. This can help in verifying if the
passwords are as expected for compliance reasons.

```python
>>> from netutils.password import compare_type5
>>>
>>> compare_type5("cisco","$1$nTc1$Z28sUTcWfXlvVe2x.3XAa.")
True
>>>
>>> compare_type5("not_cisco","$1$nTc1$Z28sUTcWfXlvVe2x.3XAa.")
False
>>>
```

Often times interfaces will come in various different shortened names, and it is helpful to normalize them.

```python
>>> from netutils.interface import canonical_interface_name
>>>
>>> canonical_interface_name("Gi1/0/1")
'GigabitEthernet1/0/1'
>>>
>>> canonical_interface_name("Eth1")
'Ethernet1'
>>>
```

These are just some examples of the many functions provided by this library.

# Attribution

The library was built to be a centralized place for common network automation code to be accessed. While in most cases it is
difficult, if not impossible to understand the origin of code, the following intends to describe the known motivation for where
code was derived from and in the few cases where actual code was directly taken from. Except where noted, all code is believed to
be unattributable, from @itdependsnetworks, or from another Network to Code employee. If this is in fact an error, please open an
issue, and the proper attribution will be provided. Any errors were not done out of malice, but rather the natural developer
workflow of pulling snippets of code from existing locations such as StackOverflow and Github over months and years of development.
As an example it is nearly impossible to understand the original author of Cisco type7 encryption/decryption in the sea of
available code, and remains unattributable though clearly originally developed prior to this library being created.

Influencers
* [Netmiko](https://github.com/ktbyers/netmiko)
* [NAPALM](https://github.com/napalm-automation/napalm)
* [Ansible](https://github.com/ansible/ansible)
* [IPCal](https://github.com/ammyblabla/ipcal)
* [StackOverflow](https://stackoverflow.com/)
* [Python 3 Docs](https://docs.python.org/3/library/)

In many instances variables and function names were reused, but the code was built from scratch to avoid any potential licensing
issues. Functions that were known to be rewritten and their known origin.

| Function | Origin |
| -------- | ------ |
| asn_to_int | NAPALM |
| is_ip | IPCal |
| ip_to_bin | IPCal |
| get_usable_range | IPCal |
| encrypt_type7 | unknown |
| decrypt_type7 | unknown |
| vlan_to_list | Ansible |
| sanitize_config | NAPALM |

Relevant PR's
* https://github.com/napalm-automation/napalm/pull/493
* https://github.com/ansible/ansible/pull/39901
* https://github.com/ansible/ansible/pull/26566

In building out the time conversion, the regex patterns are based on NAPALM implementation with their consent.

# Contributing

Pull requests are welcomed and automatically built and tested against multiple versions of Python through TravisCI.
Except for unit tests, testing is only supported on Python 3.7.

The project is packaged with a light development environment based on `docker-compose` to help with the local development of the project and to run tests within TravisCI.

The project is following Network to Code software development guidelines and are leveraging the following:
- Black, Pylint, Bandit, Mypy, flake8, and pydocstyle for Python linting and formatting.
- pytest, coverage, and unittest for unit tests.

There are a number of things that are required in order to have a successful PR.

- All new functions must contain at least 1 example in their docstrings.
- Docstrings must conform to the google docstring [convention](https://google.github.io/styleguide/pyguide.html#381-docstrings).
- Unit test for newly added functions are required.
- If applicable, tests related to config parsing and compliance must be added.
- Update the jinja2 filter (netutils.utils.jinja2_convenience_function) for any new functions (see below for details).
- If you create a new file in the `netutils` folder, you must create a new folder and `index.rst` in the docs folder (see below for details).
- Your PR must not introduce any required dependencies. You can introduce optional or development dependencies.

## Adding to the jinja2 filter function

To add a new function to the jinja2 filter, add a new entry to the `_JINJA2_FUNCTION_MAPPINGS` located in the `utils.py` file. When adding an entry, the key corresponds with the name to call the function and the value to the path to find the function.

## Adding docs for a new python file

If adding a new python file, the docs must be updated to account for the new file.

1. Create a new folder in `docs/source/netutils` matching the name of your new file.
2. Create an `index.rst` file in that folder.
3. Add the following to the newly created file.

```python
#############################
# ENTER THE TITLE OF THE PAGE
##############################

.. automodule:: netutils.newfile
    :members:
```

## CLI Helper Commands

The project features a CLI helper based on [invoke](http://www.pyinvoke.org/) to help setup the development environment. The commands are listed below in 3 categories:
- `dev environment`
- `utility`
- `testing`

Each command can be executed with `invoke <command>`. Each command also has its own help `invoke <command> --help`

### Local dev environment

```
  build              Build all docker images.
  clean              Remove the project specific image.
  rebuild            Clean the Docker image and then rebuild without using cache.
```

### Utility

```
  clean-docs         Removes the build directory and all of its contents.
  check-pypi-version Verify if the version specified already exists on PyPI.
  cli                Enter the image to perform troubleshooting or dev work.
  html               Creates html docs using sphinx-build command.
```

### Testing

```
  bandit             Run bandit to validate basic static code security analysis.
  black              Run black to check that Python files adhere to its style standards.
  coverage           Run the coverage report against pytest.
  flake8             Run flake8 to check that Python files adhere to its style standards.
  mypy               Run mypy to validate typing-hints.
  pylint             Run pylint code analysis.
  pydocstyle         Run pydocstyle to validate docstring formatting adheres to NTC defined standards.
  pytest             Run pytest for the specified name and Python version.
  tests              Run all tests for the specified name and Python version.
  yamllint           Run yamllint to validate formatting adheres to NTC defined YAML standards.
```

## Questions

Please see [the documentation](https://netutils.readthedocs.io/) for detailed documentation on how to use netutils. For any additional questions or
comments, feel free to swing by the [Network to Code slack channel](https://networktocode.slack.com/) (channel #networktocode).
Sign up [here](http://slack.networktocode.com/)

