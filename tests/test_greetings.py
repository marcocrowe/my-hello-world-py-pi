"""
Test cases for the greetings module of the project
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
"""

from hello_world import greet


def test_greet() -> None:
    """Test the greet function."""
    assert greet() == "Hello, world!"
