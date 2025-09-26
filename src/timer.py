import logging
import platform
import subprocess
from time import sleep

logger = logging.getLogger(__name__)


class Timer:
    """
    Timer class
    """

    def __init__(self, minutes: int):
        self.minutes = minutes
        self.file = "assets/phone-incoming-call.oga"

    @classmethod
    def set(cls, minutes):
        """
        Returns an instance of timer
        """
        return cls(minutes)

    def start(self):
        """
        tracks time
        """

        seconds = self.get_seconds(self.minutes)

        while seconds != 0:
            logger.info("%s seconds remaining", seconds)
            print(f"{seconds} seconds remaining")
            sleep(1)
            seconds = seconds - 1

        self.ring_bell()

    def get_seconds(self, minutes: int) -> int:
        """
        returns the corresponding seconds of minutes
        """
        return minutes * 60

    def ring_bell(self):
        """
        Rings the bell
        """
        if platform.system() == "Windows":
            subprocess.run(["start", self.file], shell=True)
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", self.file])
        else:  # Linux
            subprocess.run(["xdg-open", self.file])
