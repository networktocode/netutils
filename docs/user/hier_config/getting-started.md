# hier_config Up and Running

Hierarchical Configuration doesn't communicate with devices themselves. It simply reads configuration data and creates a remediation plan based on the input from a running config and the input from a generated config.

The very first thing that needs to happen is that a hier_config Host object needs to be initiated for a device. To do this, import the hier_config Host class.

```python
from netutils.hier_config import Host
```

With the Host class imported, it can be utilized to create host objects.

```python
host = Host(hostname="aggr-example.rtr", os="ios")
```

Once a host object has been created, the running configuration and generated configurations of a network device can be loaded into the host object. These configurations can be loaded in two ways. If you already have the configurations loaded as strings in memory, you can load them from the strings.

*Example of loading configs from in memory strings*:
```python

running_config = """hostname aggr-example.rtr
!
ip access-list extended TEST
 10 permit ip 10.0.0.0 0.0.0.7 any
!
vlan 2
 name switch_mgmt_10.0.2.0/24 
!
vlan 3
 name switch_mgmt_10.0.4.0/24
!
interface Vlan2
 descripton switch_10.0.2.0/24 
 ip address 10.0.2.1 255.255.255.0
 shutdown
!
interface Vlan3
 mtu 9000
 description switch_mgmt_10.0.4.0/24
 ip address 10.0.4.1 255.255.0.0
 ip access-group TEST in
 no shutdown"""

generated_config = """hostname aggr-example.rtr
!
ip access-list extended TEST
 10 permit ip 10.0.0.0 0.0.0.7 any
!
vlan 2
 name switch_mgmt_10.0.2.0/24 
!
vlan 3
 name switch_mgmt_10.0.3.0/24
!
vlan 4
 name switch_mgmt_10.0.4.0/24
!
interface Vlan2
 mtu 9000
 descripton switch_10.0.2.0/24 
 ip address 10.0.2.1 255.255.255.0
 ip access-group TEST in
 no shutdown
!
interface Vlan3
 mtu 9000
 description switch_mgmt_10.0.3.0/24
 ip address 10.0.3.1 255.255.0.0
 ip access-group TEST in
 no shutdown
!
interface Vlan4
 mtu 9000
 description switch_mgmt_10.0.4.0/24
 ip address 10.0.4.1 255.255.0.0
 ip access-group TEST in
 no shutdown"""

host.load_running_config(config_text=running_config)
host.load_generated_config(config_text=generated_config)
```

The second method for loading configs into the host object is loading the configs from files.

*Example of loading configs from files.*
```python
host.load_running_config_from_file("./tests/fixtures/running_config.conf")
host.load_generated_config_from_file("./tests/fixtures/generated_config.conf")
```

Once the configs are loaded into the host object, a remediation can be created.

```python
host.remediation_config()
```

`host.remediation_config()` is loaded as a python object. To view the results of the remediation, call the `host.remediation_config_filtered_text(include_tags={}, exclude_tags={})` method.

```python
print(host.remediation_config_filtered_text(include_tags={}, exclude_tags={}))
```

> If you're using the examples from the `/tests/fixtures` folder in the [github](https://github.com/netdevops/hier_config/) repository, you should see an output that resembles:

```text
vlan 3
  name switch_mgmt_10.0.3.0/24
vlan 4
  name switch_mgmt_10.0.4.0/24
interface Vlan2
  mtu 9000
  ip access-group TEST in
  no shutdown
interface Vlan3
  description switch_mgmt_10.0.3.0/24
  ip address 10.0.3.1 255.255.0.0
interface Vlan4
  mtu 9000
  description switch_mgmt_10.0.4.0/24
  ip address 10.0.4.1 255.255.0.0
  ip access-group TEST in
  no shutdown
```
