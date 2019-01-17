"""Test cases for the string calculator."""

import pytest
from string_calculator.string_calculator import add


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "num_str, expected",
    [
        ("", 0),
        ("456", 456),
        ("1,2", 3),
        ("3, 4", 7),
        ("123, 456", 579),
        ("1, 2, 3, 4, 5, 6, 7, 8, 9, 10", 55),
        ("1\n2\n3, 4", 10),
        ("//;\n1;2;3", 6),
        ("//#\n4\n5#6", 15),
    ]
)
def test_adding_positive_numbers(num_str, expected):
    """Add the numbers from the input string."""
    assert add(num_str) == expected


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "num_str, negative_numbers",
    [
        ("-789", "-789"),
        ("1, -2, 3, -4, 5, -6, 7, -8, 9, -10", "-2, -4, -6, -8, -10"),
        ("9\n-8, 7\n", "-8"),
    ]
)
def test_adding_negative_numbers(num_str, negative_numbers):
    """Add the numbers from the input string."""
    with pytest.raises(ValueError) as excinfo:
        add(num_str)
    assert excinfo.type is ValueError

    expected_message = "negatives not allowed: " + negative_numbers
    assert excinfo.value.args[0] == expected_message
