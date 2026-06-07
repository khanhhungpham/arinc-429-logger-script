import time
import socket

HOST = "0.0.0.0"
PORT = 10001


def encode_arinc_429_word(binary_str: str, channel: int = 1) -> str | None:
    if (
        not binary_str
        or len(binary_str) != 32
        or any(c not in "01" for c in binary_str)
    ):
        return None

    try:
        if not (1 <= channel <= 26):
            return None
        first_char = chr(channel + 64)

        reversed_bits = binary_str[::-1]

        nibbles = [reversed_bits[i : i + 4] for i in range(0, 32, 4)]

        payload_chars = []
        for nibble in nibbles:
            val = int(nibble, 2)
            if 0 <= val <= 15:
                payload_chars.append(chr(val + 97))
            else:
                return None

        payload = "".join(payload_chars)[::-1]

        return first_char + payload

    except Exception as e:
        print(f"[ERROR] Encoding: {e}")
        return None


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)

        print(f"Listening on {HOST}:{PORT}...")

        conn, addr = server.accept()
        with conn:
            print(f"Client connected: {addr}")

            try:
                while True:
                    binary = "10001000001000011101010100110011"
                    encoded = encode_arinc_429_word(binary)
                    if encoded is None:
                        print("Encode failed")
                        return
                    payload = (encoded + "\n").encode("ascii")
                    conn.sendall(payload)
                    time.sleep(0.1)

            except (BrokenPipeError, ConnectionResetError):
                print("Client disconnected")


if __name__ == "__main__":
    run_server()
