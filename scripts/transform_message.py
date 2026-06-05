from decimal import Decimal, getcontext
from typing import TypedDict


getcontext().prec = 40


def transform_message(raw_message):
    if not raw_message:
        return None

    bin_label = raw_message['fields']['label']
    reversed_label = bin_label[::-1]

    try:    
        processed_label = format(int(reversed_label, 2), '03o')
    except ValueError:
        processed_label = None

    a_737_labels = [ "317", "210", "211", "010", "223", "266", "267", "264", "324", "127", "320", "126", "031", "030", "377", "153"]
    if processed_label in a_737_labels:
        message_group = "A-737"
    else:
        message_group = None

    processed_data = get_processed_data_by_label(processed_label, raw_message['fields']['data'])

    processed_message = {
        "channel": raw_message['channel'],
        "raw_message": raw_message['binary'],
        "raw_fields": {
            "label": raw_message['fields']['label'],
            "data": raw_message['fields']['data'],
            "parity": raw_message['fields']['parity'],
        },
        "processed_fields": {
            "label": processed_label,
            "data": processed_data
        },
        "message_group": message_group
    }

    return processed_message


def get_processed_data(
    binary_str: str,
    start_pos: int,
    end_pos: int,
    min_val: float,
    max_val: float
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

    return format(result, 'f')


def get_processed_data_by_label(label: str, raw_data: str):
    class LabelConfig(TypedDict):
        start_pos: int
        end_pos: int
        min_val: float
        max_val: float

    LABEL_CONFIG: dict[str, LabelConfig] = {
        "210": {
            "start_pos": 2,
            "end_pos": 23,
            "min_val": 0,
            "max_val": 90 * 2,
        },
        "211": {
            "start_pos": 2,
            "end_pos": 23,
            "min_val": 0,
            "max_val": 90 * 2,
        },
        "223": {
            "start_pos": 2,
            "end_pos": 23,
            "min_val": 0,
            "max_val": 65536 * 2,
        },
        "266": {
            "start_pos": 2,
            "end_pos": 23,
            "min_val": 0,
            "max_val": 3034.3168 * 2,
        },
        "267": {
            "start_pos": 2,
            "end_pos": 23,
            "min_val": 0,
            "max_val": 3034.3168 * 2,
        },
        "264": {
            "start_pos": 2,
            "end_pos": 23,
            "min_val": 0,
            "max_val": 3034.3168 * 2,
        },
        "127": {
            "start_pos": 2,
            "end_pos": 23,
            "min_val": 0,
            "max_val": 104857.6 * 2,
        },
        "320": {
            "start_pos": 2,
            "end_pos": 17,
            "min_val": 0,
            "max_val": 16384 * 2,
        },
    }

    config = LABEL_CONFIG.get(label)
    if not config:
        return None
    
    return get_processed_data(
        raw_data,
        config["start_pos"],
        config["end_pos"],
        config["min_val"],
        config["max_val"],
    )
