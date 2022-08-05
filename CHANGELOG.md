# Changelog

## v1.2.0 - 2022-08

### Added

- #128 Documentation for Nokia SROS duplicate lines/duplicate line detection
- #138 Added nxos_ssh to Napalm mapper

### Changed

- #113 Updated lib mapping docs
- #115 Switched build backend to poetry-core
- #121 Update banner parsing for EOS
- #129 Add type hints to the whole project and mypy testing setup and CI
- #134 Updated CODEOWNERS

### Fixed

- #122 Fixed encrypt type7

## v1.1.0 - 2022-04

### Added

- #90 Uptime Conversions.
- #102 Add Ansible mapping for Nokia SrOS.
- #105 Add min_grouping_sizing to vlanlist_to_config method.
- #106 Add Nokia SrOS Config Parser.

### Changed

- #104 Optimize vlanconfig_to_list using builtin Regex methods.

### Fixed

- #99 Fixed decimal place in bits_to_name.
- #107 Fix issue when backup or intended is empty.


## v1.0.0 - 2021-11

### Added

- #69 Normalise banner delimiter for IOS to ^C & support parsing delimiter ^

### Fixed

- #79 F5 parser fix for irules with multiline single command lines.

### Removed

- #83 remove support for old function 'is_fqdn_valid' as prep for 1.0.0

## v0.2.5 - 2021-11

### Added

- #76 Added wrapper for Python ipaddress methods for use with Jinja

### Fixed

- #75 Updated Python requirements to be loosened
- #76 Fixed doc errors with ip methods
- #77 Fixed CI pipeline for docker caching

## v0.2.4 - 2021-11

### Added

- #33 Add interface range compress function
- #53 Add get peer address function
- #59 Add bandwidth converting function
- #65 Added Docker caching
- #68 Add Fortinet Fortios Parser support

### Changed

- #64 CI implementation on GitHub actions

### Fixed

- #52 Update pyproject.toml build-server 
- #55 update version in toml and init files
- #63 Fix lack of zero padding on ip to binary conversion
- #70 Fix lack of zero padding on ip to hex conversion
- #68 Update Black pinning

## v0.2.3 - 2021-09

### Added

- #45 Added a jinja2 convenience function

### Changed

- #46 Updated NAPALM Maps to include community drivers

### Fixed

- #49 Fix read the docs

## v0.2.2 - 2021-09

### Added

- #35 TCP/UDP Mappings
- #31 Interface range expansion
- #28 IPv6 Functionality to IP Module
- #34 Interface sorting

### Changed

- #39 Updated docs to include automation library mappings
- #41 Updated docs to include tcp/udp mappings

### Fixed

- Corrected contribution and attribution docs

## v0.2.1 - 2021-06

### Added

- #16 Cisco ASA Parser.

### Changed

- #17 Update interface mapping for Sync, TenGig, Port-channel.

## v0.2.0 - 2021-06

### Fixed

- Enable docstring tests
- Fix docstring tests
- Fix wording and links on README

### Changed

- Changed name of is_fqdn_valid to is_fqdn_resolvable, prepare to deprecate is_fqdn_valid
- Removed automatic import of all functions on initiation of package
- Moved interface mappings from variables to constants

## v0.1.1 - 2021-05

### Added

- Update travis configuration to release a new version from CI/CD pipeline

## v0.1.0 - 2021-03-19

Initial release
