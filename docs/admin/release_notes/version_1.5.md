# v1.5 Release Notes

## Release Overview

- Added Mikrotik, fastiron, and Panos parsers.
- Added function to allow conversion crom Panos curly bracket to set format.
- Updated Interface mappings for FourHundredGigabitEthernet and TwoGigabitEthernet.
- Added Encryption/Decryption/Comparison for Cisco & Juniper Type 9.

## Announcements

- Deprecation of compare_type5, compare_type7, encrypt_type7, encrypt_type5, and decrypt_type7 in favor of vendor namespaced functions, such as compare_cisco_type5 and decrypt_cisco_type7 to take place on netutils 2.0.
- Support for Python 3.7 is dropped.

## [v1.5.0] - 2023-07

### Added

- [#223](https://github.com/networktocode/netutils/pull/223) Interface abbreviation for TwoGigabitEthernet.
- [#227](https://github.com/networktocode/netutils/pull/227) Add functions for encrypting and decrypting junipter $9$ type passwords.
- [#244](https://github.com/networktocode/netutils/pull/244) Added Mikrotik RouterOS Parser.
- [#252](https://github.com/networktocode/netutils/pull/252) New lib mapper to translate between normalized network OS names and names used by hier_config.
- [#253](https://github.com/networktocode/netutils/pull/253) Add encrypt_type9 (changed to encrypt_cisco_type9) function to netutils.password.
- [#261](https://github.com/networktocode/netutils/pull/261) Added function get_upgrade_path to provide the step upgrade path of to a new version.
- [#262](https://github.com/networktocode/netutils/pull/262) Added Palo Alto networks panos parser. 
- [#262](https://github.com/networktocode/netutils/pull/262) Added Palo Alto brace to set conversion function. 
- [#264](https://github.com/networktocode/netutils/pull/264) Added Ruckus fastiron parser.
- [#285](https://github.com/networktocode/netutils/pull/285) Added FourHundredGigabitEthernet to REVERSE_MAPPING.

### Changed

- [#213](https://github.com/networktocode/netutils/pull/213) Clarify when Python 3.6 support was dropped.
- [#286](https://github.com/networktocode/netutils/pull/286) Move password helper names to be namespaced with vendor information. Assign new name to old name to not break semver.
- [#317](https://github.com/networktocode/netutils/pull/317) Dropped Python 3.6 and bump version of dev dependencies.


### Fixed

- [#217](https://github.com/networktocode/netutils/pull/217) Moved where deletion of branch took place in workflow.
- [#218](https://github.com/networktocode/netutils/pull/218) Create dependabot.yml to fix itdependsabot.
- [#219](https://github.com/networktocode/netutils/pull/219) Fix vlanlist_to_config failing on empty list.
- [#224](https://github.com/networktocode/netutils/pull/224) Add Interface type for Cisco App-hosting port.
- [#284](https://github.com/networktocode/netutils/pull/284) Add -f to flatbot branch pushes.
- [#304](https://github.com/networktocode/netutils/pull/304) Update hier_config docs and add fastiron to NAPALM mapper.
- [#305](https://github.com/networktocode/netutils/pull/305) Fixed OS Version docs showing in mkdocs.
- [#316](https://github.com/networktocode/netutils/pull/316) Update panos conversion function to strip out `devices localhost.localdomain`.
- [#317](https://github.com/networktocode/netutils/pull/317) Fix Citrix mock tests file location to correctly run.