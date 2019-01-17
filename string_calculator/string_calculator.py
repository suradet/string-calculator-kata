"""A string calculator."""


def add(numbers: str) -> int:
    """Add the numbers."""
    if numbers == "":
        return 0
    else:
        return int(numbers)
