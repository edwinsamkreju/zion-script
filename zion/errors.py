class ZionError(Exception):
    """A friendly error caused by invalid ZION source code."""
    def __init__(self, message: str, line: int | None = None):
        self.message = message
        self.line = line
        super().__init__((f"Line {line}: " if line else "") + message)
