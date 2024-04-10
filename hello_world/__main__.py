"""
This is the hello_world package.
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
"""

from . import goodbye
from . import greet


def main() -> None:
    """Prints 'Hello, World!' to the console."""
    greet()
    goodbye()

if __name__ == "__main__":
    main()
