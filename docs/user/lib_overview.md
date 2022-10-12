# Library Overview

A Python library that is a collection of functions for common network automation tasks.

This library intends to keep the following tenets:

- Must not be any dependencies required to run the library.
    - May be some optional dependencies, to be managed by the user in opt in fashion.
- Shall prefer functions over classes.
- Shall prefer a folder and file structure that is flat.
- Shall leverage docstrings as the primary documentation mechanism.
    - Must provide examples in every public function.
- Shall retain a high test coverage.

## Description/Overview

A Python library that is a collection of functions that are used in the common network automation tasks. Tasks such as converting a BGP ASN to and from dotted format, normalizing an interface name, or "type 5" encrypting a password. The intention is to centralize these functions while keeping the library light.


## Audience (User Personas) - Who should use this Library?

The intended audience is those who are programming network automation tasks with Python. Whether you are a seasoned veteran or a casual scripter, this library should help to reduce duplication between various reinventing the wheel.

## Authors and Maintainers

- @itdependsnetworks
- @jeffkala
- @qduk
- @abates
