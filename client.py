"""Client socket function."""


import socket
import sys


def client_socket(message):
    """Function to send messages to client."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 4000))
    message = u'{}'.format(message)
    client.sendall(message.encode('utf8'))
    buffer_length = 1024
    reply_complete = False
    while not reply_complete:
        part = client.recv(buffer_length)
        print(part.decode('utf8'))
        if len(part) < buffer_length:
            break
    client.close()

if __name__ == '__main__':
    client_socket(sys.argv[1])



