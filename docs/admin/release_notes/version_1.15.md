
# v1.15 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Add parser support for Rad ETX.
- Update the library to the NTC 2025 development standards.

<!-- towncrier release notes start -->

## [v1.15.2 (2025-12-31)](https://github.com/networktocode/netutils/releases/tag/v1.15.2)

### Fixed

- [#723](https://github.com/networktocode/netutils/issues/723) - Fix the GitHub release failures occurring in CI.
- [#741](https://github.com/networktocode/netutils/issues/741) - Fixed the logic error where `salt=0` was ignored in `encrypt_cisco_type7`
- [#750](https://github.com/networktocode/netutils/issues/750) - Fix PAN-OS banner parsing by removing IOS-style banner end normalization.

## [v1.15.1 (2025-10-20)](https://github.com/networktocode/netutils/releases/tag/v1.15.1)

### Added

- [#704](https://github.com/networktocode/netutils/issues/704) - Added show running config mapper for 22 additional operating systems.

## [v1.15.0 (2025-09-05)](https://github.com/networktocode/netutils/releases/tag/v1.15.0)

### Added

- [#692](https://github.com/networktocode/netutils/issues/692) - Add Rad ETX config parser.

### Housekeeping

- [#675](https://github.com/networktocode/netutils/issues/675) - Replaced black, bandit, flake8 and pydocstyle with ruff.
- [#675](https://github.com/networktocode/netutils/issues/675) - Updated tasks.py with newest task list.
- [#675](https://github.com/networktocode/netutils/issues/675) - Updated to using pyinvoke for development environment definition.
- Fix CI for Flatbot to install Ruff and remove black.
