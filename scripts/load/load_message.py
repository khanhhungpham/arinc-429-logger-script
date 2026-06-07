import json
import sqlite3
import os
from datetime import datetime

from scripts.schemas import ProcessedMessage

# ── Output root & session folder ──────────────────────────────────────────────
OUTPUTS_ROOT = "outputs"
SESSION_DIR = os.path.join(OUTPUTS_ROOT, datetime.now().strftime("%Y%m%d_%H%M%S"))
os.makedirs(SESSION_DIR, exist_ok=True)

print(f"[INFO] Session output folder: {SESSION_DIR}/")

# ── Single DB for the whole session ───────────────────────────────────────────
_DB_PATH = os.path.join(SESSION_DIR, "arinc_429_messages.db")
_conn = sqlite3.connect(_DB_PATH)
_conn.execute("PRAGMA journal_mode=WAL;")
_conn.execute("""
    CREATE TABLE IF NOT EXISTS arinc_429_messages (
        id                      INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp               DATETIME,
        raw_string              TEXT,
        channel                 INTEGER,
        raw_message             TEXT,
        raw_parity              TEXT,
        raw_data                TEXT,
        raw_label               TEXT,
        parity_ok               BOOLEAN,
        processed_label         TEXT,
        processed_data_by_group TEXT
    )
""")
_conn.commit()

_INSERT_SQL = """
    INSERT INTO arinc_429_messages
        (timestamp, raw_string, channel, raw_message, raw_parity, raw_data,
         raw_label, parity_ok, processed_label, processed_data_by_group)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""


def load_message(message: ProcessedMessage) -> None:
    if not message:
        return

    processed_data_by_group_json = (
        json.dumps(message["processed_data_by_group"], ensure_ascii=False)
        if message["processed_data_by_group"] is not None
        else None
    )

    try:
        _conn.execute(
            _INSERT_SQL,
            (
                message["raw_message"]["timestamp"],
                message["raw_message"]["string"],
                message["raw_message"]["channel"],
                message["raw_message"]["binary"],
                message["raw_message"]["parity"],
                message["raw_message"]["data"],
                message["raw_message"]["label"],
                message["parity_ok"],
                message["label"],
                processed_data_by_group_json,
            ),
        )
        _conn.commit()

    except Exception as e:
        print(f"[ERROR] Database insertion: {e}")
