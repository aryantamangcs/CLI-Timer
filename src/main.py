from .cli import CLIInterface
from .timer import Timer


def main():
    """
    main entry point
    """

    cli = CLIInterface.init()
    if not cli:
        print("Error while initiating cli")
    timer = Timer.set(minutes=cli.minutes)
    timer.start()


if __name__ == "__main__":
    main()
