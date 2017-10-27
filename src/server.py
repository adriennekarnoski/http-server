"""Server function."""
import socket
import email.utils
import sys


def response_error(error):
    """Determine and format proper response."""
    send_error_response = """
    HTTP/1.1 {}\r\n
     DATE: {}\r\n
    """
    message = u'{}*'.format(send_error_response)
    if error == 'method':
        error_code = '405 METHOD NOT ALLOWED'
    elif error == 'protocol':
        error_code = '505 HTTP VERSION NOT SUPPORTED'
    elif error == 'server':
        error_code = '500 INTERNAL SERVER ERROR'
    return message.format(error_code, email.utils.formatdate(usegmt=True))


def parse_request(msg):
    """Parse the incoming msg to check for proper format,
    raise appropriate exception."""
    request = msg.split(' ')
    if request[0] == 'CRASH':
        raise IOError
    elif request[0] == 'GET' and request[2] == 'HTTP/1.1':
        message_return = response_ok(request[1])
        return [message_return, request]
    elif request[0] != 'GET':
        raise ValueError
    elif request[2] != 'HTTP/1.1':
        raise ValueError('505')


def resolve_uri(uri):
    """."""
    os.chdir('..')
    os.chdir('web_home_directory')
    if uri.endswith('/'):
        if not os.path.isdir(uri):
            raise IndexError
        else:
            html_list = [s for s in os.listdir(uri) if s.endswith('.jpg')]
            html_count = len(html_list)
            result = response_ok((html_list, html_count, 'HTML LISTING'))
            return result
    else:
        if not os.path.exists(uri):
            raise IndexError
        else:
            # uri_list = uri.split('/')
            # uri_dir = '/'.join(uri_list[:-1])
            extension = os.path.splitext(uri)[1]
            # os.chdir(uri_dir)
            txt = ''
            with open(uri, 'r') as f:
                txt = f.read()
            txt_len = len(txt)
            result = response_ok((txt, txt_len, extension))
            return result

        
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
        except KeyboardInterrupt:
            conn.close()
            server.close()
            break


def response_ok(msg):
    """Send the 200 ok msg if called."""
    send_ok_response = """
HTTP/1.1 200 OK \r\n
FILE TYPE: {type}
FILE LENGTH:{len}
DATE: {date} \r\n
\r\n
BODY: \r\n {body}
\r\n
    """.format(
        date=email.utils.formatdate(usegmt=True),
        type=msg[2],
        len=msg[1],
        body=msg[0]
    )
    message = u'{}*'.format(send_ok_response)
    return message


if __name__ == '__main__':
    try:
        server()
    except KeyboardInterrupt:
        pass
