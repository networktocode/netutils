# v1.6 Release Notes

## Release Overview

- Added `ubiquiti_airos` parser.
- Added `ACLRule` and `ACLRules` classes.
- Added `is_ip_range`, `is_ip_within`, `is_network`, and `get_range_ips` functions.
- Added `NETUTILSPARSER_LIB_MAPPER` and `NETUTILSPARSER_LIB_MAPPER_REVERSE` to lib mapper.

## [v1.6.0] - 2023-09

### Added

- [#290](https://github.com/networktocode/netutils/pull/290) Added `ACLRule` and `ACLRules` classes.
- [#290](https://github.com/networktocode/netutils/pull/290) Added `is_ip_range`, `is_ip_within`, `is_network`, and `get_range_ips` functions.
- [#329](https://github.com/networktocode/netutils/pull/329) Added `ubiquiti_airos` parser.
- [#352](https://github.com/networktocode/netutils/pull/352) Added `NETUTILSPARSER_LIB_MAPPER` and `NETUTILSPARSER_LIB_MAPPER_REVERSE` to lib mapper.

### Changed

- [#346](https://github.com/networktocode/netutils/pull/346) Updated `mac_to_format` docs.
- [#352](https://github.com/networktocode/netutils/pull/352) Clean up docs and sorting for lib mapper.
- [#358](https://github.com/networktocode/netutils/pull/358) Changed flatbot schedule.

### Fixed

- [#339](https://github.com/networktocode/netutils/pull/339) Fix for ASN functions.
- [#340](https://github.com/networktocode/netutils/pull/340) Fixed Netscaler parser slug.
- [#346](https://github.com/networktocode/netutils/pull/346) Fix issue where interface abbreviation not working.
- [#350](https://github.com/networktocode/netutils/pull/350) Update library mappings to be correct order.
- [#356](https://github.com/networktocode/netutils/pull/356) Fixed mkdocs dependencies.
