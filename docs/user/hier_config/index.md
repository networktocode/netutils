# Introduction

Welcome to the Hierarchical Configuration documentation site. Hierarchical Configuration, also known as `hier_config`, is a python library is able to take a running configuration of a network device, compare it to its intended configuration, and build the remediation steps necessary to bring a device into spec with its intended configuration.

Hierarchical Configuraiton has been used extensively on:

- [x] Cisco IOS
- [x] Cisco IOSXR
- [x] Cisco NXOS
- [x] Arista EOS

However, any NOS that utilizes a CLI syntax that is structured in a similar fasion to IOS should work mostly out of the box.