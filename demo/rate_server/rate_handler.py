import threading
import socket


class rate_handler(threading.Thread):
    """some thread"""

    def __init__(self, conn: socket):
        threading.Thread.__init__(self)
        self.conn = conn

    # the run method is what runs when you call "start"
    def run(self) -> None:
        #b is shortcut of encode.utf8
        self.conn.sendall(b"connected to the rate server")

        while True:
            message =self.conn.recv(2048).decode("UTF-8")
            if not message:
                break
            print(f"recv: {message}")
            self.conn.sendall(message.encode("UTF-8"))