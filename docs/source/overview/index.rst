*********
Overview
*********

A Python library that is a collection of objects for common network automation tasks.

This library intends to keep the following tenets:

 * Must not be any dependencies required to run the library.
 * May be some dependencies, that will be managed by user in opt in fashion.
 * Shall prefer functional programming over object oriented programming.
 * Shall retain a folder and file structure that is flat.
 * Shall leverage docstrings as the primary documentation mechanism.
 * Must provide examples in every public function.
 * Shall retain a high test coverage.

###################
Function Groupings
###################

Functions are grouped with liked functions, such as IP or MAC address based functions. Included to date are groupings of:

* BGP ASN - Provides the ability to convert BGP ASN from integer to dot notation.
* Configuration
   * Cleaning - Provides the ability to remove or replace lines based on regex matches.
   * Compliance - Provides the ability to compare two configurations to sanely understand the differences.
   * Parsing - Provides the ability to parse configuration for the minor differences that are there.
* DNS - Provides the ability to work with dns, such as validating fqdn is resolvable.
* Interface - Provides the ability to work with interface names, expanding, abbreviating, and spliting the names.
* IP Address - Provides the ability to work with IP addresses, primarily exposing Python `ipaddress` functionality.
* Library Mapper - Provides mappings in expected vendor names between Netmiko, NAPALM, pyntc, ntc-templates, pyats, and scrapli.
* MAC Address - Provides the ability to work with MAC addresses such as validating or converting to integer.
* Password - Provides the ability to compare and encrypt common password schemas such as type5 and type7 Cisco passwords.
* Ping - Provides the ability to ping, currently only tcp ping.
* Protocol Mapper - Provides a mapping for protocol names to numbers and vice versa.
* Route - Provides the ability to provide a list of routes and an IP Address and return the longest prefix matched route.
* Vlans - Provide the ability to convert configuration into lists or lists into configuration.