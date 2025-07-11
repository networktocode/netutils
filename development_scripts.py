"""Developer script to generate markdown tables."""

from jinja2 import BaseLoader, Environment, select_autoescape

from netutils import lib_mapper
from netutils.config.compliance import parser_map
from netutils.utils import _JINJA2_FUNCTION_MAPPINGS

LIB_MAPPER_TEMPLATE = """| {{ header_src }} | | {{ header_dst }} |
| ---------- | -- | ------ |
{%- for key, val in _dict|dictsort %}
| {{ key }} | → | {{ val|safe }} |
{%- endfor %}
"""

PARSER_MAPPER_TEMPLATE = """| OS Name | Parser Class |
| ---------- | ------ |
{%- for key, val in _dict|dictsort %}
| {{ key }} | netutils.config.parser.{{ val.__name__ }} |
{%- endfor %}
"""

JINJA_MAPPER_TEMPLATE = """| Filter name | Function |
| ---------- | ------ |
{%- for key, val in _dict|dictsort(false, 'value') %}
| {{ key }} | netutils.{{ val }} |
{%- endfor %}
"""

TEMPLATE = {
    "LIB_MAPPER_TEMPLATE": LIB_MAPPER_TEMPLATE,
    "PARSER_MAPPER_TEMPLATE": PARSER_MAPPER_TEMPLATE,
    "JINJA_MAPPER_TEMPLATE": JINJA_MAPPER_TEMPLATE,
}


MAPPER = {
    "LIB_MAPPER_TEMPLATE": {
        "aerleon": {
            "header_src": "AERLEON",
            "header_dst": "NORMALIZED",
            "_dict": lib_mapper.AERLEON_LIB_MAPPER,
            "_file": "docs/user/lib_mapper/aerleon.md",
        },
        "aerleon_reverse": {
            "header_src": "NORMALIZED",
            "header_dst": "AERLEON",
            "_dict": lib_mapper.AERLEON_LIB_MAPPER_REVERSE,
            "_file": "docs/user/lib_mapper/aerleon_reverse.md",
        },
        "ansible": {
            "header_src": "ANSIBLE",
            "header_dst": "NORMALIZED",
            "_dict": lib_mapper.ANSIBLE_LIB_MAPPER,
            "_file": "docs/user/lib_mapper/ansible.md",
        },
        "ansible_reverse": {
            "header_src": "NORMALIZED",
            "header_dst": "ANSIBLE",
            "_dict": lib_mapper.ANSIBLE_LIB_MAPPER_REVERSE,
            "_file": "docs/user/lib_mapper/ansible_reverse.md",
        },
        "capirca": {
            "header_src": "CAPIRCA",
            "header_dst": "NORMALIZED",
            "_dict": lib_mapper.CAPIRCA_LIB_MAPPER,
            "_file": "docs/user/lib_mapper/capirca.md",
        },
        "capirca_reverse": {
            "header_src": "NORMALIZED",
            "header_dst": "CAPIRCA",
            "_dict": lib_mapper.CAPIRCA_LIB_MAPPER_REVERSE,
            "_file": "docs/user/lib_mapper/capirca_reverse.md",
        },
        "dna_center": {
            "header_src": "DNA_CENTER",
            "header_dst": "NORMALIZED",
            "_dict": lib_mapper.DNA_CENTER_LIB_MAPPER,
            "_file": "docs/user/lib_mapper/dna_center.md",
        },
        "dna_center_reverse": {
            "header_src": "NORMALIZED",
            "header_dst": "DNA_CENTER",
            "_dict": lib_mapper.DNA_CENTER_LIB_MAPPER_REVERSE,
            "_file": "docs/user/lib_mapper/dna_center_reverse.md",
        },
        "forwardnetworks": {
            "header_src": "FORWARDNETWORKS",
            "header_dst": "NORMALIZED",
            "_dict": lib_mapper.FORWARDNETWORKS_LIB_MAPPER,
            "_file": "docs/user/lib_mapper/forwardnetworks.md",
        },
        "forwardnetworks_reverse": {
            "header_src": "NORMALIZED",
            "header_dst": "FORWARDNETWORKS",
            "_dict": lib_mapper.FORWARDNETWORKS_LIB_MAPPER_REVERSE,
            "_file": "docs/user/lib_mapper/forwardnetworks_reverse.md",
        },
        "hierconfig": {
            "header_src": "HIERCONFIG",
            "header_dst": "NORMALIZED",
            "_dict": lib_mapper.HIERCONFIG_LIB_MAPPER,
            "_file": "docs/user/lib_mapper/hierconfig.md",
        },
        "hierconfig_reverse": {
            "header_src": "NORMALIZED",
            "header_dst": "HIERCONFIG",
            "_dict": lib_mapper.HIERCONFIG_LIB_MAPPER_REVERSE,
            "_file": "docs/user/lib_mapper/hierconfig_reverse.md",
        },
        "napalm": {
            "header_src": "NAPALM",
            "header_dst": "NORMALIZED",
            "_dict": lib_mapper.NAPALM_LIB_MAPPER,
            "_file": "docs/user/lib_mapper/napalm.md",
        },
        "napalm_reverse": {
            "header_src": "NORMALIZED",
            "header_dst": "NAPALM",
            "_dict": lib_mapper.NAPALM_LIB_MAPPER_REVERSE,
            "_file": "docs/user/lib_mapper/napalm_reverse.md",
        },
        "netmiko": {
            "header_src": "NETMIKO",
            "header_dst": "NORMALIZED",
            "_dict": lib_mapper.NETMIKO_LIB_MAPPER,
            "_file": "docs/user/lib_mapper/netmiko.md",
        },
        "netmiko_reverse": {
            "header_src": "NORMALIZED",
            "header_dst": "NETMIKO",
            "_dict": lib_mapper.NETMIKO_LIB_MAPPER_REVERSE,
            "_file": "docs/user/lib_mapper/netmiko_reverse.md",
        },
        "netutilsparser": {
            "header_src": "NETUTILSPARSER",
            "header_dst": "NORMALIZED",
            "_dict": lib_mapper.NETUTILSPARSER_LIB_MAPPER,
            "_file": "docs/user/lib_mapper/netutilsparser.md",
        },
        "netutilsparser_reverse": {
            "header_src": "NORMALIZED",
            "header_dst": "NETUTILSPARSER",
            "_dict": lib_mapper.NETUTILSPARSER_LIB_MAPPER_REVERSE,
            "_file": "docs/user/lib_mapper/netutilsparser_reverse.md",
        },
        "nist": {
            "header_src": "NIST",
            "header_dst": "NORMALIZED",
            "_dict": lib_mapper.NIST_LIB_MAPPER,
            "_file": "docs/user/lib_mapper/nist.md",
        },
        "nist_reverse": {
            "header_src": "NORMALIZED",
            "header_dst": "NIST",
            "_dict": lib_mapper.NIST_LIB_MAPPER_REVERSE,
            "_file": "docs/user/lib_mapper/nist_reverse.md",
        },
        "ntctemplates": {
            "header_src": "NTCTEMPLATES",
            "header_dst": "NORMALIZED",
            "_dict": lib_mapper.NTCTEMPLATES_LIB_MAPPER,
            "_file": "docs/user/lib_mapper/ntctemplates.md",
        },
        "ntctemplates_reverse": {
            "header_src": "NORMALIZED",
            "header_dst": "NTCTEMPLATES",
            "_dict": lib_mapper.NTCTEMPLATES_LIB_MAPPER_REVERSE,
            "_file": "docs/user/lib_mapper/ntctemplates_reverse.md",
        },
        "pyats": {
            "header_src": "PYATS",
            "header_dst": "NORMALIZED",
            "_dict": lib_mapper.PYATS_LIB_MAPPER,
            "_file": "docs/user/lib_mapper/pyats.md",
        },
        "pyats_reverse": {
            "header_src": "NORMALIZED",
            "header_dst": "PYATS",
            "_dict": lib_mapper.PYATS_LIB_MAPPER_REVERSE,
            "_file": "docs/user/lib_mapper/pyats_reverse.md",
        },
        "pyntc": {
            "header_src": "PYNTC",
            "header_dst": "NORMALIZED",
            "_dict": lib_mapper.PYNTC_LIB_MAPPER,
            "_file": "docs/user/lib_mapper/pyntc.md",
        },
        "pyntc_reverse": {
            "header_src": "NORMALIZED",
            "header_dst": "PYNTC",
            "_dict": lib_mapper.PYNTC_LIB_MAPPER_REVERSE,
            "_file": "docs/user/lib_mapper/pyntc_reverse.md",
        },
        "running_config_mapper": {
            "header_src": "NORMALIZED",
            "header_dst": "RUNNING_CONFIG_COMMAND",
            "_dict": lib_mapper.RUNNING_CONFIG_MAPPER,
            "_file": "docs/user/lib_mapper/running_config.md",
        },
        "scrapli": {
            "header_src": "SCRAPLI",
            "header_dst": "NORMALIZED",
            "_dict": lib_mapper.SCRAPLI_LIB_MAPPER,
            "_file": "docs/user/lib_mapper/scrapli.md",
        },
        "scrapli_reverse": {
            "header_src": "NORMALIZED",
            "header_dst": "SCRAPLI",
            "_dict": lib_mapper.SCRAPLI_LIB_MAPPER_REVERSE,
            "_file": "docs/user/lib_mapper/scrapli_reverse.md",
        },
    },
    "PARSER_MAPPER_TEMPLATE": {
        "default": {
            "_dict": parser_map,
            "_file": "docs/dev/include_parser_list.md",
        },
    },
    "JINJA_MAPPER_TEMPLATE": {
        "default": {
            "_dict": _JINJA2_FUNCTION_MAPPINGS,
            "_file": "docs/user/include_jinja_list.md",
        },
    },
}


def main(test=False):
    """Generate or test generation of standard files."""
    env = Environment(loader=BaseLoader, autoescape=select_autoescape())

    for template_name, value in MAPPER.items():
        for data in value.values():
            _file = data["_file"]
            output = env.from_string(TEMPLATE[template_name]).render(**data)
            if test:
                with open(_file, encoding="utf8") as file:
                    actual = file.read()
                if output != actual:
                    return False
            else:
                with open(_file, "w", encoding="utf8") as file:
                    file.write(output)
    return True


if __name__ == "__main__":
    main()
