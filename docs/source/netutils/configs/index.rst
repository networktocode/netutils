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

Fortinet FortiOS Parser
-----------------------
- To support HTML blocks that exist in FortiOS configurations, some preprocessing via a regex is performed that specifically grabs everything between quotes after the 'set buffer' sub-command. It is explicitly looking for the double quote followed by a newline ("\n) to end the captured data. This support for HTML data will not support any other HTML that doesn't follow this convention.

F5 Parser
-----------------------
- The "ltm rule" configuration sections are not uniform nor standardized; therefore, these sections are completely removed from the configuration in a preprocessing event.

Nokia SrOS Parser
-----------------

- The parser depends upon the configuration presented in backups being in the "info" format as opposed to the indented MD-CLI format.
