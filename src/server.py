"""Server function."""
import email.utils
import sys
import os
from gevent.server import StreamServer


def response_error(error_code):
    """Determine and format proper response."""
    if error_code == '405':
        error_msg = 'METHOD NOT ALLOWED'
    elif error_code == '505':
        error_msg = 'HTTP VERSION NOT SUPPORTED'
    elif error_code == '500':
        error_msg = 'INTERNAL SERVER ERROR'
    elif error_code == '404':
        error_msg = 'CONTENT NOT FOUND'
    send_error_response = """
    HTTP/1.1 {}\r\n
     DATE: {}\r\n
     ERROR: {}\r\n
    """.format(error_code, email.utils.formatdate(usegmt=True), error_msg)

    message = u'{}*'.format(send_error_response)
    return message


def parse_request(msg):
    """Parse the incoming msg to check for proper format, raise appropriate exception."""
    request = msg.split(' ')

    if request[0] == 'CRASH':
        raise ValueError('500')
    elif request[0] == 'GET' and request[2] == 'HTTP/1.1':
        uri = request[1]
        try:
            message_return = resolve_uri(uri)
        except IndexError:
            raise ValueError('404')
        return [message_return, request]
    elif request[0] != 'GET':
        raise ValueError('405')
    elif request[2] != 'HTTP/1.1':
        raise ValueError('505')


def resolve_uri(uri):
    """Open proper file from request in our database or raise errors."""
    os.chdir('..')
    os.chdir('web_home_directory')
    if uri.endswith('/'):
        if not os.path.isdir(uri):
            raise IndexError
        else:
            html_list = [s for s in os.listdir(uri) if s.endswith('.jpg')]
            print(html_list)
            result = response_ok(('HTML LISTINGS', html_list))
            return result
    else:
        if not os.path.exists(uri):
            raise IndexError
        else:
            uri_list = uri.split('/')
            if len(uri_list) > 1:
                uri_dir = '/'.join(uri_list[:-1])
                os.chdir(uri_dir)
                uri_file = uri_list[-1]
            elif len(uri_list) == 1:
                uri_file = uri
            txt = ''
            with open(uri_file, 'r') as f:
                txt = f.read()
            result = response_ok(('FILE CONTENT', txt))
            return result


def handle_conn(conn, addr):
    """Handle incoming request."""
    buffer_len = 8
    msg = ''
    while True:
        data = (conn.recv(buffer_len)).decode('utf8')
        msg += data

        if data.endswith('*'):
            try:
                message_return = parse_request(msg)[0]
            except ValueError as err:
                message_return = response_error(err.args[0])
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


def server():
    """Create the stream server."""
    try:
        stream = StreamServer(('127.0.0.1', 3000), handle_conn)
        stream.serve_forever()
    except KeyboardInterrupt:
        pass


def response_ok(uri):
    """Send the 200 ok msg if called."""
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
