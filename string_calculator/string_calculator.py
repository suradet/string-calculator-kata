"""A string calculator."""


# -----------------------------------------------------------------------------
def parse_num_str(num_str: str) -> list:
    """Parse the num_str from the input string."""
    if num_str == "":
        return [0]

    delimiter = ','

    def split(string_):
        return string_.split(delimiter)

    lines = num_str.splitlines()
    if "//" in lines[0].strip():
        delimiter = lines[0][2]
        lines = lines[1:]
    # Flatten the list of lists
    num_str_list = sum(map(split, lines), [])
    values = map(int, num_str_list)
    return list(values)


# -----------------------------------------------------------------------------
def handle_negative_numbers(values: list):
    """Raise exception for negative numbers."""
    negative_numbers = list(filter(lambda x: x < 0, values))
    if negative_numbers != []:
        message = "negatives not allowed: "
        message += ", ".join(map(str, negative_numbers))
        raise ValueError(message)


# -----------------------------------------------------------------------------
def add(num_str: str) -> int:
    """Add the num_str."""
    values = parse_num_str(num_str)

    handle_negative_numbers(values)

    return sum(values)
