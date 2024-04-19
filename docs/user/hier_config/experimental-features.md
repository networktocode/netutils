# Experimental Features

Experimental features are those features that work, but haven't been thoroughly tested enough to feel confident to use in production.

## Rollback Configuration

Starting in version 2.0.2, a featured called rollback configuraiton was introduced. The rollback configuration is exactly what it sounds like. It renders a rollback configuration in the event that a remediation causes a hiccup when being deployed. The rollback configuration does the inverse on a remediation. Instead of a remediation being renedered based upon the generated config, a rollback remediation is rendered from the generated config based upon the running configuration.

A rollback configuration can be rendered once the running and generated configurations are loaded. Below is an example.

```bash
>>> from netutils.hier_config import Host
>>> host = Host(hostname="aggr-example.rtr", os="ios")
>>> host.load_running_config_from_file("./tests/fixtures/running_config.conf")
>>> host.load_generated_config_from_file("./tests/fixtures/generated_config.conf")
>>> rollback = host.rollback_config()
>>> for line in rollback.all_children_sorted():
...     print(line.cisco_style_text())
... 
no vlan 4
no interface Vlan4
vlan 3
  name switch_mgmt_10.0.4.0/24
interface Vlan2
  no mtu 9000
  no ip access-group TEST in
  shutdown
interface Vlan3
  description switch_mgmt_10.0.4.0/24
  ip address 10.0.4.1 255.255.0.0
>>> 
```


## Unified diff

Starting in version 2.1.0, a featured called unified diff was introduced. It provides a similar output to difflib.unified_diff() but is aware of out of order lines and the parent child relationships present in the hier_config model of the configurations being diffed.  

This feature is useful in cases where you need to compare the differences of two network device configurations. Such as comparing the configs of redundant device pairs. Or, comparing running and intended configs. 

In its current state, this algorithm does not consider duplicate child differences. e.g. two instances `endif` in an IOS-XR route-policy. It also does not respect the order of commands where it may count, such as in ACLs. In the case of ACLs, they should contain sequence numbers if order is important.

```bash
In [1]: list(running_config.unified_diff(generated_config))
Out[1]:
['vlan 3',
 '  - name switch_mgmt_10.0.4.0/24',
 '  + name switch_mgmt_10.0.3.0/24',
 'interface Vlan2',
 '  - shutdown',
 '  + mtu 9000',
 '  + ip access-group TEST in',
 '  + no shutdown',
 'interface Vlan3',
 '  - description switch_mgmt_10.0.4.0/24',
 '  - ip address 10.0.4.1 255.255.0.0',
 '  + description switch_mgmt_10.0.3.0/24',
 '  + ip address 10.0.3.1 255.255.0.0',
 '+ vlan 4',
 '  + name switch_mgmt_10.0.4.0/24',
 '+ interface Vlan4',
 '  + mtu 9000',
 '  + description switch_mgmt_10.0.4.0/24',
 '  + ip address 10.0.4.1 255.255.0.0',
 '  + ip access-group TEST in',
 '  + no shutdown']
```
        


## Future Config

Starting in version 2.2.0, a featured called future config was introduced. It attempts to predict the running config after a change is applied.

This feature is useful in cases where you need to determine what the configuration state will be after a change is applied. Such as:
- Ensuring that a configuration change was applied successfully to a device.
  - i.e. Does the post-change config match the predicted future config?
- Providing a future state config that can be fed into batfish, or similar, to predict if a change will cause an impact.
- Building rollback configs. If you have the future config state, then generating a rollback config can be done by simply building the remediation config in the reverse direction `rollback = future.config_to_get_to(running)`.
  - If you are building rollbacks for a series of config changes, you can feed the post-change-1 future config into the process for determining the post-change-2 future config e.g. 
      ```shell
      post_change_1_config = running_config.future(change_1_config)
      change_1_rollback_config = post_change_1_config.config_to_get_to(running_config)
      post_change_2_config = post_change_1_config.future(change_2_config)
      change_2_rollback_config = post_change_2_config.config_to_get_to(post_change_1_config)
      ...
      ```

In its current state, this algorithm does not consider:
- negate a numbered ACL when removing an item
- sectional exiting
- negate with
- idempotent command blacklist
- idempotent_acl_check
- and likely others

```bash
In [1]: from netutils.hier_config import HConfig, Host
   ...:
   ...:
   ...: host = Host("test.dfw1", "ios")
   ...: running_config = HConfig(host)
   ...: running_config.load_from_file("./tests/fixtures/running_config.conf")
   ...: remediation_config = HConfig(host)
   ...: remediation_config.load_from_file("./tests/fixtures/remediation_config_without_tags.conf")
   ...: future_config = running_config.future(remediation_config)
   ...:
   ...: print("\n##### running config")
   ...: for line in running_config.all_children():
   ...:     print(line.cisco_style_text())
   ...:
   ...: print("\n##### remediation config")
   ...: for line in remediation_config.all_children():
   ...:     print(line.cisco_style_text())
   ...:
   ...: print("\n##### future config")
   ...: for line in future_config.all_children():
   ...:     print(line.cisco_style_text())
   ...:

##### running config
hostname aggr-example.rtr
ip access-list extended TEST
  10 permit ip 10.0.0.0 0.0.0.7 any
vlan 2
  name switch_mgmt_10.0.2.0/24
vlan 3
  name switch_mgmt_10.0.4.0/24
interface Vlan2
  descripton switch_10.0.2.0/24
  ip address 10.0.2.1 255.255.255.0
  shutdown
interface Vlan3
  mtu 9000
  description switch_mgmt_10.0.4.0/24
  ip address 10.0.4.1 255.255.0.0
  ip access-group TEST in
  no shutdown

##### remediation config
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

##### future config
vlan 3
  name switch_mgmt_10.0.3.0/24
vlan 4
  name switch_mgmt_10.0.4.0/24
interface Vlan2
  mtu 9000
  ip access-group TEST in
  descripton switch_10.0.2.0/24
  ip address 10.0.2.1 255.255.255.0
interface Vlan3
  description switch_mgmt_10.0.3.0/24
  ip address 10.0.3.1 255.255.0.0
  mtu 9000
  ip address 10.0.4.1 255.255.0.0
  ip access-group TEST in
  no shutdown
interface Vlan4
  mtu 9000
  description switch_mgmt_10.0.4.0/24
  ip address 10.0.4.1 255.255.0.0
  ip access-group TEST in
  no shutdown
hostname aggr-example.rtr
ip access-list extended TEST
  10 permit ip 10.0.0.0 0.0.0.7 any
vlan 2
  name switch_mgmt_10.0.2.0/24
```

## JunOS-style Syntax Remediation
"set" based operating systems can now be remediated in experimental capacity. Here is an example of a JunOS style remediation.

```
$ cat ./tests/fixtures/running_config_flat_junos.confset system host-name aggr-example.rtr

set firewall family inet filter TEST term 1 from source-address 10.0.0.0/29
set firewall family inet filter TEST term 1 then accept

set vlans switch_mgmt_10.0.2.0/24 vlan-id 2
set vlans switch_mgmt_10.0.2.0/24 l3-interface irb.2

set vlans switch_mgmt_10.0.4.0/24 vlan-id 3
set vlans switch_mgmt_10.0.4.0/24 l3-interface irb.3

set interfaces irb unit 2 family inet address 10.0.2.1/24
set interfaces irb unit 2 family inet description "switch_10.0.2.0/24"
set interfaces irb unit 2 family inet disable

set interfaces irb unit 3 family inet address 10.0.4.1/16
set interfaces irb unit 3 family inet filter input TEST
set interfaces irb unit 3 family inet mtu 9000
set interfaces irb unit 3 family inet description "switch_mgmt_10.0.4.0/24"


$ python3
Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import yaml
>>> from netutils.hier_config import Host
>>>
>>> host = Host('example.rtr', 'junos')
>>> 
>>> # Build Hierarchical Configuration object for the Running Config
>>> host.load_running_config_from_file("./tests/fixtures/running_config_flat_junos.conf")
>>> 
>>> # Build Hierarchical Configuration object for the Generated Config
>>> host.load_generated_config_from_file("./tests/fixtures/generated_config_flat_junos.conf")
>>> 
>>> # Build and Print the all lines of the remediation config
>>> print(host.remediation_config_filtered_text({}, {}))
delete vlans switch_mgmt_10.0.4.0/24 vlan-id 3
delete vlans switch_mgmt_10.0.4.0/24 l3-interface irb.3
delete interfaces irb unit 2 family inet disable
delete interfaces irb unit 3 family inet address 10.0.4.1/16
delete interfaces irb unit 3 family inet description "switch_mgmt_10.0.4.0/24"
set vlans switch_mgmt_10.0.3.0/24 vlan-id 3
set vlans switch_mgmt_10.0.3.0/24 l3-interface irb.3
set vlans switch_mgmt_10.0.4.0/24 vlan-id 4
set vlans switch_mgmt_10.0.4.0/24 l3-interface irb.4
set interfaces irb unit 2 family inet filter input TEST
set interfaces irb unit 2 family inet mtu 9000
set interfaces irb unit 3 family inet address 10.0.3.1/16
set interfaces irb unit 3 family inet description "switch_mgmt_10.0.3.0/24"
set interfaces irb unit 4 family inet address 10.0.4.1/16
set interfaces irb unit 4 family inet filter input TEST
set interfaces irb unit 4 family inet mtu 9000
set interfaces irb unit 4 family inet description "switch_mgmt_10.0.4.0/24"
```

Configurations loaded into Hier Config as Juniper-style syntax are converted to a flat `set` based configuration format. Remediations are then rendered using this `set` style syntax.

```
$ cat ./tests/fixtures/running_config_junos.conf 
system {
    host-name aggr-example.rtr;
}

firewall {
    family inet {
        filter TEST {
            term 1 {
                from {
                    source-address 10.0.0.0/29;
                }
                then {
                    accept;
                }
            }
        }
    }
}

vlans {
    switch_mgmt_10.0.2.0/24 {
        vlan-id 2;
        l3-interface irb.2;
    }
    switch_mgmt_10.0.4.0/24 {
        vlan-id 3;
        l3-interface irb.3;
    }
}

interfaces {
    irb {
        unit 2 {
            family inet {
                address 10.0.2.1/24;
                description "switch_10.0.2.0/24";
                disable;
            }
        }
        unit 3 {
            family inet {
                address 10.0.4.1/16;
                filter {
                    input TEST;
                }
                mtu 9000;
                description "switch_mgmt_10.0.4.0/24";
            }
        }
    }
}

$ python3
Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import yaml
>>> from netutils.hier_config import Host
>>> 
>>> host = Host('example.rtr', 'junos')
>>> 
>>> # Build Hierarchical Configuration object for the Running Config
>>> host.load_running_config_from_file("./tests/fixtures/running_config_junos.conf")
>>> 
>>> # Build Hierarchical Configuration object for the Generated Config
>>> host.load_generated_config_from_file("./tests/fixtures/generated_config_junos.conf")
>>> 
>>> # Build and Print the all lines of the remediation config
>>> print(host.remediation_config_filtered_text({}, {}))
delete vlans switch_mgmt_10.0.4.0/24 vlan-id 3
delete vlans switch_mgmt_10.0.4.0/24 l3-interface irb.3
delete interfaces irb unit 2 family inet description "switch_10.0.2.0/24"
delete interfaces irb unit 2 family inet disable
delete interfaces irb unit 3 family inet address 10.0.4.1/16
delete interfaces irb unit 3 family inet description "switch_mgmt_10.0.4.0/24"
set vlans switch_mgmt_10.0.3.0/24 vlan-id 3
set vlans switch_mgmt_10.0.3.0/24 l3-interface irb.3
set vlans switch_mgmt_10.0.4.0/24 vlan-id 4
set vlans switch_mgmt_10.0.4.0/24 l3-interface irb.4
set interfaces irb unit 2 family inet filter input TEST
set interfaces irb unit 2 family inet mtu 9000
set interfaces irb unit 2 family inet description "switch_mgmt_10.0.2.0/24"
set interfaces irb unit 3 family inet address 10.0.3.1/16
set interfaces irb unit 3 family inet description "switch_mgmt_10.0.3.0/24"
set interfaces irb unit 4 family inet address 10.0.4.1/16
set interfaces irb unit 4 family inet filter input TEST
set interfaces irb unit 4 family inet mtu 9000
set interfaces irb unit 4 family inet description "switch_mgmt_10.0.4.0/24"
```