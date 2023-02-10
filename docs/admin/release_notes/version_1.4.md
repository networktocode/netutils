# v1.4 Release Notes

## Release Overview

- Added is_classful utility function.
- Added AOS-CX, IOS-XR, MRV_OPTISWITCH, and EXTREME_NETIRON parsers.
- Update flatbot CI process.
- Fix and cleanup tests and parser information.
- Fix tcp_ping behavior.

## [v1.4.1] - 2023-02

### Changed

- [#171](https://github.com/networktocode/netutils/pull/171) Allow protocol mapper to be auto-generated.
- [#197](https://github.com/networktocode/netutils/pull/197) Prepend OUI Flatbot step to delete existing branch.
- [#200](https://github.com/networktocode/netutils/pull/200) Allow bandwith to be represented without "ps" in bandwidth.

### Fixed

- [#206](https://github.com/networktocode/netutils/pull/206) Fix Passwords docs that show ASN details.
- [#209](https://github.com/networktocode/netutils/pull/209) Fixed interface_range_expansion with trailing constant.
- [#210](https://github.com/networktocode/netutils/pull/210) Install black into flat environment, change flat action name.

## [v1.4.0] - 2023-01

### Added

- [#163](https://github.com/networktocode/netutils/pull/163) Added IP `is_classfull` utility function.
- [#172](https://github.com/networktocode/netutils/pull/172) Added Aruba AOS-CX Parser.
- [#177](https://github.com/networktocode/netutils/pull/177) Added IOS-XR Parser.
- [#182](https://github.com/networktocode/netutils/pull/182) Added Mrv Optiswitch Parser.
- [#182](https://github.com/networktocode/netutils/pull/182) Added Extreme Netiron Parser.

### Changed

- [#178](https://github.com/networktocode/netutils/pull/178) Update OUI flatbot CI process.

### Fixed

- [#173](https://github.com/networktocode/netutils/pull/173) Fixes classfull address naming.
- [#183](https://github.com/networktocode/netutils/pull/183) Updates parser folder info, fix aruba tests.
- [#181](https://github.com/networktocode/netutils/pull/181) Fixes incorrect behavior when calling tcp_ping with timeout >= 3.

### Removed

- [#184](https://github.com/networktocode/netutils/pull/184) Removed redundant `__init__` methods on Parser classes.
