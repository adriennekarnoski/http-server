"""Client socket function."""


import socket
import sys


def client_socket(message):
    """Function to send messages to client."""
    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )
    client.connect(('127.0.0.1', 3003))
    message = message + ' *'
    message = u'{}'.format(message)
    client.sendall(message.encode('utf8'))
    buffer_length = 8
    reply_complete = False
    msg = ''
    while not reply_complete:
        part = (client.recv(buffer_length)).decode('utf8')
        msg += part
        if part.endswith('*'):
            print(msg[:-1])
            return msg
    client.close()

if __name__ == '__main__':
    client_socket(sys.argv[1])
