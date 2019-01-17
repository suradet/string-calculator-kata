"""Test cases for the string calculator."""

import pytest
from string_calculator.string_calculator import add


# -----------------------------------------------------------------------------
def test_input_with_empty_string():
    """Input with empty string."""
    assert add("") == 0


# -----------------------------------------------------------------------------
def test_input_with_one_number():
    """Input with one number."""
    assert add("123") == 123


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "num_str, expected",
    [
        ("", 0),
        ("456", 456),
        ("-789", -789),
    ]
)
def test_adding_numbers(num_str, expected):
    """Add the numbers from the input string."""
    assert add(num_str) == expected
