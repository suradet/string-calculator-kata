"""Test cases for the string calculator."""

from string_calculator.string_calculator import add


# -----------------------------------------------------------------------------
def test_input_with_empty_string():
    """Input with empty string."""
    assert add("") == 0
