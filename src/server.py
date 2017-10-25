"""Server function."""
import socket
import email.utils
import sys


def response_error(error):
    send_error_response = """
    HTTP/1.1 {}\r\n
     DATE: {}\r\n
    """
    message = u'{}*'.format(send_error_response)
    if error == 'method':
        error_code = '405 METHOD NOT ALLOWED'
    elif error == 'protocol':
        error_code = '505 HTTP VERSION NOT SUPPORTED'
    elif error_code == 'server':
        error_code = '500 INTERNAL SERVER ERROR'
    return message.format(error_code, email.utils.formatdate(usegmt=True))


def parse_request(msg):
    request = msg.split(' ')
    message_request = [request[0], request[1], request[2]]
    if request[0] == 'GET' and request[2] == 'HTTP/1.1':
        message_return = response_ok(request[1])
    elif request[0] != 'GET':
        message_return = response_error('method')
    elif request[2] != 'HTTP/1.1':
        message_return = response_error('protocol')
    return [message_return, message_request]


def server():
    """."""
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
                    message_return = parse_request(msg)[0]
                    conn.send(message_return.encode('utf8'))
                    logged_request = """
                    INCOMING REQUEST\r\n
                    REQUEST BODY: {}\r\n
                    FROM: {}\r\n
                    DATE: {}\r\n
                    """.format(
                        msg,
                        addr,
                        email.utils.formatdate(usegmt=True))
                    sys.stdout.write(logged_request)
                    msg = ''
                    break
            conn.close()
        except KeyboardInterrupt:
            conn.close()
            server.close()
            break


def response_ok(uri):
    send_ok_response = """
    HTTP/1.1 200 OK \r\n
    DATE: {} \r\n
    URI: {} \r\n
    """.format(email.utils.formatdate(usegmt=True), uri)
    message = u'{}*'.format(send_ok_response)
    return message


if __name__ == '__main__':
    try:
        server()
    except KeyboardInterrupt:
        pass
