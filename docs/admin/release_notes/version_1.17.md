
# v1.17 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
