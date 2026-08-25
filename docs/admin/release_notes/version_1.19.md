# v1.19 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Major features or milestones

<!-- towncrier release notes start -->

## [v1.19.0 (2026-08-25)](https://github.com/networktocode/netutils/releases/tag/v1.19.0)

### Added

- [#596](https://github.com/networktocode/netutils/issues/596) - Added a library mapping for `ncclient` which is used for NETCONF communication.
- [#765](https://github.com/networktocode/netutils/issues/765) - Add a Library Mapper for LibreNMS obtained values in order to map with existing network_drivers.
- [#832](https://github.com/networktocode/netutils/issues/832) - Add bit, Kbit, Mbit to normalize bandwidth utility.
- [#873](https://github.com/networktocode/netutils/issues/873) - Added Aruba AOS-CX support to the Netmiko and Hier Config library mappers.

### Fixed

- [#775](https://github.com/networktocode/netutils/issues/775) - Fixed platform mappings to reconcile Netmiko driver support.
- [#795](https://github.com/networktocode/netutils/issues/795) - Fixed the incorrect running configuration command for `aruba_os`.
- [#833](https://github.com/networktocode/netutils/issues/833) - Fixed typo in Ansible mappings for `dell_os10`.
- [#859](https://github.com/networktocode/netutils/issues/859) - Fixed config parser failing to parse more than three consecutive banners, which caused "Unable to parse banner end." errors on configs with many banners (e.g. Cisco IOS).

### Housekeeping

- [#oui-automation](https://github.com/networktocode/netutils/issues/oui-automation) - Fix OUI automation and CI workflow to auto format.
- Rebaked from the cookie `main`.
- Update the regex for OUI data file gathering.
