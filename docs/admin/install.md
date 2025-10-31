# Installation

Option 1: Install from PyPI.

```bash
$ pip install netutils
```

Option 2: Install from PyPI with optional requirements.

```bash
$ pip install netutils[napalm]
pip install netutils
```

Option 3: Manually install via Poetry.

```bash
git clone https://github.com/networktocode/netutils.git
cd netutils
curl -sSL https://install.python-poetry.org | python3 -
poetry install
```

Option 4: Install from a GitHub branch, such as develop as shown below.

```bash
$ pip install git+https://github.com/networktocode/netutils.git@develop
```

### Optional Dependencies
One of the requirements of this library is to avoid having dependencies; however, including a few optional dependencies in an opt in fashion allows `netutils` to remain lean while offering some powerful addons.

Installing the optional dependencies is only needed when the user needs access to the functions using the dependencies. As an example `get_napalm_getters()` which will provide a mapping of available NAPALM getters based on currently installed NAPALM libraries, if NAPALM is not installed the function simply raises an exception and warns the user that the library is not installed.
