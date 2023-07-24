# Netutils to Jinja2 Filters

In an effort to simplify the process of adding netutils' functions to Jinja2 as filters we have created a convenience function. Let's go through how you could add the filters to your Jinja2 environment.
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

When adding the netutils functions to your Jinja2 environment, you also gain access to the built-in ipaddress python library using these three Jinja2 filters.

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

## regex Convenience Functions

When adding the netutils functions to your Jinja2 environment, you also gain access to the built-in `re` python library using these Jinja2 filters.

```python
    "regex_findall": "regex.regex_findall",
    "regex_match": "regex.regex_match",
    "regex_search": "regex.regex_search",
    "regex_split": "regex.regex_split",
    "regex_sub": "regex.regex_sub",
```

These functions will always return a json serializable object and not a complex object like `re.Match` or similar to better serve the primary use case of functions to be used as Jinja2 filters. After all, they are simply small wrappers around Python `re` functions, the Python provided `re` functionality should be preferred when not using Jinja2 or similar templating language.

Below is code that you can drop into your Python shell to help bring to life how these regex functions can be used.

```python
from jinja2 import Environment, BaseLoader
from netutils.utils import jinja2_convenience_function

env = Environment(loader=BaseLoader())
env.filters.update(jinja2_convenience_function())

DATA = {
    "device": "USSCAMS07", 
    "comma_seperated_devices": "NYC-RT01,NYC-RT02,SFO-SW01,SFO-RT01"
}

TEMPLATE_STRING = """
{% set device_details = '([A-Z]{2})([A-Z]{2})([A-Z]{3})(\d*)' | regex_match(device) %}

Country: {{ ('^([A-Z]{2})([A-Z]{2})([A-Z]{3})(\d*)' | regex_search(device))[0] }}
STATE: {{ device_details[1] }}
FUNCTION: {{ device_details[2] }}

ALL DEVICES:
{% for router in ',' | regex_split(comma_seperated_devices) -%}
  - {{ router }}
{% endfor %}

ONLY ROUTERS:
{% for router in ',' | regex_split(comma_seperated_devices) -%}
{% if '-RT' | regex_search(router) -%}
  - {{ router }}
{% endif -%}
{% endfor %}
"""

template = env.from_string(TEMPLATE_STRING, DATA)
result = template.render()
print(result)
```

Which would result in the following output.

```text
Country: US
STATE: SC
FUNCTION: AMS

ALL DEVICES:
- NYC-RT01
- NYC-RT02
- SFO-SW01
- SFO-RT01

ONLY ROUTERS:
- NYC-RT01
- NYC-RT02
- SFO-RT01
```

## Netutils to Jinja2 Filters List


The below list shows what jinja2 filters are added when you add them using the process above. The keys of the dictionary are the names you would use to call the jinja2 filter.

!!! note

    The Jinja2 filter names match the python function names.

--8<-- "docs/user/include_jinja_list.md"