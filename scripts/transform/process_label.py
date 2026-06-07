from scripts.transform.message_groups import MESSAGE_GROUPS


def get_processed_label(raw_label: str) -> str | None:
    reversed_raw_label = raw_label[::-1]

    try:
        return format(int(reversed_raw_label, 2), "03o")
    except ValueError:
        return None


def get_all_message_groups(processed_label: str) -> list[str]:
    """Return all groups that contain this label (handles duplicate labels)."""
    return [
        group
        for group, labels in MESSAGE_GROUPS.items()
        if processed_label in labels
    ]


def get_message_description(message_group: str, processed_label: str) -> str | None:
    label_config = MESSAGE_GROUPS[message_group].get(processed_label)
    if label_config is None:
        return None

    return label_config.get("description")
