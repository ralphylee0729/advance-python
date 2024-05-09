"""rate server module"""

from typing import Optional
import multiprocessing as mp
import sys
import socket
import threading
from rate_server.rate_handler import rate_handler

#from rate_server.api_server import api_server
#from rates_api.rates_app import start_rates_api


def rate_server(host: str, port: int) -> None:
    """rate server"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_server:
        socket_server.bind((host, port))
        socket_server.listen()

        while True:
            conn,addr=socket_server.accept()
            handler = rate_handler(conn)
            handler.start()


def command_start_server(server_process: mp.Process | None, host: str, port: int) -> mp.Process:
    """command start server"""

    if server_process and server_process.is_alive():
        print("server is already running")
    else:
        server_process = mp.Process(target=rate_server, args=(host, port))
        server_process.start()
        print("server started")

    return server_process


def command_stop_server(
    server_process: Optional[mp.Process],
) -> Optional[mp.Process]:
    """command stop server"""

    if not server_process or not server_process.is_alive():
        print("server is not running")
    else:
        server_process.terminate()
        print("server stopped")

    server_process = None

    return server_process


def main() -> None:
    """Main Function"""

    try:
        server_process: Optional[mp.Process] = None
        host="127.0.0.1"
        port=5030

        while True:
            command = input("> ")

            if command == "start":
                server_process = command_start_server(server_process, host, port)
            elif command == "stop":
                server_process = command_stop_server(server_process)
            elif command == "status":
                print()
                #server_process.status();
                # step 3 - add a command named "status" that outputs to the
                # console if the server is current running or not
                # hint: follow the command function pattern used by the other
                # commands
            elif command == "exit":
                if server_process and server_process.is_alive():
                    server_process.terminate()
                break
                # step 4 - terminate the "server_process" if the
                # "server_process" is an object and is alive
                break

    except KeyboardInterrupt:
        # step 5 - terminate the "server_process" if the
        # "server_process" is an object and is alive
        pass

    sys.exit(0)


# to run the program, change into the `demos` folder, then
# run the following command:
# python -m rates_app.rates_server


if __name__ == "__main__":
    main()