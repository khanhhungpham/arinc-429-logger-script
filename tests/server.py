import socket
import time

HOST = "0.0.0.0"
PORT = 10001

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
                    conn.sendall(b"Abbeilkib\n")
                    time.sleep(0.1)  # tránh spam quá nhanh
            except (BrokenPipeError, ConnectionResetError):
                print("Client disconnected")

if __name__ == "__main__":
    run_server()
