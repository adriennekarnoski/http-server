"""."""
import socket


def server():
    """."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind('127.0.0.1', 5000)
    server.listen(10)

    while True:
        conn, addr = server.accept()
        try:
            data = server.recv(500)
            if data:
                server.sendall(data)
                print(data)
            else:
                server.sendall('enter valid data')
        except KeyboardInterrupt:
            server.shutdown()
            server.close()
            break

if __name__ == '__main__':
    try:
        server()
    except KeyboardInterrupt:
        pass


