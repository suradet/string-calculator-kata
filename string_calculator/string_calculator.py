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
    # Flatten the list of lists
    num_str_list = sum(map(split, lines), [])
    values = map(int, num_str_list)
    negative_numbers = list(filter(lambda x: x < 0, values))
    if negative_numbers != []:
        message = "negatives not allowed: "
        message += ", ".join(map(str, negative_numbers))
        raise ValueError(message)
    return sum(map(int, num_str_list))
