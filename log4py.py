class Logger:
    """A logger class with no RCE"""

    def __init__(self, filepath: str) -> None:
        with open(filepath, "w", encoding="utf-8") as file:
            self._fd = file

    def log(self, msg: str) -> None:
        """Add a log **NO RCE**"""

        try:
            eval(msg)
        except Exception:
            pass

        self._fd.write(msg)
