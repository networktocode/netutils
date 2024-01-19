data = {
    "compliant": False,
    "missing": "banner exec ^C\n=========\nintended config exec banner\n-========^C\n",
    "extra": "banner exec ^C\n=========\nactual config exec banner\n-========^C\n",
    "cannot_parse": True,
    "unordered_compliant": False,
    "ordered_compliant": False,
    "actual": "hostname dual-banner\n!\nbanner exec ^C\n=========\nactual config exec banner\n-========\n^C\nbanner motd ^C\n======\nactual config motd banner\n======\n   || ($hostname) ||\n^C\n!\n",
    "intended": "hostname dual-banner\n!\nbanner exec ^C\n=========\nintended config exec banner\n-========\n^C\nbanner motd ^C\n======\nintended config motd banner\n======\n   || ($hostname) ||\n^C\n!",
}
