"""Demo module: after clone, use ``import test`` or ``from test import hello, GREETING``."""

GREETING = "hello world!"


def hello():
    """Print the greeting."""
    print(GREETING)


__all__ = ["GREETING", "hello"]


if __name__ == "__main__":
    hello()
