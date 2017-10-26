"""Testing server response to requests."""
from server import response_error
from client import client_socket
from server import response_ok
from server import parse_request


def test_response_message_response():
    """Testing for ok msg function."""
    ok_message = response_ok('/URI')
    assert ok_message[5:20] == 'HTTP/1.1 200 OK'


def test_405_error_message_response():
    """Testing for if 405 error is triggered."""
    returned = client_socket('POST /URI HTTP/1.1')
    error_message = response_error('405')
    assert returned == error_message


# def test_200_message_response():
#     """Testing for if 200 ok is triggered."""
#     returned = client_socket('GET /URI HTTP/1.1')
#     ok_message = response_ok('/URI')
#     assert returned == ok_message


def test_505_error_message_response():
    """Testing if 505 error is triggered."""
    returned = client_socket('GET /URI HTTP/1.2')
    error_message = response_error('505')
    assert returned == error_message


def test_500_error_message_respoonse():
    """Testing if 500 error is triggered."""
    returned = client_socket('CRASH GET /URI HTTP/1.1')
    error_message = response_error('500')
    assert returned == error_message


def test_parse_no_get_req():
    """Test parse function returns proper error."""
    try:
        parse_request('POST /URI HTTP/1.1')
    except ValueError:
        pass


def test_parse_no_httpver_req():
    """Test parse function returns proper error."""
    try:
        parse_request('GET /URI HTTP')
    except ValueError:
        pass


def test_parse_crash_server_req():
    """Test parse function returns proper error."""
    try:
        parse_request('CRASH GET /URI HTTP/1.1')
    except ValueError:
        pass
