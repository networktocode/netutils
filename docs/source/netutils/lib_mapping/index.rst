*****************
Library Mappings
*****************

These dictionaries provide mappings in expected vendor names between Netmiko, NAPALM, pyntc, ntc-templates, pyats, and scrapli. For each non-reversed mapper, the keys of the dictionary represent the driver used for that library while the values represent the "normalized" driver based on netmiko.

These dictionaries allow you to keep your Source of Truth platform data consistent and still easily switch between automation libraries. For example, you may be storing your device platform data in Nautobot. In a Nautobot platform, you can store the NAPALM driver needed for that platform. What if you wanted to write
a python script to leverage the backup capabilities of pyntc? Here's an example of how you could use the following dictionaries to perform mappings from your stored Nautobot NAPALM driver to the pyntc driver needed for your script.

.. code-block:: python

    import pynautobot
    from netutils.lib_mapper import NAPALM_LIB_MAPPER, PYNTC_LIB_MAPPER_REVERSE
    from pyntc import ntc_device as NTC


    # Get device from Nautobot
    nautobot = pynautobot.api(url="http://mynautobotinstance.com",token="mytoken")

    # Get Napalm driver and save for later use.
    device = nautobot.dcim.devices.get(name="mydevice")
    sot_driver = device.platform.napalm_driver


    # Connect to device via Napalm
    driver = napalm.get_network_driver("ios")

    device = driver(
        hostname="device.name",
        username="demo",
        password="secret"
    )

    # Do Napalm tasks

    pyntc_driver = PYNTC_LIB_MAPPER_REVERSE.get(NAPALM_LIB_MAPPER.get(sot_driver))
    net_con = NTC(host=device.name, username="demo", password="secret", device_type=pyntc_driver)

    # Do pyntc tasks

Another use case could be using an example like the above in an Ansible filter. That would allow you to write a filter utilizing whichever automation library you needed without having to store the driver for each one in your Source of Truth.

Napalm Mapper
==============================
.. include:: NAPALM_table.rst

Reverse Napalm Mapper
==============================
.. include:: NAPALM_reverse_table.rst

PyNTC Mapper
==============================
.. include:: PYNTC_table.rst

Reverse PyNTC Mapper
==============================
.. include:: PYNTC_reverse_table.rst

Ansible Mapper
==============================
.. include:: ANSIBLE_table.rst

Reverse Ansible Mapper
==============================
.. include:: ANSIBLE_reverse_table.rst

PyATS Mapper
==============================
.. include:: PYATS_table.rst

Reverse PyATS Mapper
==============================
.. include:: PYATS_reverse_table.rst

Scrapli Mapper
==============================
.. include:: SCRAPLI_table.rst

Reverse Scrapli Mapper
==============================
.. include:: SCRAPLI_reverse_table.rst

NTC Templates Mapper
==============================
.. include:: NTCTEMPLATES_table.rst

Reverse NTC Templates Mapper
==============================
.. include:: NTCTEMPLATES_reverse_table.rst


