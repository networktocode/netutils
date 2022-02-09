from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="configure { }", parents=()),
    ConfigLine(config_line="configure { card 1 }", parents=()),
    ConfigLine(config_line="configure { card 1 card-type iom-1 }", parents=()),
    ConfigLine(config_line="configure { card 1 mda 1 }", parents=()),
    ConfigLine(config_line="configure { card 1 mda 1 mda-type me12-100gb-qsfp28 }", parents=()),
    ConfigLine(config_line="configure { card 1 mda 2 }", parents=()),
    ConfigLine(config_line="configure { card 1 fp 1 }", parents=()),
    ConfigLine(config_line="configure { log }", parents=()),
    ConfigLine(config_line='configure { log filter "1001" }', parents=()),
    ConfigLine(config_line='configure { log filter "1001" named-entry "10" }', parents=()),
    ConfigLine(
        config_line='configure { log filter "1001" named-entry "10" description "Collect only events of major severity or higher" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { log filter "1001" named-entry "10" action forward }', parents=()),
    ConfigLine(config_line='configure { log filter "1001" named-entry "10" match }', parents=()),
    ConfigLine(config_line='configure { log filter "1001" named-entry "10" match severity }', parents=()),
    ConfigLine(config_line='configure { log filter "1001" named-entry "10" match severity gte major }', parents=()),
    ConfigLine(config_line='configure { log log-id "100" }', parents=()),
    ConfigLine(config_line='configure { log log-id "100" description "Default Serious Errors Log" }', parents=()),
    ConfigLine(config_line='configure { log log-id "100" filter "1001" }', parents=()),
    ConfigLine(config_line='configure { log log-id "100" source }', parents=()),
    ConfigLine(config_line='configure { log log-id "100" source main true }', parents=()),
    ConfigLine(config_line='configure { log log-id "100" destination }', parents=()),
    ConfigLine(config_line='configure { log log-id "100" destination memory }', parents=()),
    ConfigLine(config_line='configure { log log-id "100" destination memory max-entries 500 }', parents=()),
    ConfigLine(config_line='configure { log log-id "99" }', parents=()),
    ConfigLine(config_line='configure { log log-id "99" description "Default System Log" }', parents=()),
    ConfigLine(config_line='configure { log log-id "99" source }', parents=()),
    ConfigLine(config_line='configure { log log-id "99" source main true }', parents=()),
    ConfigLine(config_line='configure { log log-id "99" destination }', parents=()),
    ConfigLine(config_line='configure { log log-id "99" destination memory }', parents=()),
    ConfigLine(config_line='configure { log log-id "99" destination memory max-entries 500 }', parents=()),
    ConfigLine(config_line="configure { port 1/1/c1 }", parents=()),
    ConfigLine(config_line="configure { port 1/1/c2 }", parents=()),
    ConfigLine(config_line="configure { port 1/1/c3 }", parents=()),
    ConfigLine(config_line="configure { port 1/1/c4 }", parents=()),
    ConfigLine(config_line="configure { port 1/1/c5 }", parents=()),
    ConfigLine(config_line="configure { port 1/1/c6 }", parents=()),
    ConfigLine(config_line="configure { port 1/1/c7 }", parents=()),
    ConfigLine(config_line="configure { port 1/1/c8 }", parents=()),
    ConfigLine(config_line="configure { port 1/1/c9 }", parents=()),
    ConfigLine(config_line="configure { port 1/1/c10 }", parents=()),
    ConfigLine(config_line="configure { port 1/1/c11 }", parents=()),
    ConfigLine(config_line="configure { port 1/1/c12 }", parents=()),
    ConfigLine(config_line='configure { router "Base" }', parents=()),
    ConfigLine(config_line='configure { router "Base" interface "L3-OAM-eNodeB069420-W1" }', parents=()),
    ConfigLine(
        config_line='configure { router "Base" interface "L3-OAM-eNodeB069420-W1" admin-state disable }', parents=()
    ),
    ConfigLine(
        config_line='configure { router "Base" interface "L3-OAM-eNodeB069420-W1" ingress-stats false }', parents=()
    ),
    ConfigLine(config_line="configure { system }", parents=()),
    ConfigLine(config_line='configure { system name "core-router" }', parents=()),
    ConfigLine(config_line="configure { system grpc }", parents=()),
    ConfigLine(config_line="configure { system grpc admin-state enable }", parents=()),
    ConfigLine(config_line="configure { system grpc allow-unsecure-connection }", parents=()),
    ConfigLine(config_line="configure { system grpc gnmi }", parents=()),
    ConfigLine(config_line="configure { system grpc gnmi auto-config-save true }", parents=()),
    ConfigLine(config_line="configure { system grpc rib-api }", parents=()),
    ConfigLine(config_line="configure { system grpc rib-api admin-state enable }", parents=()),
    ConfigLine(config_line="configure { system management-interface }", parents=()),
    ConfigLine(config_line="configure { system management-interface configuration-mode model-driven }", parents=()),
    ConfigLine(config_line="configure { system management-interface netconf }", parents=()),
    ConfigLine(config_line="configure { system management-interface netconf admin-state enable }", parents=()),
    ConfigLine(config_line="configure { system management-interface netconf auto-config-save true }", parents=()),
    ConfigLine(config_line="configure { system management-interface snmp }", parents=()),
    ConfigLine(config_line="configure { system management-interface snmp packet-size 9216 }", parents=()),
    ConfigLine(config_line="configure { system management-interface snmp streaming }", parents=()),
    ConfigLine(config_line="configure { system management-interface snmp streaming admin-state enable }", parents=()),
    ConfigLine(config_line="configure { system bluetooth }", parents=()),
    ConfigLine(config_line="configure { system bluetooth advertising-timeout 30 }", parents=()),
    ConfigLine(config_line="configure { system login-control }", parents=()),
    ConfigLine(config_line="configure { system login-control ssh }", parents=()),
    ConfigLine(config_line="configure { system login-control ssh inbound-max-sessions 30 }", parents=()),
    ConfigLine(config_line="configure { system security }", parents=()),
    ConfigLine(config_line="configure { system security aaa }", parents=()),
    ConfigLine(config_line="configure { system security aaa local-profiles }", parents=()),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "administrative" }', parents=()),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" default-action permit-all }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" netconf }', parents=()
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" netconf base-op-authorization }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" netconf base-op-authorization kill-session true }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" netconf base-op-authorization lock true }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 10 }', parents=()
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 10 action permit }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 10 match "configure system security" }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 20 }', parents=()
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 20 action permit }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 20 match "show system security" }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 30 }', parents=()
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 30 action permit }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 30 match "tools perform security" }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 40 }', parents=()
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 40 action permit }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 40 match "tools dump security" }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 50 }', parents=()
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 50 action permit }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 50 match "admin system security" }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 100 }', parents=()
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 100 action deny }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 100 match "configure li" }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 110 }', parents=()
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 110 action deny }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 110 match "show li" }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 111 }', parents=()
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 111 action deny }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 111 match "clear li" }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 112 }', parents=()
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 112 action deny }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "administrative" entry 112 match "tools dump li" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "default" }', parents=()),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "default" entry 10 }', parents=()),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 10 action permit }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 10 match "exec" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "default" entry 20 }', parents=()),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 20 action permit }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 20 match "exit" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "default" entry 30 }', parents=()),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 30 action permit }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 30 match "help" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "default" entry 40 }', parents=()),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 40 action permit }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 40 match "logout" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "default" entry 50 }', parents=()),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 50 action permit }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 50 match "password" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "default" entry 60 }', parents=()),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 60 action deny }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 60 match "show config" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "default" entry 65 }', parents=()),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 65 action deny }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 65 match "show li" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "default" entry 66 }', parents=()),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 66 action deny }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 66 match "clear li" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "default" entry 67 }', parents=()),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 67 action deny }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 67 match "tools dump li" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "default" entry 68 }', parents=()),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 68 action deny }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 68 match "state li" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "default" entry 70 }', parents=()),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 70 action permit }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 70 match "show" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "default" entry 75 }', parents=()),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 75 action permit }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 75 match "state" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "default" entry 80 }', parents=()),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 80 action permit }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 80 match "enable-admin" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "default" entry 90 }', parents=()),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 90 action permit }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 90 match "enable" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { system security aaa local-profiles profile "default" entry 100 }', parents=()),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 100 action deny }',
        parents=(),
    ),
    ConfigLine(
        config_line='configure { system security aaa local-profiles profile "default" entry 100 match "configure li" }',
        parents=(),
    ),
    ConfigLine(config_line="configure { system security ssh }", parents=()),
    ConfigLine(config_line="configure { system security ssh server-cipher-list-v1 }", parents=()),
    ConfigLine(config_line="configure { system security ssh server-cipher-list-v1 cipher 200 }", parents=()),
    ConfigLine(config_line="configure { system security ssh server-cipher-list-v1 cipher 200 name 3des }", parents=()),
    ConfigLine(config_line="configure { system security ssh server-cipher-list-v1 cipher 205 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-cipher-list-v1 cipher 205 name blowfish }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh server-cipher-list-v2 }", parents=()),
    ConfigLine(config_line="configure { system security ssh server-cipher-list-v2 cipher 190 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-cipher-list-v2 cipher 190 name aes256-ctr }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh server-cipher-list-v2 cipher 192 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-cipher-list-v2 cipher 192 name aes192-ctr }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh server-cipher-list-v2 cipher 194 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-cipher-list-v2 cipher 194 name aes128-ctr }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh server-cipher-list-v2 cipher 200 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-cipher-list-v2 cipher 200 name aes128-cbc }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh server-cipher-list-v2 cipher 205 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-cipher-list-v2 cipher 205 name 3des-cbc }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh server-cipher-list-v2 cipher 210 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-cipher-list-v2 cipher 210 name blowfish-cbc }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh server-cipher-list-v2 cipher 215 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-cipher-list-v2 cipher 215 name cast128-cbc }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh server-cipher-list-v2 cipher 220 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-cipher-list-v2 cipher 220 name arcfour }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh server-cipher-list-v2 cipher 225 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-cipher-list-v2 cipher 225 name aes192-cbc }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh server-cipher-list-v2 cipher 230 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-cipher-list-v2 cipher 230 name aes256-cbc }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh server-cipher-list-v2 cipher 235 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-cipher-list-v2 cipher 235 name rijndael-cbc }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v1 }", parents=()),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v1 cipher 200 }", parents=()),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v1 cipher 200 name 3des }", parents=()),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v1 cipher 205 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-cipher-list-v1 cipher 205 name blowfish }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v1 cipher 210 }", parents=()),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v1 cipher 210 name des }", parents=()),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v2 }", parents=()),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v2 cipher 190 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-cipher-list-v2 cipher 190 name aes256-ctr }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v2 cipher 192 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-cipher-list-v2 cipher 192 name aes192-ctr }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v2 cipher 194 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-cipher-list-v2 cipher 194 name aes128-ctr }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v2 cipher 200 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-cipher-list-v2 cipher 200 name aes128-cbc }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v2 cipher 205 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-cipher-list-v2 cipher 205 name 3des-cbc }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v2 cipher 210 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-cipher-list-v2 cipher 210 name blowfish-cbc }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v2 cipher 215 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-cipher-list-v2 cipher 215 name cast128-cbc }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v2 cipher 220 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-cipher-list-v2 cipher 220 name arcfour }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v2 cipher 225 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-cipher-list-v2 cipher 225 name aes192-cbc }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v2 cipher 230 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-cipher-list-v2 cipher 230 name aes256-cbc }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh client-cipher-list-v2 cipher 235 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-cipher-list-v2 cipher 235 name rijndael-cbc }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh server-mac-list-v2 }", parents=()),
    ConfigLine(config_line="configure { system security ssh server-mac-list-v2 mac 200 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-mac-list-v2 mac 200 name hmac-sha2-512 }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh server-mac-list-v2 mac 210 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-mac-list-v2 mac 210 name hmac-sha2-256 }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh server-mac-list-v2 mac 215 }", parents=()),
    ConfigLine(config_line="configure { system security ssh server-mac-list-v2 mac 215 name hmac-sha1 }", parents=()),
    ConfigLine(config_line="configure { system security ssh server-mac-list-v2 mac 220 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-mac-list-v2 mac 220 name hmac-sha1-96 }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh server-mac-list-v2 mac 225 }", parents=()),
    ConfigLine(config_line="configure { system security ssh server-mac-list-v2 mac 225 name hmac-md5 }", parents=()),
    ConfigLine(config_line="configure { system security ssh server-mac-list-v2 mac 230 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-mac-list-v2 mac 230 name hmac-ripemd160 }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh server-mac-list-v2 mac 235 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh server-mac-list-v2 mac 235 name hmac-ripemd160-openssh-com }",
        parents=(),
    ),
    ConfigLine(config_line="configure { system security ssh server-mac-list-v2 mac 240 }", parents=()),
    ConfigLine(config_line="configure { system security ssh server-mac-list-v2 mac 240 name hmac-md5-96 }", parents=()),
    ConfigLine(config_line="configure { system security ssh client-mac-list-v2 }", parents=()),
    ConfigLine(config_line="configure { system security ssh client-mac-list-v2 mac 200 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-mac-list-v2 mac 200 name hmac-sha2-512 }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh client-mac-list-v2 mac 210 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-mac-list-v2 mac 210 name hmac-sha2-256 }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh client-mac-list-v2 mac 215 }", parents=()),
    ConfigLine(config_line="configure { system security ssh client-mac-list-v2 mac 215 name hmac-sha1 }", parents=()),
    ConfigLine(config_line="configure { system security ssh client-mac-list-v2 mac 220 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-mac-list-v2 mac 220 name hmac-sha1-96 }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh client-mac-list-v2 mac 225 }", parents=()),
    ConfigLine(config_line="configure { system security ssh client-mac-list-v2 mac 225 name hmac-md5 }", parents=()),
    ConfigLine(config_line="configure { system security ssh client-mac-list-v2 mac 230 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-mac-list-v2 mac 230 name hmac-ripemd160 }", parents=()
    ),
    ConfigLine(config_line="configure { system security ssh client-mac-list-v2 mac 235 }", parents=()),
    ConfigLine(
        config_line="configure { system security ssh client-mac-list-v2 mac 235 name hmac-ripemd160-openssh-com }",
        parents=(),
    ),
    ConfigLine(config_line="configure { system security ssh client-mac-list-v2 mac 240 }", parents=()),
    ConfigLine(config_line="configure { system security ssh client-mac-list-v2 mac 240 name hmac-md5-96 }", parents=()),
    ConfigLine(config_line="configure { system security user-params }", parents=()),
    ConfigLine(config_line="configure { system security user-params local-user }", parents=()),
    ConfigLine(config_line='configure { system security user-params local-user user "admin" }', parents=()),
    ConfigLine(
        config_line='configure { system security user-params local-user user "admin" password "$2y$10$TQrZlpBDra86.qoexZUzQeBXDY1FcdDhGWdD9lLxMuFyPVSm0OGy6" }',
        parents=(),
    ),
    ConfigLine(config_line='configure { system security user-params local-user user "admin" access }', parents=()),
    ConfigLine(
        config_line='configure { system security user-params local-user user "admin" access console true }', parents=()
    ),
    ConfigLine(
        config_line='configure { system security user-params local-user user "admin" access ftp true }', parents=()
    ),
    ConfigLine(
        config_line='configure { system security user-params local-user user "admin" access snmp true }', parents=()
    ),
    ConfigLine(
        config_line='configure { system security user-params local-user user "admin" access netconf true }', parents=()
    ),
    ConfigLine(
        config_line='configure { system security user-params local-user user "admin" access grpc true }', parents=()
    ),
    ConfigLine(config_line='configure { system security user-params local-user user "admin" console }', parents=()),
    ConfigLine(
        config_line='configure { system security user-params local-user user "admin" console member ["administrative"] }',
        parents=(),
    ),
]
