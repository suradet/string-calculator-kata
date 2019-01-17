"""A string calculator."""


def add(numbers: str) -> int:
    """Add the numbers."""
    if numbers == "":
        return 0

    delimiter = ','

    def split(string_):
        return string_.split(delimiter)

    lines = numbers.splitlines()
    if "//" in lines[0].strip():
        delimiter = lines[0][2]
        lines = lines[1:]
    num_str_list = sum(map(split, lines), [])
    return sum(map(int, num_str_list))
