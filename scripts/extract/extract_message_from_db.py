import sqlite3
from typing import Iterator

from scripts.schemas import RawMessage


def extract_message_from_db() -> Iterator[RawMessage]:
    conn = sqlite3.connect("arinc_429_log.db")
    conn.execute("PRAGMA journal_mode=WAL;")

    cursor = conn.cursor()
    cursor.execute("""
        SELECT timestamp, channel, raw_message
        FROM arinc_429_messages
        ORDER BY id DESC
    """)

    for timestamp, channel, raw_message in cursor:
        parity = raw_message[0]
        data = raw_message[1:24]
        label = raw_message[24:32]
        yield {
            "timestamp": timestamp,
            "string": None,
            "channel": channel,
            "binary": raw_message,
            "parity": parity,
            "data": data,
            "label": label,
        }
