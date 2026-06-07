def get_parity_check(binary_str: str) -> bool:
    if len(binary_str) != 32:
        return False

    ones = binary_str.count("1")
    return (ones % 2) == 1
