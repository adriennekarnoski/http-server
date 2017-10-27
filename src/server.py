"""."""
import socket
import email.utils
import sys


def server():
    """Function for the server."""
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )
    server.bind(('127.0.0.1', 2100))
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
                    message_return = response_ok()
                    conn.send(message_return.encode('utf8'))
                    logged_request = """
                    INCOMING REQUEST\r\n
                    REQUEST BODY: {}\r\n
                    FROM: {}\r\n
                    DATE: {}\r\n
                    """.format(msg, addr, email.utils.formatdate(usegmt=True))
                    sys.stdout.write(logged_request)
                    msg = ''
                    break
            conn.close()
        except IndexError:
            error_message = response_error()
            conn.send(error_message.encode('utf8'))
        except KeyboardInterrupt:
            conn.close()
            server.close()
            break


def response_ok():
    """Response function return 200 OK message."""
    send_ok_response = """
    HTTP/1.1 200 OK \r\n
    DATE: {} \r\n
    """.format(email.utils.formatdate(usegmt=True))
    message = u'{}*'.format(send_ok_response)
    return message


def response_error():
    """Response function returns error message."""
    send_error_response = """
    HTTP/1.1 500 INTERNAL SERVER ERROR<CRLF>
     DATE: {} \r\n
    """.format(email.utils.formatdate(usegmt=True))
    message = u'{}*'.format(send_error_response)
    return message


if __name__ == '__main__':
    try:
        server()
    except KeyboardInterrupt:
        pass
