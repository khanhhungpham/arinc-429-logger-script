import argparse

from scripts.extract.extract_message_from_board import extract_message_from_board
from scripts.load.load_message import load_message
from scripts.transform.transform_message import transform_message

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="TCP client receiving data from an ARINC 429 LAN board"
    )

    parser.add_argument(
        "--host",
        type=str,
        default="192.168.24.190",
        help="board ip address (default: 192.168.24.190)",
    )

    parser.add_argument(
        "--port", type=int, default=10001, help="board port number (default: 10001)"
    )

    args = parser.parse_args()

    for raw_message in extract_message_from_board(args.host, args.port):
        if raw_message:
            processed_message = transform_message(raw_message)
            if processed_message:
                load_message(processed_message)
