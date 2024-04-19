# Advanced Topics

## Lineage Rules

Lineage rules are rules that are written in YAML. They allow users to seek out very specific sections of configurations or even seek out very generalized lines within a configuration. For example, suppose you just wanted to seek out interface descriptions. Your lineage rule would look like:

```yaml
- lineage:
  - startswith: interface
  - startswith: description
```

In the above example, a start of a lineage is defined with the **- lineage:** syntax. From there the interface is defined with the **- startswith: interface** syntax under the **- lineage:** umbrella. This tells hier_config to search for any configuration that starts with the string **interface** as the parent of a configuration line. When it finds an **interface** parent, it then looks at any child configuration line of the interface that starts with the string **description**.

With lineage rules, you can get as deep into the children or as shallow as you need. Suppose you want to inspect the existence or absence of http, ssh, snmp, and logging within a configuration. This can be done with a single lineage rule, like so:

```yaml
- lineage:
  - startswith:
    - ip ssh
    - no ip ssh
    - ip http
    - no ip http
    - snmp-server
    - no snmp-server
    - logging
    - no logging
```

Or suppose, you want to inspect whether BGP IPv4 AFIs are activated. You can do this with the following:

```yaml
- lineage:
  - startswith: router bgp
  - startswith: address-family ipv4
  - endswith: activate
```

In the above example, I utilized a different keyword to look for activated BGP neighbors. The keywords that can be utilized within lineage rules are:
- startswith
- endswith
- contains
- equals
- re_search

You can also put all of the above examples together in the same set of lineage rules like so:

```yaml
- lineage:
  - startswith: interface
  - startswith: description
- lineage:
  - startswith:
    - ip ssh
    - no ip ssh
    - ip http
    - no ip http
    - snmp-server
    - no snmp-server
    - logging
    - no logging
- lineage:
  - startswith: router bgp
  - startswith: address-family ipv4
  - endswith: activate
```

When hier_config consumes the lineage rules, it consumes them as a list of lineage rules and processes them individually.

## Working with Tags

With a firm understanding of lineage rules, more complex use cases become available within hier_config. A powerful use case is the ability to tag specific sections of configuration and only display remediations based on those tags. This becomes very handy when you're attempting to execute a maintenance that only targets low risk configuration changes or isolate the more risky configuration changes to scrutinize their execution during a maintenance.

Tagging expands on the use of the lineage rules by creating an **add_tags** keyword to a lineage rule.

Suppose you had a running configuration that had an ntp configuration that looked like:

```text
ntp server 192.0.2.1 prefer version 2
```

However, your intended configuration utilized a publicly available NTP server on the internet:

```text
ip name-server 1.1.1.1
ip name-server 8.8.8.8
ntp server time.nist.gov
```

You could create a lineage rule that targeted that specific remediation like this:

```yaml
- lineage:
  - startswith:
    - ip name-server
    - no ip name-server
    - ntp
    - no ntp
  add_tags: ntp
```

Now we can modify the script above to load the tags and create a remediation of the said tags:

```python
#!/usr/bin/env python3

# Import the hier_config Host library
from netutils.hier_config import Host

# Create a hier_config Host object
host = Host(hostname="aggr-example.rtr", os="ios")

# Load the tagged lineage rules
host.load_tags_from_file("./tests/fixtures/tags_ios.yml")

# Load a running configuration from a file
host.load_running_config_from_file("./tests/fixtures/running_config.conf")

# Load an intended configuration from a file
host.load_generated_config_from_file("./tests/fixtures/generated_config.conf")

# Create the remediation steps
host.remediation_config()

# Display the remediation steps for only the "ntp" tags
print(host.remediation_config_filtered_text(include_tags={"ntp"}, exclude_tags={}))
```

In the script, we made two changes. The first change is to load the tagged lineage rules:
`host.load_tags_from_file("./tests/fixtures/tags_ios.yml")`.
And the second is to filter the remediation steps by only including steps that are tagged with **ntp** via the **include_tags** argument.

The remediation looks like:

```text
no ntp server 192.0.2.1 prefer version 2
ip name-server 1.1.1.1
ip name-server 8.8.8.8
ntp server time.nist.gov
```

## hier_config Options

There are a number of options that can be loaded into hier_config to make it better conform to the nuances of your network device. By default, hier_config loads a set of [sane defaults](https://github.com/netdevops/hier_config/blob/master/hier_config/options.py) for Cisco IOS, IOS XE, IOS XR, NX-OS, and Arista EOS.

Below are the configuration options available for manipulation.

```python
base_options: dict = {
    "style": None,
    "negation": "no",
    "syntax_style": "cisco",
    "sectional_overwrite": [],
    "sectional_overwrite_no_negate": [],
    "ordering": [],
    "indent_adjust": [],
    "parent_allows_duplicate_child": [],
    "sectional_exiting": [],
    "full_text_sub": [],
    "per_line_sub": [],
    "idempotent_commands_blacklist": [],
    "idempotent_commands": [],
    "negation_default_when": [],
    "negation_negate_with": [],
}
```

The default options can be completely overwritten and loaded from a yaml file, or individual components of the options can be manipulated to provide the functionality that is desired.

Here is an example of manipulating the built-in options.

```python
# Import the hier_config Host library
from netutils.hier_config import Host

# Create a hier_config Host object
host = Host(hostname="aggr-example.rtr", os="ios")

# Create an NTP negation ordered lineage rule
ordered_negate_ntp = {"lineage": [{"startswith": ["no ntp"], "order": 700}]}

# Update the hier_config options "ordering" key.
host.hconfig_options["ordering"].append(ordered_negate_ntp)
```

Here is an example of completely overwriting the default options and loading in your own.

```python
# import YAML
import yaml

# Import the hier_config Host library
from netutils.hier_config import Host

# Load the hier_config options into memory
with open("./tests/fixtures/options_ios.yml") as f:
    options = yaml.load(f.read(), Loader=yaml.SafeLoader)

# Create a hier_config Host object
host = Host(hostame="aggr-example.rtr", os="ios", hconfig_options=options)
```

In the following sections, I'll cover the available options.

#### style

The **style** defines the os family. Such as **ios**, **iosxr**, etc.

Example:

```yaml
style: ios
```

#### negation

The **negation** defines how an os handles negation. The default is **no**. However, in some circumstances, the negation method is different. Comware, for instance uses **undo** as the negation method and set based syntax uses **delete** for negation.

```yaml
negation: no
```

#### syntax_style

**syntax_style** is used when using a configuration syntax that is different than Cisco ios-style configuration syntax. The only non-Cisco based syntax supported is **juniper**. Calling the juniper syntax style will call additional parsing methods when loading configurations into memory.

Default:
```yaml
syntax_style: cisco
```

Juniper:
```yaml
syntax_style: juniper
```

#### sectional_overwrite_no_negate

The sectional overwrite with no negate hier_config option will completely overwrite sections of configuration without negating them. This option is often used with the RPL sections of IOS XR devices that require that the entire RPL be re-created when making modifications to them, rather than editing individual lines within the RPL.

An example of sectional overwrite with no negate is:

```yaml
sectional_overwrite_no_negate:
- lineage:
  - startswith: as-path-set
- lineage:
  - startswith: prefix-set
- lineage:
  - startswith: route-policy
- lineage:
  - startswith: extcommunity-set
- lineage:
  - startswith: community-set
```

#### sectional_overwrite

Sectional overwrite is just like sectional overwrite with no negate, except that hier_config will negate a section of configuration and then completely re-create it.

#### ordering

Ordering is one of the most useful hier_config options. This allows you to use lineage rules to define the order in which remediation steps are presented to the user. For the ntp example above, the ntp server was negated (`no ntp server 192.0.2.1`) before the new ntp server was added. In most cases, this wouldn't be advantageous. Thus, ordering can be used to define the proper order to execute commands.

All commands are assigned a default order weight of 500, with a usable order weight of 1 - 999. The smaller the weight value, the higher on the list of steps a command is to be executed. The larger the weight value, the lower on the list of steps a command is to be executed. To create an order in which new ntp servers are added before old ntp servers are removed, you can create an order lineage that weights the negation to the bottom.

Example:

```yaml
ordering:
- lineage:
  - startswith: no ntp
  order: 700
```

With the above order lineage applied, the output of the above ntp example would look like:

```text
ip name-server 1.1.1.1
ip name-server 8.8.8.8
ntp server time.nist.gov
no ntp server 192.0.2.1 prefer version 2
```

#### indent_adjust

coming soon...

#### parent_allows_duplicate_child

coming soon...

#### sectional_exiting

Sectional exiting features configuration sections that have a configuration syntax that defines the end of a configuration section. Examples of this are RPL (route policy language) configurations in IOS XR or peer policy and peer session configurations in IOS BGP sections. The sectional exiting configuration allows you to define the configuration syntax so that hier_config can render a remediation that properly exits those configurations.

An example of sectional exiting is:

```yaml
sectional_exiting:
- lineage:
  - startswith: router bgp
  - startswith: template peer-policy
  exit_text: exit-peer-policy
- lineage:
  - startswith: router bgp
  - startswith: template peer-session
  exit_text: exit-peer-session
```

#### full_text_sub

Full text sub allows for substitutions of a multi-line string. Regular expressions are commonly used and allowed in this section. An example of this would be:

```yaml
full_text_sub:
- search: "banner\s(exec|motd)\s(\S)\n(.*\n){1,}(\2)"
  replace: ""
```

This example simply searches for a banner message in the configuration and replaces it with an empty string.

#### per_line_sub

Per line sub allows for substitutions of individual lines. This is commonly used to remove artifacts from a running configuration that don't provide any value when creating remediation steps.

An example is removing lines such as:

```text
Building configuration...

Current configuration : 3781 bytes
```

Per line sub can be used to remove those lines:

```yaml
per_line_sub:
- search: "Building configuration.*"
  replace: ""
- search: "Current configuration.*"
  replace: ""
```

#### idempotent_commands_blacklist

coming soon...

#### idempotent_commands

Idempotent commands are commands that can just be overwritten and don't need negation. Lineage rules can be created to define those commands that are idempotent.

An example of idempotent commands are:

```yaml
idempotent_commands:
- lineage:
  - startswith: vlan
  - startswith: name
- lineage:
  - startswith: interface
  - startswith: description
```

The lineage rules above specify that defining a vlan name and updating an interface description are both idempotent commands.

#### negation_default_when

coming soon...

#### negation_default_with

coming soon...

## Custom hier_config Workflows

Coming soon...
