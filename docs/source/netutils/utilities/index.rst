*******************
Netutils Utilities
*******************

Netutils to Jinja2 Filters
============================

In an effort to simplify the process of adding netutils' functions to jinja2 as filters we have created a convenience function. Let's go through how you could add the filters to your jinja2 environment.
Here is the current folder structure.

.. code-block:: python

    .
    ├── jinja2_environment.py
    ├── templates
    └── test.j2

Below is the code in the `test.j2` file.

.. code-block:: jinja

    IP Address + 200 = {{ "192.168.0.1/10" | ip_addition(200) }}

Below is a code in the `jinja2_environment.py` folder.

.. code-block:: python

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

When you run `jinja2_environment.py` the output will be:

.. code-block:: python

    IP Address + 200 = 192.168.0.201


Netutils to Jinja2 Filters List
======================================

The below list shows what jinja2 filters are added when you add them using the process above. The keys of the dictionary are the names you would use to call the jinja2 filter.

.. note::
    The jinja2 filter names match the python function names.

.. exec::
    import json
    from netutils.utils import jinja2_convenience_function
    data = list(jinja2_convenience_function().keys())
    json_obj = json.dumps(data, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    ]"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")


ipaddress Convenience Functions
---------------------------------

When adding the netutils functions to your jinja2 environment, you also gain access to the built-in ipaddress python library using these three jinja2 filters.

.. code-block:: python

    "ipaddress_address": "ip.ipaddress_address",
    "ipaddress_interface": "ip.ipaddress_interface",
    "ipaddress_network": "ip.ipaddress_network",

When using these filters, you must specify an attribute of that given class. Here is an example of how you would use the `version` if the `ipaddress_interface` filter.

.. code-block:: python

    .
    ├── jinja2_environment.py
    └── templates
    └── test.j2

Below is the code in the `test.j2` file.

.. code-block:: jinja

    The version of 192.168.0.1/24 is IPv{{ "192.168.0.1/24" | ipaddress_interface("version") }}.

Below is a code in the `jinja2_environment.py` folder.

.. code-block:: python

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

When you run `jinja2_environment.py` the output will be:

.. code-block:: python

    The version of 192.168.0.1/24 is IPv4.

In Ansible, one can add with the following code by adding to a folder called `filter_plugins` in a file called `nutils.py` as an example.

.. code-block:: python

    from netutils.utils import jinja2_convenience_function

    class FilterModule(object):

        def filters(self):
            return jinja2_convenience_function()