# Attribution

The library was built to be a centralized place for common network automation code to be accessed. While in most cases it is difficult, if not impossible to understand the origin of code, the following intends to describe the known motivation for where code was derived from and in the few cases where actual code was directly taken from. Except where noted, all code is believed to be unattributable, from @itdependsnetworks, or from another Network to Code employee. If this is in fact an error, please open an issue, and the proper attribution will be provided. Any errors were not done out of malice, but rather the natural developer workflow of pulling snippets of code from existing locations such as StackOverflow and Github over months and years of development. As an example it is nearly impossible to understand the original author of Cisco type7 encryption/decryption in the sea of available code, and remains unattributable though clearly originally developed prior to this library being created.

Influencers

- [Netmiko](https://github.com/ktbyers/netmiko)
- [NAPALM](https://github.com/napalm-automation/napalm)
- [Ansible](https://github.com/ansible/ansible)
- [IPCal](https://github.com/ammyblabla/ipcal)
- [StackOverflow](https://stackoverflow.com/)
- [Python 3 Docs](https://docs.python.org/3/library/)

In many instances variables and function names were reused, but the code was built from scratch to avoid any potential licensing issues. Functions that were known to be rewritten and their known origin.

| Function            | Origin  |
| ------------------- | ------- |
| asn_to_int          | NAPALM  |
| is_ip               | IPCal   |
| ip_to_bin           | IPCal   |
| get_usable_range    | IPCal   |
| encrypt_cisco_type7 | unknown |
| decrypt_cisco_type7 | unknown |
| vlan_to_list        | Ansible |
| sanitize_config     | NAPALM  |

Relevant PR's

- [NAPALM #493](https://github.com/napalm-automation/napalm/pull/493)
- [Ansible #39901](https://github.com/ansible/ansible/pull/39901)
- [Ansible #26566](https://github.com/ansible/ansible/pull/26566)

In building out the time conversion, the regex patterns are based on NAPALM implementation with their consent.