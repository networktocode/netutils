# v1.8 Release Notes

## Release Overview

- Added support for Python 3.12.
- Added local support of `distutils.version` now that Python 3.12 deprecates disutils.
- Added functions `compare_version_loose` and `compare_version_strict` based on `distutils.version`.
- Added function `paloalto_panos_clean_newlines`.
- Added various lib_mapper updates.
- Added HP Comware parser.

## [v1.8.0] 2024-04

### Added

- [#483](https://github.com/networktocode/netutils/pull/483) Added support for Python 3.12.
- [#483](https://github.com/networktocode/netutils/pull/483) Added local support of `distutils.version` now that Python 3.12 deprecates disutils.
- [#490](https://github.com/networktocode/netutils/pull/490) Add JunOS and Vyatta to HierConfig mappers.
- [#416](https://github.com/networktocode/netutils/pull/416) Added `paloalto_panos_clean_newlines` function.
- [#467](https://github.com/networktocode/netutils/pull/467) Added HP Comware parser.

### Changed

- [#485](https://github.com/networktocode/netutils/pull/485) Changed order of changelog menu.
- [#494](https://github.com/networktocode/netutils/pull/494) Changed protocol number import to be dynamic update via flatbot.
- [#495](https://github.com/networktocode/netutils/pull/495) Changed XR mapping, add tests to ensure always using normalized name, various lib_mapper fixes.

### Fixed

- [#496](https://github.com/networktocode/netutils/pull/496) Fixed vyos lib_mapper.
- [#416](https://github.com/networktocode/netutils/pull/416) Fixed for `\n` characters in parsing bug in palo parser.
- [#509](https://github.com/networktocode/netutils/pull/509) Fixed parsing of empty banner, dual banner.
