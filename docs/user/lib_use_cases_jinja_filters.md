# Netutils to Jinja2 Filters

In an effort to simplify the process of adding netutils' functions to jinja2 as filters we have created a convenience function. Let's go through how you could add the filters to your jinja2 environment.
Here is the current folder structure.

```bash
.
├── jinja2_environment.py
├── templates
└── test.j2
```

Below is the code in the `test.j2` file.

```jinja

IP Address + 200 = {{ "192.168.0.1/10" | ip_addition(200) }}

```
Below is a code in the `jinja2_environment.py` folder.

```python

from jinja2.loaders import FileSystemLoader, PackageLoader
from jinja2 import Environment, PackageLoader, select_autoescape
from netutils.utils import jinja2_convenience_function

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

env.filters.update(jinja2_convenience_function())

template = env.get_template("test.j2")
result = template.render()
print(result)
```

When you run `jinja2_environment.py` the output will be:

```text

IP Address + 200 = 192.168.0.201

```

## Netutils to Ansible Jinja2 Filters

In Ansible, one can add with the following code by adding to a folder called `filter_plugins` in a file called `nutils.py` as an example.

```python
from netutils.utils import jinja2_convenience_function
class FilterModule(object):
    def filters(self):
        return jinja2_convenience_function()
```

## ipaddress Convenience Functions

When adding the netutils functions to your jinja2 environment, you also gain access to the built-in ipaddress python library using these three jinja2 filters.

```python
  "ipaddress_address": "ip.ipaddress_address",
  "ipaddress_interface": "ip.ipaddress_interface",
  "ipaddress_network": "ip.ipaddress_network",
```

When using these filters, you must specify an attribute of that given class. Here is an example of how you would use the `version` if the `ipaddress_interface` filter.

```bash
.
├── jinja2_environment.py
├── templates
└── test.j2
```

Below is the code in the `test.j2` file.

```jinja

The version of 192.168.0.1/24 is IPv{{ "192.168.0.1/24" | ipaddress_interface("version") }}.

```

Below is a code in the `jinja2_environment.py` folder.

```python
from jinja2.loaders import FileSystemLoader, PackageLoader
from jinja2 import Environment, PackageLoader, select_autoescape
from netutils.utils import jinja2_convenience_function

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

env.filters.update(jinja2_convenience_function())

template = env.get_template("test.j2")
result = template.render()
print(result)
```

When you run `jinja2_environment.py` the output will be:

```text
The version of 192.168.0.1/24 is IPv4.
```

## Netutils to Jinja2 Filters List


The below list shows what jinja2 filters are added when you add them using the process above. The keys of the dictionary are the names you would use to call the jinja2 filter.

!!! note

    The jinja2 filter names match the python function names.

--8<-- "docs/user/include_jinja_list.md"