*******
Configs
*******

.. automodule:: netutils.config.clean
    :members:

.. automodule:: netutils.config.compliance
    :members:

.. automodule:: netutils.config.parser
    :members:

Edge Cases
==============

Fortinet Fortios Parser
-----------------------
- In order to support html blocks that exist in Fortios configurations, some preprocessing is executed, this is a regex that specifically grabs everything between quotes after the 'set buffer' sub-command. It's explicitly looking for double quote followed by a newline ("\n) to end the captured data.  This support for html data will not support any other html that doesn't follow this convention.

F5 Parser
-----------------------
- The "ltm rule" configuration sections are not uniform nor standardized; therefor, these sections are completely removed from the configuration in a preprocessing event.
