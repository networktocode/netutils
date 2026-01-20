
# v1.16 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Add config parsers for Adva and Ciena.
- Update the app with 2026 NTC Development Standards.

## [v1.16.0 (2026-01-20)](https://github.com/networktocode/netutils/releases/tag/v1.16.0)

### Added

- [#748](https://github.com/networktocode/netutils/issues/748) - Added parsing for FSP150F2 and FSP150F3 ADVA AOS device configs.
- [#778](https://github.com/networktocode/netutils/issues/778) - Added ConfigParser class for Ciena SAOS/10 devices.

### Fixed

- [#723](https://github.com/networktocode/netutils/issues/723) - Fixed the GitHub release failures occurring in CI.
- [#741](https://github.com/networktocode/netutils/issues/741) - Fixed the logic error where `salt=0` was ignored in `encrypt_cisco_type7`.
- [#745](https://github.com/networktocode/netutils/issues/745) - Fixed OUI GitHub Actions workflow to correctly fetch and generate OUI mappings.
- [#750](https://github.com/networktocode/netutils/issues/750) - Fixed PAN-OS banner parsing by removing IOS-style banner end normalization.

### Housekeeping

- Rebaked from the cookie `main`.
- Run drift manager to get app updated with NTC standards.
