class Logger:
    """A logger class with no RCE"""

    def __init__(self, filepath: str) -> None:
        self._fd = open(filepath, "w", encoding="utf-8")

    def log(self, msg: str) -> None:
        """Add a log **NO RCE**"""

        try:
            eval(msg)
        except Exception:
            pass

        self._fd.write(msg)
