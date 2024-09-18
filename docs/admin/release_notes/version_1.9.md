# v1.9 Release Notes

## Release Overview

- Added NIST URL creation and platform mapper.
- Added DNA Center platform mappings.
- Improved error message when duplicate line is parsed.

## [v1.9.2] 2024-09

### Added
- [534](https://github.com/networktocode/netutils/pull/534) Extend ip_network extension to support method calls with kwargs.

### Changed
- [570](https://github.com/networktocode/netutils/pull/570) OUI File Updates.
- [571](https://github.com/networktocode/netutils/pull/571) PROTOCOL File Updates.

### Fixed

- [569](https://github.com/networktocode/netutils/pull/569) Fix banner parsers auto striping all newlines. Allow newlines in banners.
- [574](https://github.com/networktocode/netutils/pull/574) Fix ntc_template reverse mapping for cisco xe.

## [v1.9.1] 2024-08

### Changed

- [557](https://github.com/networktocode/netutils/pull/557) OUI File Updates.
- [558](https://github.com/networktocode/netutils/pull/558) PROTOCOL File Updates.

### Fixed

- [553](https://github.com/networktocode/netutils/pull/553) Fixes incorrect cisco_xe to ntc-templates library mapping.

## [v1.9.0] 2024-07

### Added

- [489](https://github.com/networktocode/netutils/pull/489) Added NIST URL creation and platform mapper.
- [519](https://github.com/networktocode/netutils/pull/519) Added DNA Center forward and reverse platform mappings.

### Changed

- [539](https://github.com/networktocode/netutils/pull/539) Provide more descriptive error message when duplicate line is parsed.
