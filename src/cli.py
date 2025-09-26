import sys


class CLIInterface:
    """
    CLI interface class
    """

    def __init__(self, minutes: int):
        self.minutes = minutes

    @classmethod
    def init(cls):
        """
        Initializes the cli
        """
        try:
            str_minutes = str(sys.argv[1])
            minutes = int(str_minutes)
            return cls(minutes=minutes)
        except Exception:  # pylint: disable=broad-except
            print("Invalid input. Input must be integer")
            return None

    def __str__(self):
        return f"{self.minutes} CLI interface"

    def __repr__(self):
        return f"CLIInterface(minutes={self.minutes})"
