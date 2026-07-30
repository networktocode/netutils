
# v1.18 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Added the `sanitize_config_jinja` function to render each replacement as a Jinja2 template. Requires the optional `jinja2` dependency (`pip install netutils[optionals]`).

## [v1.18.0 (2026-07-30)](https://github.com/networktocode/netutils/releases/tag/v1.18.0)

### Added

- [#845](https://github.com/networktocode/netutils/issues/845) - Added `sanitize_config_jinja` to render each replacement as a Jinja2 template. Requires the optional `jinja2` dependency (`pip install netutils[optionals]`).

### Dependencies

- [#845](https://github.com/networktocode/netutils/issues/845) - Added `jinja2` as an optional dependency.
