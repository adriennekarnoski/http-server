"""Client socket function."""


import socket
import sys


def client_socket(message):
    """Function to send messages to client."""
    client = socket.socket(*socket.getaddrinfo('127.0.0.1', 5000)[1][:3])
    client.connect(('127.0.0.1', 5000))
    message = u'{}'.format(message)
    client.sendall(message.encode('utf8'))
    buffer_length = 8
    reply_complete = False
    while not reply_complete:
        part = client.recv(buffer_length)
        print(part.decode('utf8'))
        if len(part) < buffer_length:
            break
    client.close()


if __name__ == '__main__':
    sys.stdout.write(client_socket(sys.argv[1]))