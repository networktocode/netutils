# ACL

The ACL classes are intended to help guide the ACL conversation. It is not intended to solve every ACL challenge you may have. In essence, it provides sane defaults and welcomes you to extend the logic via supported extension mechanisms. There are three patterns that heavily make up the capabilities:

- Expanding data to the ["Cartesian product"](#cartesian-product) (or permutations) of each rule, so that each product can be easily evaluated.
- Providing a `f"{type}_*` method pattern, to dynamically find any `validate_*` or `enforce_*` method you provide.
- Providing a `f"{type}_{attr}` method pattern, to dynamically find any `process_{attr}` or `match_{attr}` method you provide for the given attrs.

Each of these are covered in detail, below in the [core concepts](#core-concepts) section.

Here you can see how the Python classes work together. There is a lot going on, so I encourage you to review the diagram briefly, and refer back to it often while reviewing the detailed information below.

![ACL Classes](../images/acl-workflow.png)

!!! info
    It may be helpful to open the diagram in a new tab to view the full size, as an example, in Chrome you can right-click on the image and select "Open Image on New Tab".

The intention of this page is not to cover every attribute and it's behavior, but a more human (although highly technical) understanding of what is going on. For more detailed information, please see the [test](https://github.com/networktocode/netutils/blob/develop/tests/unit/test_acl.py) and [code docs](../dev/code_reference/acl.md).

!!! info
    In the future the intention is to add features such as better de-duplication, partial match, and path analysis.

## Core Concepts

### Cartesian Product

This ["Cartesian product"](https://en.wikipedia.org/wiki/Cartesian_product) concept is used throughout the page, so I thought it would be good to review. In this example, we have a single `rule`, and like many rules, it has multiple sources, destinations, and protocols. The `_cartesian_product` function creates the permutations, each of which is technically called a product.


```python
>>> from netutils.acl import _cartesian_product
>>> rule = dict(
...         name="Allow to internal web",
...         src_ip=["192.168.0.0/24", "10.0.0.0/16"],
...         dst_ip=["172.16.0.0/16", "192.168.250.10-192.168.250.20"],
...         dst_port=["tcp/80", "udp/53"],
...         action="permit",
...     )
>>> for item in _cartesian_product(rule):
...   print(item)
... 
{'name': 'Allow to internal web', 'src_ip': '192.168.0.0/24', 'dst_ip': '172.16.0.0/16', 'dst_port': 'tcp/80', 'action': 'permit'}
{'name': 'Allow to internal web', 'src_ip': '192.168.0.0/24', 'dst_ip': '172.16.0.0/16', 'dst_port': 'udp/53', 'action': 'permit'}
{'name': 'Allow to internal web', 'src_ip': '192.168.0.0/24', 'dst_ip': '192.168.250.10-192.168.250.20', 'dst_port': 'tcp/80', 'action': 'permit'}
{'name': 'Allow to internal web', 'src_ip': '192.168.0.0/24', 'dst_ip': '192.168.250.10-192.168.250.20', 'dst_port': 'udp/53', 'action': 'permit'}
{'name': 'Allow to internal web', 'src_ip': '10.0.0.0/16', 'dst_ip': '172.16.0.0/16', 'dst_port': 'tcp/80', 'action': 'permit'}
{'name': 'Allow to internal web', 'src_ip': '10.0.0.0/16', 'dst_ip': '172.16.0.0/16', 'dst_port': 'udp/53', 'action': 'permit'}
{'name': 'Allow to internal web', 'src_ip': '10.0.0.0/16', 'dst_ip': '192.168.250.10-192.168.250.20', 'dst_port': 'tcp/80', 'action': 'permit'}
{'name': 'Allow to internal web', 'src_ip': '10.0.0.0/16', 'dst_ip': '192.168.250.10-192.168.250.20', 'dst_port': 'udp/53', 'action': 'permit'}
>>> 
```

Now that you have the Cartesian products, you can evaluate each one individually. In this example perhaps '192.168.0.0/24' -> '172.16.0.0/16' is allowed, but '192.168.0.0/24' -> '192.168.250.10-192.168.250.20' is denied. Yet another example is the access could be allowed on both sources and destinations IPs, but not for udp/53 (DNS).

Having the ability to look at each product individually allows you to only have to worry about the check you wish to create, versus custom logic that attempts to understand the permutations. Building a `is_pci_to_non_pci` becomes trivial when looking at each product. This idea applies to validating, enforcing, matching, etc.


### Dynamic Method - Attrs 

The methods `process` and `match` both follow this pattern. As an example, the `process` method will dynamically find any method that follows `f"process_{attr}` pattern. This allows a Python class that inherits from `ACLRule` to simply add a `process_src_ip` method and that method would be called.

### Dynamic Method - Any

The methods `validate` and `enforce` both follow this pattern. As an example, the `validate` method will dynamically find any method that follows `f"process_*` pattern. This allows a Python class that inherits from `ACLRule` to simply add a `validate_ip_in_network` method and that method would be called.

In both methods, ordering can be controlled with order_validate and order_enforce respectively. The default ordering will be alphabetical, as returned by the Python dir function.

## ACLRule

The `ACLRule` class at a high level:

- The class `ACLRule` is used for working with Access Control List (ACL) rules.
- It is built with extensibility in mind to allow you to customize how your business operates.
- It contains a list of attributes such as "name," "src_ip," "src_zone," "dst_ip," "dst_port," "dst_zone," and "action" that are commonly used to work with ACLs.
- Provides the ability for you to expand data such as converting an address-group name into detailed addresses with your custom code.
- Provides the Cartesian product (or permutations) of the rules to make evaluation simple.
- It provides options for verifying input data and result data (data expanded) with corresponding JSON schemas.
- Provides the ability to validate data, generally for tech feasibility testing such as "are IPs on our network and in IPAM" or "is NAT IP provided vs actual IP".
- Provides the ability to enforce data, generally for security testing such as "is PCI attempting to talk with a non-PCI environment" or "is IP range not narrowly scoped enough".
    - The class supports a matrix feature, which allows users to define custom rule matching based on predefined matrix definitions.
- Provides the ability to match one rule to another, to understand if rule exists already.

### Initialization & Loading Data

The initialization process calls on the `load_data` method. This on a high level verifies schema of initial data, allows you to process data (e.g. convert tcp/https -> 80/443), expand data, determine Cartesian product (or permutations) of the firewall rule (traditionally 5-tuple), and verifies schema of result data.

The Cartesian product (or permutations) is key to the functionality of other steps, this allows you to evaluate each rule based on the smallest view of the data, so pay close attention to those steps, as it is important to other methods as well.

To provide some ideas on what you may validate:

- Is one of the source or destination IPs in our network?
- Is one of the source or destination IPs in our IPAM?
- Is the source and destination IPs able to route to each other?
- Is the source and destination IPs on the same network?
- Is one of the destination IPs to the real IP vs the NAT IP?
- Is there routing from the source zone to the destination zone?
- Is the business unit name in the description ?

Many of validations will be based on IPs, but not all.

Here you will find a written understanding of what is happening in the code:

- The init method takes in data and calls `load_data`.
- The method `load_data` processes the input data.
    - The `input_data_check` method is called and verifies the input data based on the specified JSON schema.
        - This is controlled by the `input_data_verify` attribute and schema defined in `input_data_schema`.
    - For each `self.attrs`, a method name matching `f"process_{attr}"`, (e.g. `process_src_ip()`) is called.
        - This allows you to inherit from and provide your own custom processes to convert, expand, or otherwise modify data before being evaluated.
        - The `process_dst_port` method processes the `dst_port` attribute by converting the protocol and port information, it is enabled by default but controlled with the `dst_port_process` attribute.
        - Both a dictionary `self.processed` and attributes (e.g. self.action, self.src_ip, etc.) are created.
    - The `result_data_check` method verifies the processed data based on the specified JSON schema.
        - This is controlled by the `result_data_verify` attribute which is disabled by default.
    - The `validate` method validating the rule using a series of custom methods starting with `validate_` prefixes.
        - The ordering can be controlled based on the `order_validate` attribute or defaults to all matches.
    - The rules are expanded into `self.expanded_rules` by creating each permutations of the tuple, using a Cartesian product function.
        - An example permutations would be converting source: 10.1.1.1, 10.1.1.2, destination: 10.100.100.100, port: 80 -> 10.1.1.1, destination: 10.100.100.100, port: 80 and 10.1.1.2, destination: 10.100.100.100, port: 80.
        - This will be key, so that each permutations can be compared individually later.
    - Filter out the permutations that have the same source and destination IP, if `self.filter_same_ip` which is on by default.

### Enforce

Enforce is generally used for security controls. An `enforce_matrix` is provided but not used by default. You can think of the matrix as an Excel sheet, in which you have source as the rows and destination as the column. You would identify the source/destination IP and find which x & y coordinates in your Excel document, and perform whatever action it states, such as deny, review, approve, etc.

To provide some ideas on what you may enforce:

- Is the request for a PCI to non-PCI network?
- Is the request for a security-zone-X to security-zone-Y network?
- Is the protocol a secure protocol?
- Is the request approved?
- Is the IPs requested narrowly scoped?

Here you will find a written understanding of what is happening in the code:

- The `enforce` method validating the rule using a series of custom methods starting with `enforce_` prefixes such as `enforce_pci_checks`.
    - The ordering can be controlled based on the `order_enforce` attribute or defaults to all matches.
    - The `enforce_matrix` method enforces ACL rules based on a predefined matrix feature.
        - This is controlled by the `self.matrix_enforced` attribute and is off by default.
        - The `enforce_matrix` method runs the enforcement checks for each of the `self.expanded_rules` (or permutations of tuples)
        - This matrix definition is very simple and not likely ready to be be used in a production environment, instead used for simple demonstrations and communicating potential ideas.
    - Each method should return a dictionary or list of dictionaries as both of these are handled
        - In the example there is the `obj` and `action` key.
        - This could and should be extended, such as providing obj, action, detail_msg, notification_team, and any other metadata that the tooling using this system would require.
        - Catastrophic errors will raise an error.

While not accurate in all use cases it would be best practice to run any of your custom `enforce_` against `self.expanded_rules`. 

### Match & Match Details

The `match_details` method provides a verbose way of verifying match details between two ACL rule's, the `match` method uses `match_details` and provides a boolean if there are any rules in `rules_unmatched` which would tell you if you had a full match or not. We will only review in detail the `match_details`.

Here you will find a written understanding of what is happening in the code:

- The `self.expanded_rules` is looped over for every permutations.
    - For each `self.attrs`, a method name matching `f"match_{attr}"`, (e.g. `match_src_ip()`) is called.
        - This allows you to inherit from and provide your own custom equality check or verify with your business logic.
        - You do not need to have a `f"match_{attr}"` method for every attr, description as example would not be a good candidate to match on.
        - Equality checks are done on `src_zone`, `dst_zone`, `action`, and `port` by default.
        - An `is_ip_within` check is done with for `src_ip` and `dst_ip` by default.
- In the process, details are provided for and returned:
    - `rules_matched` - Root key that is a list of dictionaries of rules that matched.
    - `rules_unmatched` - Root key that is a list of dictionaries of rules that did not match.
    - `existing_rule_product` - The original expanded_rule that existed in this item.
    - `existing_rule` - The full original rule (not expanded_rule) that existed.
    - `match_rule` - The full original rule that tested against, only shown in `rules_matched` root key.

This data could help you to understand what matched, why it matched, and other metadata. This detail data can be used to in `ACLRules` to aggregate and ask more interesting questions.

## ACLRules

The `ACLRules` class at a high level:

- Loads up multiple `ACLRule` and loads the data from a list of dictionaries.
    - This is generally the data that exists on the firewall already, but there are other use cases.
- Allows you to match the multiple `ACLRule` objects, and test against a single `ACLRule` object.
    - This is generally to see if the access to the rule you are testing exists already or not.

Using the `match_details` method, you could as an example, build logic if every product of the rule is matched, just not against a single rule. This is one of many different ways you could use the data. 

## Example Usage

Here we can test if a rule is matched via the existing ruleset. We can leverage the permit or deny to understand if this exists already or not.

**Simple Example**

```python
>>> from netutils.acl import ACLRules
>>> 
>>> existing_acls = [
...     dict(
...         name="Allow to internal web",
...         src_ip=["192.168.0.0/24", "10.0.0.0/16"],
...         dst_ip=["172.16.0.0/16", "192.168.250.10-192.168.250.20"],
...         dst_port=["tcp/80", "udp/53"],
...         action="permit",
...     ),
...     dict(
...         name="Allow to internal dns",
...         src_ip=["192.168.1.0/24"],
...         dst_ip=["172.16.0.0/16"],
...         dst_port=["tcp/80", "udp/53"],
...         action="permit",
...     )
... ]
>>> 
>>> new_acl_match = dict(
...     name="Check multiple sources pass",
...     src_ip=["192.168.1.10", "192.168.1.11", "192.168.1.15-192.168.1.20"],
...     dst_ip="172.16.0.10",
...     dst_port="tcp/www-http",
...     action="permit",
... )
>>> 
>>> ACLRules(existing_acls).match(new_acl_match)
'permit'
>>> 
>>> 
>>> new_acl_non_match = dict(
...     name="Check no match",
...     src_ip=["10.1.1.1"],
...     dst_ip="172.16.0.10",
...     dst_port="tcp/www-http",
...     action="permit",
... )
>>> 
>>> ACLRules(existing_acls).match(new_acl_non_match)
'deny'
>>> 
```

**Inherit Example**

```python

from netutils.acl import ACLRule

class ExpandAddrGroups(ACLRule):
    address_groups = {"red": ["white", "blue"], "blue": ["cyan"], "yellow": ["orange"]}
    addresses = {"white": ["10.1.1.1", "10.2.2.2"], "cyan": ["10.3.3.3"], "orange": ["10.4.4.4"]}

    def __init__(self, data, *args, **kwargs):
        self.flattened_addresses = self.flatten_addresses(self.address_groups, self.addresses)
        super().__init__(data, *args, **kwargs)

    def flatten_addresses(self, address_groups, addresses):
        flattened_addresses = {}
        for group, subgroups in address_groups.items():
            if group in addresses:
                flattened_addresses.setdefault(group, []).extend(addresses[group])
            for subgroup in subgroups:
                if subgroup in addresses:
                    flattened_addresses.setdefault(group, []).extend(addresses[subgroup])
                if subgroup in address_groups:
                    subgroup_addresses = self.flatten_addresses({subgroup: address_groups[subgroup]}, addresses)
                    for sub_group, ips in subgroup_addresses.items():
                        flattened_addresses.setdefault(sub_group, []).extend(ips)
                        if group != sub_group:
                            flattened_addresses.setdefault(group, []).extend(ips)
        return flattened_addresses

    def process_ip(self, ip):
        if not isinstance(ip, list):
            ip = [ip]
        output = []
        for ip_name in ip:
            if not ip_name[0].isalpha():
                output.append(ip_name)
            elif self.addresses.get(ip_name):
                output.extend(self.addresses[ip_name])
            elif self.flattened_addresses.get(ip_name):
                output.extend(self.flattened_addresses[ip_name])
        return sorted(list(set(output)))

    def process_src_ip(self, src_ip):
        return self.process_ip(src_ip)

    def process_dst_ip(self, dst_ip):
        return self.process_ip(dst_ip)
```

Using the above object, we can test with:

```python
>>> rule_data = dict(
...     name="Check allow",
...     src_ip=["red", "blue", "10.4.4.4"],
...     dst_ip=["white"],
...     dst_port="6/www-http",
...     action="permit",
... )
>>> 
>>> address_object_expanded = ExpandAddrGroups(rule_data)
>>> for item in address_object_expanded.expanded_rules:
...   print(item)
... 
{'name': 'Check allow', 'src_ip': '10.1.1.1', 'dst_ip': '10.2.2.2', 'dst_port': '6/80', 'action': 'permit'}
{'name': 'Check allow', 'src_ip': '10.2.2.2', 'dst_ip': '10.1.1.1', 'dst_port': '6/80', 'action': 'permit'}
{'name': 'Check allow', 'src_ip': '10.3.3.3', 'dst_ip': '10.1.1.1', 'dst_port': '6/80', 'action': 'permit'}
{'name': 'Check allow', 'src_ip': '10.3.3.3', 'dst_ip': '10.2.2.2', 'dst_port': '6/80', 'action': 'permit'}
{'name': 'Check allow', 'src_ip': '10.4.4.4', 'dst_ip': '10.1.1.1', 'dst_port': '6/80', 'action': 'permit'}
{'name': 'Check allow', 'src_ip': '10.4.4.4', 'dst_ip': '10.2.2.2', 'dst_port': '6/80', 'action': 'permit'}
>>> 
```

In that example you can see how we expanded `red` -> 10.1.1.1", "10.2.2.2", "10.3.3.3" as an example.
