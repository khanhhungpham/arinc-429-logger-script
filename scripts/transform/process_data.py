from decimal import Decimal, getcontext

from scripts.transform.message_groups import MESSAGE_GROUPS

getcontext().prec = 40


def get_processed_data(
    message_group: str, label: str, raw_data: str
) -> dict[str, str] | None:
    configs = MESSAGE_GROUPS[message_group][label].get("fields")
    if configs is None:
        return None

    result: dict[str, str] = {}

    for config in configs:
        value = compute_data(
            raw_data,
            config["start_pos"],
            config["end_pos"],
            config["min_val"],
            config["max_val"],
        )

        if value is not None:
            result[config["name"]] = value

    return result if result else None


def compute_data(
    binary_str: str, start_pos: int, end_pos: int, min_val: float, max_val: float
) -> str | None:
    if max_val < min_val:
        return None

    if not (0 <= start_pos < end_pos <= len(binary_str)):
        return None
    bit_count = end_pos - start_pos

    sub_str = binary_str[start_pos:end_pos]

    try:
        raw_val = int(sub_str, 2)
    except ValueError:
        return None

    min_decimal = Decimal(str(min_val))
    max_decimal = Decimal(str(max_val))

    scale = (max_decimal - min_decimal) / (Decimal(2) ** bit_count)

    result = (scale * Decimal(raw_val)).normalize() + min_decimal

    return format(result, "f")
