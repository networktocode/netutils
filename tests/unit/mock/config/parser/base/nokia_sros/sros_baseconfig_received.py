from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="exit all", parents=()),
    ConfigLine(config_line="configure", parents=()),
    ConfigLine(config_line="System Configuration", parents=()),
    ConfigLine(config_line="    system", parents=("System Configuration",)),
    ConfigLine(config_line='        name "sros-r1"', parents=("System Configuration", "    system")),
    ConfigLine(config_line="        netconf", parents=("System Configuration", "    system")),
    ConfigLine(
        config_line="            auto-config-save", parents=("System Configuration", "    system", "        netconf")
    ),
    ConfigLine(
        config_line="            no shutdown", parents=("System Configuration", "    system", "        netconf")
    ),
    ConfigLine(config_line="        exit", parents=("System Configuration", "    system")),
    ConfigLine(config_line="        snmp", parents=("System Configuration", "    system")),
    ConfigLine(config_line="            streaming", parents=("System Configuration", "    system", "        snmp")),
    ConfigLine(
        config_line="                no shutdown",
        parents=("System Configuration", "    system", "        snmp", "            streaming"),
    ),
    ConfigLine(config_line="            exit", parents=("System Configuration", "    system", "        snmp")),
    ConfigLine(
        config_line="            packet-size 9216", parents=("System Configuration", "    system", "        snmp")
    ),
    ConfigLine(config_line="        exit", parents=("System Configuration", "    system")),
    ConfigLine(config_line="        time", parents=("System Configuration", "    system")),
    ConfigLine(config_line="            sntp", parents=("System Configuration", "    system", "        time")),
    ConfigLine(
        config_line="                shutdown",
        parents=("System Configuration", "    system", "        time", "            sntp"),
    ),
    ConfigLine(config_line="            exit", parents=("System Configuration", "    system", "        time")),
    ConfigLine(config_line="            zone UTC", parents=("System Configuration", "    system", "        time")),
    ConfigLine(config_line="        exit", parents=("System Configuration", "    system")),
    ConfigLine(config_line="        bluetooth", parents=("System Configuration", "    system")),
    ConfigLine(config_line="            module A", parents=("System Configuration", "    system", "        bluetooth")),
    ConfigLine(config_line="            exit", parents=("System Configuration", "    system", "        bluetooth")),
    ConfigLine(
        config_line="            power off", parents=("System Configuration", "    system", "        bluetooth")
    ),
    ConfigLine(config_line="        exit", parents=("System Configuration", "    system")),
    ConfigLine(config_line="    exit", parents=("System Configuration",)),
    ConfigLine(config_line="System Security Configuration", parents=()),
    ConfigLine(config_line="    system", parents=("System Security Configuration",)),
    ConfigLine(config_line="        security", parents=("System Security Configuration", "    system")),
    ConfigLine(
        config_line='            profile "administrative"',
        parents=("System Security Configuration", "    system", "        security"),
    ),
    ConfigLine(
        config_line="                netconf",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line="                    base-op-authorization",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                netconf",
        ),
    ),
    ConfigLine(
        config_line="                        kill-session",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                netconf",
            "                    base-op-authorization",
        ),
    ),
    ConfigLine(
        config_line="                        lock",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                netconf",
            "                    base-op-authorization",
        ),
    ),
    ConfigLine(
        config_line="                    exit",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                netconf",
        ),
    ),
    ConfigLine(
        config_line="                exit",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line="                entry 10",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line='                    match "configure system security"',
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 10",
        ),
    ),
    ConfigLine(
        config_line="                    action permit",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 10",
        ),
    ),
    ConfigLine(
        config_line="                exit",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line="                entry 20",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line='                    match "show system security"',
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 20",
        ),
    ),
    ConfigLine(
        config_line="                    action permit",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 20",
        ),
    ),
    ConfigLine(
        config_line="                exit",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line="                entry 30",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line='                    match "tools perform security"',
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 30",
        ),
    ),
    ConfigLine(
        config_line="                    action permit",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 30",
        ),
    ),
    ConfigLine(
        config_line="                exit",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line="                entry 40",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line='                    match "tools dump security"',
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 40",
        ),
    ),
    ConfigLine(
        config_line="                    action permit",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 40",
        ),
    ),
    ConfigLine(
        config_line="                exit",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line="                entry 50",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line='                    match "admin system security"',
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 50",
        ),
    ),
    ConfigLine(
        config_line="                    action permit",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 50",
        ),
    ),
    ConfigLine(
        config_line="                exit",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line="                entry 100",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line='                    match "configure li"',
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 100",
        ),
    ),
    ConfigLine(
        config_line="                    action deny",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 100",
        ),
    ),
    ConfigLine(
        config_line="                exit",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line="                entry 110",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line='                    match "show li"',
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 110",
        ),
    ),
    ConfigLine(
        config_line="                    action deny",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 110",
        ),
    ),
    ConfigLine(
        config_line="                exit",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line="                entry 111",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line='                    match "clear li"',
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 111",
        ),
    ),
    ConfigLine(
        config_line="                    action deny",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 111",
        ),
    ),
    ConfigLine(
        config_line="                exit",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line="                entry 112",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line='                    match "tools dump li"',
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 112",
        ),
    ),
    ConfigLine(
        config_line="                    action deny",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
            "                entry 112",
        ),
    ),
    ConfigLine(
        config_line="                exit",
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            profile "administrative"',
        ),
    ),
    ConfigLine(
        config_line="            exit", parents=("System Security Configuration", "    system", "        security")
    ),
    ConfigLine(
        config_line='            user "admin"',
        parents=("System Security Configuration", "    system", "        security"),
    ),
    ConfigLine(
        config_line='                password "$2y$10$TQrZlpBDra86.qoexZUzQeBXDY1FcdDhGWdD9lLxMuFyPVSm0OGy6"',
        parents=("System Security Configuration", "    system", "        security", '            user "admin"'),
    ),
    ConfigLine(
        config_line="                access console ftp snmp netconf grpc",
        parents=("System Security Configuration", "    system", "        security", '            user "admin"'),
    ),
    ConfigLine(
        config_line="                console",
        parents=("System Security Configuration", "    system", "        security", '            user "admin"'),
    ),
    ConfigLine(
        config_line='                    member "administrative"',
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            user "admin"',
            "                console",
        ),
    ),
    ConfigLine(
        config_line="                exit",
        parents=("System Security Configuration", "    system", "        security", '            user "admin"'),
    ),
    ConfigLine(
        config_line="            exit", parents=("System Security Configuration", "    system", "        security")
    ),
    ConfigLine(
        config_line='            user "vrnetlab"',
        parents=("System Security Configuration", "    system", "        security"),
    ),
    ConfigLine(
        config_line='                password "$2y$10$zjlEA0qAfjuXNwo1gXA5..BImKLQpWGaJNZ7SIidoHJ59vu7haI7C"',
        parents=("System Security Configuration", "    system", "        security", '            user "vrnetlab"'),
    ),
    ConfigLine(
        config_line="                access console netconf",
        parents=("System Security Configuration", "    system", "        security", '            user "vrnetlab"'),
    ),
    ConfigLine(
        config_line="                console",
        parents=("System Security Configuration", "    system", "        security", '            user "vrnetlab"'),
    ),
    ConfigLine(
        config_line='                    member "administrative"',
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            user "vrnetlab"',
            "                console",
        ),
    ),
    ConfigLine(
        config_line='                    member "default"',
        parents=(
            "System Security Configuration",
            "    system",
            "        security",
            '            user "vrnetlab"',
            "                console",
        ),
    ),
    ConfigLine(
        config_line="                exit",
        parents=("System Security Configuration", "    system", "        security", '            user "vrnetlab"'),
    ),
    ConfigLine(
        config_line="            exit", parents=("System Security Configuration", "    system", "        security")
    ),
    ConfigLine(
        config_line="            per-peer-queuing",
        parents=("System Security Configuration", "    system", "        security"),
    ),
    ConfigLine(
        config_line="            dist-cpu-protection",
        parents=("System Security Configuration", "    system", "        security"),
    ),
    ConfigLine(
        config_line='                policy "_default-access-policy" create',
        parents=("System Security Configuration", "    system", "        security", "            dist-cpu-protection"),
    ),
    ConfigLine(
        config_line="                exit",
        parents=("System Security Configuration", "    system", "        security", "            dist-cpu-protection"),
    ),
    ConfigLine(
        config_line='                policy "_default-network-policy" create',
        parents=("System Security Configuration", "    system", "        security", "            dist-cpu-protection"),
    ),
    ConfigLine(
        config_line="                exit",
        parents=("System Security Configuration", "    system", "        security", "            dist-cpu-protection"),
    ),
    ConfigLine(
        config_line="            exit", parents=("System Security Configuration", "    system", "        security")
    ),
    ConfigLine(config_line="        exit", parents=("System Security Configuration", "    system")),
    ConfigLine(config_line="    exit", parents=("System Security Configuration",)),
    ConfigLine(config_line="System Login Control Configuration", parents=()),
    ConfigLine(config_line="    system", parents=("System Login Control Configuration",)),
    ConfigLine(config_line="        login-control", parents=("System Login Control Configuration", "    system")),
    ConfigLine(
        config_line="            ssh",
        parents=("System Login Control Configuration", "    system", "        login-control"),
    ),
    ConfigLine(
        config_line="                inbound-max-sessions 30",
        parents=("System Login Control Configuration", "    system", "        login-control", "            ssh"),
    ),
    ConfigLine(
        config_line="            exit",
        parents=("System Login Control Configuration", "    system", "        login-control"),
    ),
    ConfigLine(config_line="        exit", parents=("System Login Control Configuration", "    system")),
    ConfigLine(config_line="    exit", parents=("System Login Control Configuration",)),
    ConfigLine(config_line="Log Configuration", parents=()),
    ConfigLine(config_line="    log", parents=("Log Configuration",)),
    ConfigLine(config_line="    exit", parents=("Log Configuration",)),
    ConfigLine(config_line="System gRPC Configuration", parents=()),
    ConfigLine(config_line="    system", parents=("System gRPC Configuration",)),
    ConfigLine(config_line="        grpc", parents=("System gRPC Configuration", "    system")),
    ConfigLine(
        config_line="            allow-unsecure-connection",
        parents=("System gRPC Configuration", "    system", "        grpc"),
    ),
    ConfigLine(config_line="            gnmi", parents=("System gRPC Configuration", "    system", "        grpc")),
    ConfigLine(
        config_line="                auto-config-save",
        parents=("System gRPC Configuration", "    system", "        grpc", "            gnmi"),
    ),
    ConfigLine(
        config_line="                no shutdown",
        parents=("System gRPC Configuration", "    system", "        grpc", "            gnmi"),
    ),
    ConfigLine(config_line="            exit", parents=("System gRPC Configuration", "    system", "        grpc")),
    ConfigLine(config_line="            rib-api", parents=("System gRPC Configuration", "    system", "        grpc")),
    ConfigLine(
        config_line="                no shutdown",
        parents=("System gRPC Configuration", "    system", "        grpc", "            rib-api"),
    ),
    ConfigLine(config_line="            exit", parents=("System gRPC Configuration", "    system", "        grpc")),
    ConfigLine(
        config_line="            no shutdown", parents=("System gRPC Configuration", "    system", "        grpc")
    ),
    ConfigLine(config_line="        exit", parents=("System gRPC Configuration", "    system")),
    ConfigLine(config_line="    exit", parents=("System gRPC Configuration",)),
    ConfigLine(config_line="Card Configuration", parents=()),
    ConfigLine(config_line="    card 1", parents=("Card Configuration",)),
    ConfigLine(config_line="        card-type iom-1", parents=("Card Configuration", "    card 1")),
    ConfigLine(config_line="        mda 1", parents=("Card Configuration", "    card 1")),
    ConfigLine(
        config_line="            mda-type me12-100gb-qsfp28",
        parents=("Card Configuration", "    card 1", "        mda 1"),
    ),
    ConfigLine(config_line="            no shutdown", parents=("Card Configuration", "    card 1", "        mda 1")),
    ConfigLine(config_line="        exit", parents=("Card Configuration", "    card 1")),
    ConfigLine(config_line="        no shutdown", parents=("Card Configuration", "    card 1")),
    ConfigLine(config_line="    exit", parents=("Card Configuration",)),
    ConfigLine(config_line="Connector Configuration", parents=()),
    ConfigLine(config_line="    port 1/1/c1", parents=("Connector Configuration",)),
    ConfigLine(config_line="        shutdown", parents=("Connector Configuration", "    port 1/1/c1")),
    ConfigLine(config_line="    exit", parents=("Connector Configuration",)),
    ConfigLine(config_line="    port 1/1/c2", parents=("Connector Configuration",)),
    ConfigLine(config_line="        shutdown", parents=("Connector Configuration", "    port 1/1/c2")),
    ConfigLine(config_line="    exit", parents=("Connector Configuration",)),
    ConfigLine(config_line="    port 1/1/c3", parents=("Connector Configuration",)),
    ConfigLine(config_line="        shutdown", parents=("Connector Configuration", "    port 1/1/c3")),
    ConfigLine(config_line="    exit", parents=("Connector Configuration",)),
    ConfigLine(config_line="    port 1/1/c4", parents=("Connector Configuration",)),
    ConfigLine(config_line="        shutdown", parents=("Connector Configuration", "    port 1/1/c4")),
    ConfigLine(config_line="    exit", parents=("Connector Configuration",)),
    ConfigLine(config_line="    port 1/1/c5", parents=("Connector Configuration",)),
    ConfigLine(config_line="        shutdown", parents=("Connector Configuration", "    port 1/1/c5")),
    ConfigLine(config_line="    exit", parents=("Connector Configuration",)),
    ConfigLine(config_line="    port 1/1/c6", parents=("Connector Configuration",)),
    ConfigLine(config_line="        shutdown", parents=("Connector Configuration", "    port 1/1/c6")),
    ConfigLine(config_line="    exit", parents=("Connector Configuration",)),
    ConfigLine(config_line="    port 1/1/c7", parents=("Connector Configuration",)),
    ConfigLine(config_line="        shutdown", parents=("Connector Configuration", "    port 1/1/c7")),
    ConfigLine(config_line="    exit", parents=("Connector Configuration",)),
    ConfigLine(config_line="    port 1/1/c8", parents=("Connector Configuration",)),
    ConfigLine(config_line="        shutdown", parents=("Connector Configuration", "    port 1/1/c8")),
    ConfigLine(config_line="    exit", parents=("Connector Configuration",)),
    ConfigLine(config_line="    port 1/1/c9", parents=("Connector Configuration",)),
    ConfigLine(config_line="        shutdown", parents=("Connector Configuration", "    port 1/1/c9")),
    ConfigLine(config_line="    exit", parents=("Connector Configuration",)),
    ConfigLine(config_line="    port 1/1/c10", parents=("Connector Configuration",)),
    ConfigLine(config_line="        shutdown", parents=("Connector Configuration", "    port 1/1/c10")),
    ConfigLine(config_line="    exit", parents=("Connector Configuration",)),
    ConfigLine(config_line="    port 1/1/c11", parents=("Connector Configuration",)),
    ConfigLine(config_line="        shutdown", parents=("Connector Configuration", "    port 1/1/c11")),
    ConfigLine(config_line="    exit", parents=("Connector Configuration",)),
    ConfigLine(config_line="    port 1/1/c12", parents=("Connector Configuration",)),
    ConfigLine(config_line="        shutdown", parents=("Connector Configuration", "    port 1/1/c12")),
    ConfigLine(config_line="    exit", parents=("Connector Configuration",)),
    ConfigLine(config_line="Port Configuration", parents=()),
    ConfigLine(config_line="    port A/3", parents=("Port Configuration",)),
    ConfigLine(config_line="        shutdown", parents=("Port Configuration", "    port A/3")),
    ConfigLine(config_line="        ethernet", parents=("Port Configuration", "    port A/3")),
    ConfigLine(config_line="        exit", parents=("Port Configuration", "    port A/3")),
    ConfigLine(config_line="    exit", parents=("Port Configuration",)),
    ConfigLine(config_line="    port A/4", parents=("Port Configuration",)),
    ConfigLine(config_line="        shutdown", parents=("Port Configuration", "    port A/4")),
    ConfigLine(config_line="    exit", parents=("Port Configuration",)),
    ConfigLine(config_line="System Sync-If-Timing Configuration", parents=()),
    ConfigLine(config_line="    system", parents=("System Sync-If-Timing Configuration",)),
    ConfigLine(config_line="        sync-if-timing", parents=("System Sync-If-Timing Configuration", "    system")),
    ConfigLine(
        config_line="            begin",
        parents=("System Sync-If-Timing Configuration", "    system", "        sync-if-timing"),
    ),
    ConfigLine(
        config_line="            commit",
        parents=("System Sync-If-Timing Configuration", "    system", "        sync-if-timing"),
    ),
    ConfigLine(config_line="        exit", parents=("System Sync-If-Timing Configuration", "    system")),
    ConfigLine(config_line="    exit", parents=("System Sync-If-Timing Configuration",)),
    ConfigLine(config_line="Management Router Configuration", parents=()),
    ConfigLine(config_line="    router management", parents=("Management Router Configuration",)),
    ConfigLine(config_line="    exit", parents=("Management Router Configuration",)),
    ConfigLine(config_line="Router (Network Side) Configuration", parents=()),
    ConfigLine(config_line="    router Base", parents=("Router (Network Side) Configuration",)),
    ConfigLine(
        config_line='        interface "system"', parents=("Router (Network Side) Configuration", "    router Base")
    ),
    ConfigLine(
        config_line="            no shutdown",
        parents=("Router (Network Side) Configuration", "    router Base", '        interface "system"'),
    ),
    ConfigLine(config_line="        exit", parents=("Router (Network Side) Configuration", "    router Base")),
    ConfigLine(config_line="    exit", parents=("Router (Network Side) Configuration",)),
    ConfigLine(config_line="Service Configuration", parents=()),
    ConfigLine(config_line="    service", parents=("Service Configuration",)),
    ConfigLine(config_line='        customer 1 name "1" create', parents=("Service Configuration", "    service")),
    ConfigLine(
        config_line='            description "Default customer"',
        parents=("Service Configuration", "    service", '        customer 1 name "1" create'),
    ),
    ConfigLine(config_line="        exit", parents=("Service Configuration", "    service")),
    ConfigLine(config_line="    exit", parents=("Service Configuration",)),
    ConfigLine(config_line="Router (Service Side) Configuration", parents=()),
    ConfigLine(config_line="    router Base", parents=("Router (Service Side) Configuration",)),
    ConfigLine(config_line="    exit", parents=("Router (Service Side) Configuration",)),
    ConfigLine(config_line="Log all events for service vprn Configuration", parents=()),
    ConfigLine(config_line="    log", parents=("Log all events for service vprn Configuration",)),
    ConfigLine(config_line="    exit", parents=("Log all events for service vprn Configuration",)),
    ConfigLine(config_line="System Configuration Mode Configuration", parents=()),
    ConfigLine(config_line="    system", parents=("System Configuration Mode Configuration",)),
    ConfigLine(
        config_line="        management-interface", parents=("System Configuration Mode Configuration", "    system")
    ),
    ConfigLine(
        config_line="            configuration-mode model-driven",
        parents=("System Configuration Mode Configuration", "    system", "        management-interface"),
    ),
    ConfigLine(config_line="        exit", parents=("System Configuration Mode Configuration", "    system")),
    ConfigLine(config_line="    exit", parents=("System Configuration Mode Configuration",)),
    ConfigLine(config_line="exit all", parents=()),
    ConfigLine(config_line="INFO: CLI #2052: Switching to the MD-CLI engine", parents=()),
]
