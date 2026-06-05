import argparse
import sqlite3

from extract_message import extract_message
from load_message import load_message
from transform_message import transform_message


def get_db():
    conn = sqlite3.connect("arinc_429_messages.db")
    conn.execute('PRAGMA journal_mode=WAL;')

    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS arinc_429_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            channel INTEGER,
            raw_message TEXT,
            raw_parity_field TEXT,
            raw_data_field TEXT,
            raw_label_field TEXT,
            processed_label_field TEXT,
            message_group TEXT,
            processed_data_field TEXT
        )
    ''')

    return conn


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TCP client receiving data from an ARINC 429 LAN board")
    parser.add_argument(
        "--host", 
        type=str, 
        default="192.168.24.190", 
        help="Board IP address (default: 192.168.24.190)"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=10001, 
        help="Board port number (default: 10001)"
    )
    args = parser.parse_args()

    db_conn = get_db()
    for raw_message in extract_message(args.host, args.port):
        if raw_message:
            processed_message = transform_message(raw_message)
            if processed_message:
                load_message(db_conn, processed_message)
