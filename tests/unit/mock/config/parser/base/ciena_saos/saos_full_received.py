from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="virtual-switch create vs MGMT-VS", parents=()),
    ConfigLine(config_line="virtual-switch create vs OPS-VS", parents=()),
    ConfigLine(config_line="module set module 1 module-type CFP2-QSFP28", parents=()),
    ConfigLine(config_line="module set module 2 module-type CFP2-QSFP28", parents=()),
    ConfigLine(config_line="interface set interface active ip 192.168.0.101/24", parents=()),
    ConfigLine(config_line="interface create remote-interface MGMT ip 203.0.113.6/29 vs MGMT-VS", parents=()),
    ConfigLine(config_line="interface set gateway 203.0.113.1", parents=()),
    ConfigLine(config_line="traffic-services set bw-calculation-mode payload", parents=()),
    ConfigLine(
        config_line="traffic-services metering meter-profile create profile MGMT-policer cir 256 cbs 21 eir 768 ebs 21",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services metering meter-profile create profile MGMT-MTU-policer cir 2560 cbs 21 eir 7680 ebs 21",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services metering meter-profile create profile OPS-policer cir 256 cbs 21 eir 768 ebs 21",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services metering meter-profile create profile OPS-MTU-policer cir 2560 cbs 21 eir 7680 ebs 21",
        parents=(),
    ),
    ConfigLine(config_line="l2-cft create profile network l2-control-fixed-rcos 0", parents=()),
    ConfigLine(config_line="l2-cft create profile EP-UNI l2-control-fixed-rcos 0", parents=()),
    ConfigLine(config_line="l2-cft set port 1 profile network", parents=()),
    ConfigLine(config_line="l2-cft enable port 1", parents=()),
    ConfigLine(config_line="port set port 1 max-frame-size 9172 description PORT-DESC", parents=()),
    ConfigLine(config_line="l2-cft set port 2 profile network", parents=()),
    ConfigLine(config_line="l2-cft enable port 2", parents=()),
    ConfigLine(config_line="port set port 2 max-frame-size 9172 description PORT-DESC", parents=()),
    ConfigLine(config_line="l2-cft set port 1/2 profile network", parents=()),
    ConfigLine(config_line="l2-cft enable port 1/2", parents=()),
    ConfigLine(config_line="port set port 1/2 max-frame-size 9172 description PORT-DESC", parents=()),
    ConfigLine(config_line="l2-cft set port 2/2 profile network", parents=()),
    ConfigLine(config_line="l2-cft enable port 2/2", parents=()),
    ConfigLine(config_line="port set port 2/2 max-frame-size 9172 description PORT-DESC", parents=()),
    ConfigLine(config_line="port set port 1 speed ten-gig", parents=()),
    ConfigLine(config_line="port set port 2 speed gigabit", parents=()),
    ConfigLine(config_line="port set port 1/2 speed hundred-gig", parents=()),
    ConfigLine(config_line="port set port 2/2 speed forty-gig", parents=()),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 1-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 2-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 3-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 4-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 5-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 6-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 7-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 8-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 9-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 10-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 11-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 12-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 13-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 14-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 15-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 16-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 17-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 18-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 19-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 20-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 21-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 22-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 23-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 24-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 25-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 26-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 27-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 28-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 29-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 30-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 31-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 32-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 33-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 34-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 35-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 36-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 37-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 38-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 39-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 40-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 1/1-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 1/2-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 2/1-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(
        config_line="traffic-services queuing egress-port-queue-group set queue-group 2/2-Default shaper-compensation 20",
        parents=(),
    ),
    ConfigLine(config_line="cpu-interface sub-interface create cpu-subinterface MGMT-CPU", parents=()),
    ConfigLine(
        config_line="sub-port create sub-port 1/2.99 parent-port 1/2 classifier-precedence 99 ingress-meter-profile MGMT-policer",
        parents=(),
    ),
    ConfigLine(
        config_line="sub-port create sub-port 1/2.88 parent-port 1/2 classifier-precedence 88 ingress-meter-profile OPS-MTU-policer",
        parents=(),
    ),
    ConfigLine(config_line="sub-port create sub-port 1.99 parent-port 1 classifier-precedence 99", parents=()),
    ConfigLine(config_line="sub-port create sub-port 2.99 parent-port 2 classifier-precedence 99", parents=()),
    ConfigLine(config_line="sub-port add sub-port 1/2.99 class-element 1 vlan-untagged-data", parents=()),
    ConfigLine(config_line="sub-port add sub-port 1/2.88 class-element 88 vtag-stack 88", parents=()),
    ConfigLine(config_line="sub-port add sub-port 1.99 class-element 1 vlan-untagged-data", parents=()),
    ConfigLine(config_line="sub-port add sub-port 2.99 class-element 1 vlan-untagged-data", parents=()),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol cisco-cdp untagged-disposition discard",
        parents=(),
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol cisco-dtp untagged-disposition discard",
        parents=(),
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol cisco-pagp untagged-disposition discard",
        parents=(),
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol cisco-udld untagged-disposition discard",
        parents=(),
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol cisco-vtp untagged-disposition forward",
        parents=(),
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol cisco-pvst untagged-disposition discard",
        parents=(),
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol cisco-stp-uplink-fast untagged-disposition discard",
        parents=(),
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol vlan-bridge untagged-disposition discard",
        parents=(),
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol rstp untagged-disposition discard", parents=()
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol 802.1x untagged-disposition discard", parents=()
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol gmrp untagged-disposition discard", parents=()
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol gvrp untagged-disposition discard", parents=()
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol isis untagged-disposition discard", parents=()
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol bridge-rsvd-0C0D untagged-disposition discard",
        parents=(),
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol bridge-rsvd-0B0F untagged-disposition discard",
        parents=(),
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol bridge-block untagged-disposition discard",
        parents=(),
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol all-bridges-block untagged-disposition discard",
        parents=(),
    ),
    ConfigLine(
        config_line="l2-cft protocol add profile network ctrl-protocol garp-block untagged-disposition discard",
        parents=(),
    ),
    ConfigLine(config_line="virtual-switch interface attach sub-port 1/2.99 vs MGMT-VS", parents=()),
    ConfigLine(config_line="virtual-switch interface attach sub-port 1.99 vs MGMT-VS", parents=()),
    ConfigLine(config_line="virtual-switch interface attach sub-port 2.99 vs MGMT-VS", parents=()),
    ConfigLine(config_line="virtual-switch interface attach cpu-subinterface MGMT-CPU vs MGMT-VS", parents=()),
    ConfigLine(config_line="virtual-switch interface attach sub-port 1/2.88 vs OPS-VS", parents=()),
    ConfigLine(config_line="tacacs set secret 53cr37!", parents=()),
    ConfigLine(config_line="user user1 access-level super secret 53cr37!", parents=()),
    ConfigLine(config_line="user user2 access-level super secret 53cr37!", parents=()),
    ConfigLine(config_line="user user3 access-level super secret 53cr37!", parents=()),
    ConfigLine(config_line="system shell set global-more off", parents=()),
    ConfigLine(
        config_line='system shell banner create banner login line "*******************************************************************************"',
        parents=(),
    ),
    ConfigLine(
        config_line='system shell banner add banner login line "***                         THIS IS A LOGIN BANNER                          ***"',
        parents=(),
    ),
    ConfigLine(
        config_line='system shell banner add banner login line "*******************************************************************************"',
        parents=(),
    ),
    ConfigLine(config_line="port xcvr set xcvr 1 frequency 195500", parents=()),
    ConfigLine(config_line="port xcvr set xcvr 40 frequency 196100", parents=()),
    ConfigLine(
        config_line="snmp create user v2cGet auth-protocol noAuth engine-id 80:00:04:f7:05:2c:4a:11:c9:ca:80:00",
        parents=(),
    ),
    ConfigLine(
        config_line="snmp create user v2cTrap auth-protocol noAuth engine-id 80:00:04:f7:05:2c:4a:11:c9:ca:80:00",
        parents=(),
    ),
    ConfigLine(config_line="snmp security-to-group attach user v2cGet sec-model v2c group getGroup", parents=()),
    ConfigLine(config_line="snmp security-to-group attach user v2cTrap sec-model v2c group trapGroup", parents=()),
    ConfigLine(config_line="snmp create viewtree getView sub-tree iso type include", parents=()),
    ConfigLine(config_line="snmp create viewtree getView sub-tree snmpResearch type exclude", parents=()),
    ConfigLine(config_line="snmp create viewtree trapView sub-tree iso type exclude", parents=()),
    ConfigLine(
        config_line="snmp create access-entry getGroup sec-model v2c sec-level noAuth read-view getView", parents=()
    ),
    ConfigLine(
        config_line="snmp create access-entry trapGroup sec-model v2c sec-level noAuth read-view trapView notify-view V12cView",
        parents=(),
    ),
    ConfigLine(
        config_line="snmp create target anycast-target addr 192.0.2.5/32 param-name anycast-param transport-domain snmp-udp",
        parents=(),
    ),
    ConfigLine(config_line="snmp delete target anywhereIpv6", parents=()),
    ConfigLine(config_line="snmp delete target anywhere", parents=()),
    ConfigLine(
        config_line="snmp create target-param anycast-param sec-name v2cTrap sec-model v2c sec-level noAuth", parents=()
    ),
    ConfigLine(config_line="snmp delete community-index t0000000", parents=()),
    ConfigLine(config_line="snmp delete community-index t0000001", parents=()),
    ConfigLine(config_line="snmp create community-index getString community 57r1n6! sec-name v2cGet", parents=()),
    ConfigLine(config_line="snmp create community-index trapString community 57r1n6! sec-name v2cTrap", parents=()),
    ConfigLine(config_line="ssh server enable", parents=()),
]
