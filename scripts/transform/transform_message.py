from scripts.transform.check_parity import get_parity_check
from scripts.transform.process_data import get_processed_data
from scripts.transform.process_label import (
    get_processed_label,
    get_all_message_groups,
    get_message_description,
)
from scripts.schemas import RawMessage, ProcessedMessage


def transform_message(raw_message: RawMessage) -> ProcessedMessage | None:
    """
    Transform một raw ARINC 429 message thành đúng 1 ProcessedMessage (= 1 row DB).

    Với label trùng nhiều group, tất cả cách tính được gộp vào
    processed_data_by_group (dict keyed theo tên group).
    """
    if not raw_message:
        return None

    parity_ok = get_parity_check(raw_message["binary"])
    processed_label = get_processed_label(raw_message["label"])

    matching_groups = get_all_message_groups(processed_label) if processed_label else []

    if not matching_groups:
        return {
            "raw_message": raw_message,
            "parity_ok": parity_ok,
            "label": processed_label,
            "processed_data_by_group": None,
        }

    processed_data_by_group = {}
    for group in matching_groups:
        processed_data_by_group[group] = {
            "description": get_message_description(group, processed_label),
            "fields": get_processed_data(group, processed_label, raw_message["data"]),
        }

    return {
        "raw_message": raw_message,
        "parity_ok": parity_ok,
        "label": processed_label,
        "processed_data_by_group": processed_data_by_group,
    }
