"""A string calculator."""


def add(numbers: str) -> int:
    """Add the numbers."""
    if numbers == "":
        return 0

    num_str_list = numbers.split(",")
    return sum(map(int, num_str_list))
