import socket
import time


def extract_message(host: str, port: int):
    while True:
        buffer = ""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                print(f"[INFO] Connecting to the ARINC 429 LAN board at {host}:{port}...")
                client_socket.settimeout(5)
                client_socket.connect((host, port))
                print(f"[INFO] Connected to the ARINC 429 LAN board at {host}:{port}")

                while True:
                    data = client_socket.recv(4096)

                    if not data:
                        print("[INFO] Connection closed")
                        break

                    buffer += data.decode('ascii', errors='ignore')
                    lines = buffer.split('\n')
                    buffer = lines.pop()

                    for line in lines:
                        raw_message = decode_arinc_429_word(line)
                        print(raw_message)
                        yield raw_message


        except Exception as e:
            print(f"[ERROR] Network: {e}")

        print("[INFO] Reconnecting...")
        time.sleep(1)


def decode_arinc_429_word(raw_str):
    if not raw_str or len(raw_str) != 9:
        return None

    try:
        first_char = raw_str[0]
        if not first_char.isupper():
            return None
        channel = ord(first_char) - 64

        payload = raw_str[1:]
        reversed_payload = payload[::-1]

        binary_str = ""
        for char in reversed_payload:
            val = ord(char) - 97
            if 0 <= val <= 15:
                binary_str += format(val, '04b')
            else:
                return None

        final_bits = binary_str[::-1]

        parity = final_bits[0]
        data   = final_bits[1:24]
        label  = final_bits[24:32]

        result = {
            "channel": channel,
            "binary": final_bits,
            "fields": {
                "parity": parity,
                "data": data,
                "label": label
            }
        }
        return result

    except Exception as e:
        print(f"[ERROR] Decoding: {e}")
        return None
