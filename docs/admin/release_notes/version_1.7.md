# v1.7 Release Notes

## Release Overview

- Added the ability to hash a value via `hash_data` function.
- Added the ability to sort IPs a value via `get_ips_sorted` function.
- Added lib_mapper entries for `ruckus_smartzone`, `cisco_xe`,  `huawei` and `cisco_xr`.

## [v1.7.0] - 2024-03

### Added

- [#373](https://github.com/networktocode/netutils/pull/373) Added the ability to hash a value via `hash_data` function.
- [#374](https://github.com/networktocode/netutils/pull/374) Added `ruckus_smartzone` to lib_mapper.
- [#451](https://github.com/networktocode/netutils/pull/451) Added `forward` mappings.
- [#473](https://github.com/networktocode/netutils/pull/473) Added the ability to sort IPs a value via `get_ips_sorted` function.

### Changed

- [#369](https://github.com/networktocode/netutils/pull/369) Update doc string example to include the import statement.
- [#429](https://github.com/networktocode/netutils/pull/429) Updated `cisco_xe` mappings.
- [#443](https://github.com/networktocode/netutils/pull/443) Updated `ansible` platform mappers.
- [#466](https://github.com/networktocode/netutils/pull/466) Improve performance of jinja2_convenience_function by not importing NAPALM when called.

### Fixed

- [#429](https://github.com/networktocode/netutils/pull/429) Fixed `huawei` and `cisco_xr` mapping.
- [#445](https://github.com/networktocode/netutils/pull/445) Fixed dual banner issue.
