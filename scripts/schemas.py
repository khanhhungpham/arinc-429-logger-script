from typing import TypedDict

class RawMessage(TypedDict):
    channel: int
    string: str
    binary: str
    parity: str
    data: str
    label: str

class ProcessedMessage(TypedDict):
    raw_message: RawMessage
    label: str
    message_group: str
    data: str
