"""Configuraiton conversion methods for different network operating systems."""
# pylint: disable=no-member,super-with-arguments,invalid-overridden-method,raise-missing-from,invalid-overridden-method,inconsistent-return-statements,super-with-arguments,redefined-argument-from-local,no-else-break,useless-super-delegation,too-many-lines


def paloalto_panos_brace_to_set(config) -> list:
    """Convert Palo Alto Brace/JSON format configuration to set format."""
    stack = []
    output_lines = []
    config_value = ""

    for line in config:
        line = line.strip()
        if line.endswith(";"):
            line = line.split(";", 1)[0]
            line = "".join(stack) + line
            line = line.split("config ", 1)[1]
            line = "set " + line
            output_lines.append(line)
        elif line.endswith('login-banner "') or line.endswith('content "'):
            config_value = "".join(stack) + line
            config_value = "set " + config_value.split("config ", 1)[1]
            output_lines.append(config_value)

            for another_line in config:
                if '"' in another_line:
                    another_line = another_line.split(";", 1)[0]
                    output_lines.append(" " + another_line.strip())
                    break
                output_lines.append(" " + another_line.strip())
        elif line.endswith("{"):
            stack.append(line[:-1])
        elif line == "}" and len(stack) > 0:
            stack.pop()

    return output_lines
