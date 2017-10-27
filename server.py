"""."""
import socket


def server():
    """."""
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )
    server.bind(('127.0.0.1', 4000))
    server.listen(1)
    msg = ''
    buffer_len = 8
    ending = False
    while True:
        try:
            conn, addr = server.accept()
            while not ending:
                data = (conn.recv(buffer_len)).decode('utf8')
                msg += data
                if data.endswith('*'):
                    conn.send(msg.encode('utf8'))
                    print(msg)
                    msg = ''
                    break
            conn.close()
        except KeyboardInterrupt:
            conn.close()
            server.close()
            break

if __name__ == '__main__':
    try:
        server()
    except KeyboardInterrupt:
        pass
