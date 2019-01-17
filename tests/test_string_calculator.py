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
        ("123, 456", 579),
        ("1, 2, 3, 4, 5, 6, 7, 8, 9, 10", 55),
        ("1, -2, 3, -4, 5, -6, 7, -8, 9, -10", -5),
        ("1\n2\n3, 4", 10),
        ("9\n-8, 7\n", 8),
    ]
)
def test_adding_numbers(num_str, expected):
    """Add the numbers from the input string."""
    assert add(num_str) == expected
