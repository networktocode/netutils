*****************
Library Mappings
*****************

These dictionaries provide mappings in expected vendor names between Netmiko, NAPALM, pyntc, ntc-templates, pyats, and scrapli.

Napalm Mapper
==============
.. exec::
    import json
    from netutils.lib_mapper import NAPALM_LIB_MAPPER
    json_obj = json.dumps(NAPALM_LIB_MAPPER, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

Reverse Napalm Mapper
=====================
.. exec::
    import json
    from netutils.lib_mapper import NAPALM_LIB_MAPPER_REVERSE
    json_obj = json.dumps(NAPALM_LIB_MAPPER_REVERSE, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

PyNTC Mapper
==============
.. exec::
    import json
    from netutils.lib_mapper import PYNTC_LIB_MAPPER
    json_obj = json.dumps(PYNTC_LIB_MAPPER, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

Reverse PyNTC Mapper
====================
.. exec::
    import json
    from netutils.lib_mapper import PYNTC_LIB_MAPPER_REVERSE
    json_obj = json.dumps(PYNTC_LIB_MAPPER_REVERSE, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

Ansible Mapper
==============
.. exec::
    import json
    from netutils.lib_mapper import ANSIBLE_LIB_MAPPER
    json_obj = json.dumps(ANSIBLE_LIB_MAPPER, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

Reverse Ansible Mapper
======================
.. exec::
    import json
    from netutils.lib_mapper import ANSIBLE_LIB_MAPPER_REVERSE
    json_obj = json.dumps(ANSIBLE_LIB_MAPPER_REVERSE, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

PyATS Mapper
==============
.. exec::
    import json
    from netutils.lib_mapper import PYATS_LIB_MAPPER
    json_obj = json.dumps(PYATS_LIB_MAPPER, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

Reverse PyATS Mapper
====================
.. exec::
    import json
    from netutils.lib_mapper import PYATS_LIB_MAPPER_REVERSE
    json_obj = json.dumps(PYATS_LIB_MAPPER_REVERSE, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

Scrapli Mapper
==============
.. exec::
    import json
    from netutils.lib_mapper import SCRAPLI_LIB_MAPPER
    json_obj = json.dumps(SCRAPLI_LIB_MAPPER, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

Reverse Scrapli Mapper
======================
.. exec::
    import json
    from netutils.lib_mapper import SCRAPLI_LIB_MAPPER_REVERSE
    json_obj = json.dumps(SCRAPLI_LIB_MAPPER_REVERSE, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

NTC Templates Mapper
====================
.. exec::
    import json
    from netutils.lib_mapper import NTCTEMPLATES_LIB_MAPPER
    json_obj = json.dumps(NTCTEMPLATES_LIB_MAPPER, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

Reverse NTC Templates Mapper
============================
.. exec::
    import json
    from netutils.lib_mapper import NTCTEMPLATES_LIB_MAPPER_REVERSE
    json_obj = json.dumps(NTCTEMPLATES_LIB_MAPPER_REVERSE, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")


