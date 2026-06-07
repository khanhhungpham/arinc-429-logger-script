from typing import TypedDict


class RawMessage(TypedDict):
    timestamp: str
    string: str
    channel: int
    binary: str
    parity: str
    data: str
    label: str


class GroupResult(TypedDict):
    """Kết quả tính toán cho một message group."""
    description: str | None
    fields: dict[str, str] | None


class ProcessedMessage(TypedDict):
    raw_message: RawMessage
    parity_ok: bool
    label: str | None
    # Key: tên group, Value: description + decoded fields của group đó.
    # None nếu label không khớp bất kỳ group nào.
    processed_data_by_group: dict[str, GroupResult] | None
