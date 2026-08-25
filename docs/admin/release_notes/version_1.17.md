
# v1.17 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Add config parsing and update RUNNING_CONFIG_MAPPER for HP Network OS devices.

## [v1.17.3 (2026-07-07)](https://github.com/networktocode/netutils/releases/tag/v1.17.3)

### Added

- [#841](https://github.com/networktocode/netutils/issues/841) - Added TenGigE to TenGigabitEthernet interface mapping in BASE_INTERFACES.
- [#843](https://github.com/networktocode/netutils/issues/843) - Added a PYNTC lib mapper entry mapping the `cisco_xr` network driver to pyntc's `cisco_iosxr_ssh` device type.

## [v1.17.2 (2026-04-02)](https://github.com/networktocode/netutils/releases/tag/v1.17.2)

### Dependencies

- [#827](https://github.com/networktocode/netutils/issues/827) - Update development dependencies.
- [#827](https://github.com/networktocode/netutils/issues/827) - Add support for Python 3.14.

## [v1.17.1 (2026-02-04)](https://github.com/networktocode/netutils/releases/tag/v1.17.1)

### Fixed

- [#803](https://github.com/networktocode/netutils/issues/803) - Fixed an issue where an empty config would raise an error when parsing Palo Alto Networks PanOS.

## [v1.17.0 (2026-01-30)](https://github.com/networktocode/netutils/releases/tag/v1.17.0)

### Added

- [#752](https://github.com/networktocode/netutils/issues/752) - Added custom parsing of HP Network OS devices.
- [#793](https://github.com/networktocode/netutils/issues/793) - Added hp_comware running configuration command to the RUNNING_CONFIG_MAPPER.

### Deprecated

- Deprecated the public HPEConfigParser class in lieu of a private class that should be subclassed for specific HP platforms.

### Fixed

- [#780](https://github.com/networktocode/netutils/issues/780) - Fixed parsing of login banner in Palo Alto Networks config.

### Housekeeping

- Added `--pattern` and `--label` options to the `invoke pytest` task.
