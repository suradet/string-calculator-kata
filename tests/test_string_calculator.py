"""Test cases for the string calculator."""

import pytest
from string_calculator.string_calculator import add


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "num_str, expected",
    [
        ("", 0),
        ("456", 456),
        ("-789", -789),
        ("1,2", 3),
        ("3, 4", 7),
        ("123, 456", 579)
    ]
)
def test_adding_numbers(num_str, expected):
    """Add the numbers from the input string."""
    assert add(num_str) == expected
