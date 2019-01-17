"""A string calculator."""


def add(numbers: str) -> int:
    """Add the numbers."""
    if numbers == "":
        return 0

    def split(string_):
        return string_.split(',')

    lines = numbers.splitlines()
    num_str_list = sum(map(split, lines), [])
    return sum(map(int, num_str_list))
