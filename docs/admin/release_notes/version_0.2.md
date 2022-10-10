# v0.2 Release Notes

## Release Overview

- Update docs, docstrings, and docstring tests
- Changed name of is_fqdn_valid to is_fqdn_resolvable, prepare to deprecate is_fqdn_valid
- Removed automatic import of all functions on initiation of package
- Moved interface mappings from variables to constants

## [v0.2.5] - 2021-11

### Added

- [#76](https://github.com/networktocode/netutils/issues/76) Added wrapper for Python ipaddress methods for use with Jinja

### Fixed

- [#75](https://github.com/networktocode/netutils/issues/75) Updated Python requirements to be loosened
- [#76](https://github.com/networktocode/netutils/issues/76) Fixed doc errors with ip methods
- [#77](https://github.com/networktocode/netutils/issues/77) Fixed CI pipeline for docker caching

## [v0.2.4] - 2021-11

### Added

- [#33](https://github.com/networktocode/netutils/issues/33) Add interface range compress function
- [#53](https://github.com/networktocode/netutils/issues/53) Add get peer address function
- [#59](https://github.com/networktocode/netutils/issues/59) Add bandwidth converting function
- [#65](https://github.com/networktocode/netutils/issues/65) Added Docker caching
- [#68](https://github.com/networktocode/netutils/issues/68) Add Fortinet Fortios Parser support

### Changed

- [#64](https://github.com/networktocode/netutils/issues/64) CI implementation on GitHub actions

### Fixed

- [#52](https://github.com/networktocode/netutils/issues/52) Update pyproject.toml build-server 
- [#55](https://github.com/networktocode/netutils/issues/55) update version in toml and init files
- [#63](https://github.com/networktocode/netutils/issues/63) Fix lack of zero padding on ip to binary conversion
- [#70](https://github.com/networktocode/netutils/issues/70) Fix lack of zero padding on ip to hex conversion
- [#68](https://github.com/networktocode/netutils/issues/68) Update Black pinning

## [v0.2.3] - 2021-09

### Added

- [#45](https://github.com/networktocode/netutils/issues/45) Added a jinja2 convenience function

### Changed

- [#46](https://github.com/networktocode/netutils/issues/46) Updated NAPALM Maps to include community drivers

### Fixed

- [#49](https://github.com/networktocode/netutils/issues/49) Fix read the docs

## [v0.2.2] - 2021-09

### Added

- [#35](https://github.com/networktocode/netutils/issues/35) TCP/UDP Mappings
- [#31](https://github.com/networktocode/netutils/issues/31) Interface range expansion
- [#28](https://github.com/networktocode/netutils/issues/28) IPv6 Functionality to IP Module
- [#34](https://github.com/networktocode/netutils/issues/34) Interface sorting

### Changed

- [#39](https://github.com/networktocode/netutils/issues/39) Updated docs to include automation library mappings
- [#41](https://github.com/networktocode/netutils/issues/41) Updated docs to include tcp/udp mappings

### Fixed

- Corrected contribution and attribution docs

## [v0.2.1] - 2021-06

### Added

- [#16](https://github.com/networktocode/netutils/issues/16) Cisco ASA Parser.

### Changed

- [#17](https://github.com/networktocode/netutils/issues/17) Update interface mapping for Sync, TenGig, Port-channel.

## [v0.2.0] - 2021-06

### Fixed

- Enable docstring tests
- Fix docstring tests
- Fix wording and links on README

### Changed

- Changed name of is_fqdn_valid to is_fqdn_resolvable, prepare to deprecate is_fqdn_valid
- Removed automatic import of all functions on initiation of package
- Moved interface mappings from variables to constants