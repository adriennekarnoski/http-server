"""."""
import socket


def server():
    """."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 4000))
    server.listen(1)

    while True:
        conn, addr = server.accept()
        try:
            data = conn.recv(10)
            if data:
                conn.sendall(data)
                print(data)
            else:
                conn.sendall('enter valid data')
        except KeyboardInterrupt:
            conn.shutdown()
            conn.close()
            break

if __name__ == '__main__':
    try:
        server()
    except KeyboardInterrupt:
        pass

