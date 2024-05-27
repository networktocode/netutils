"""Hier Config Exceptions."""


class HostAttrError(Exception):
    """Hier Config Host attribute exception."""

    def __init__(self, expression, message):
        """Initialize exception."""
        self.expression = expression
        self.message = message
        super().__init__(f"{expression}: {message}")


class HierConfigError(Exception):
    """Hier Config generic exception."""

    def __init__(self, message):
        """Initialize exception."""
        self.message = message
        super().__init__(f"{message}")
