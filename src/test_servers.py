"""Test functionality between server and client."""

from server import response_error
from client import client_socket
from server import response_ok
from server import parse_request
import pytest

# echo tests tests


# def test_message_is_sent_from_client():
#     """Test the client sends messages."""
#     from client import client_socket
#     message_sent = client_socket('message')
#     assert message_sent


# def test_message_shorter_than_buffer_length():
#     """Test the client message return when message is shorter than buffer."""
#     from client import client_socket
#     message_sent = client_socket('short')
#     assert len(message_sent) == len('short')


# def test_message_longer_than_buffer_length():
#     """Test the client message return when message is longer than buffer."""
#     from client import client_socket
#     message = 'This is a message that is longer than buffer length'
#     message_sent = client_socket(message)
#     assert len(message_sent) == len(message)


# def test_message_same_as_buffer_length():
#     """Test the client message return when message is longer than buffer."""
#     from client import client_socket
#     message_sent = client_socket('12345678')
#     assert len(message_sent) == 8


# def test_message_with_non_ascii_characters():
#     """Test message can be sent and returned with non-ascii characters."""
#     from client import client_socket
#     message_sent = client_socket('ààààààààà')
#     assert message_sent == 'ààààààààà'


# step1 tests


# def test_okay_response_message():
#     """Manually test ok message output."""
#     from server import response_ok
#     ok_message = response_ok()
#     assert ok_message[5:20] == 'HTTP/1.1 200 OK'


# def test_error_response_message():
#     """Manually test error message output."""
#     from server import response_error
#     error_message = response_error()
#     assert error_message[5:39] == 'HTTP/1.1 500 INTERNAL SERVER ERROR'


# def test_client_receives_ok_response():
#     """Test the server sends okay message back."""
#     from server import response_ok
#     from client import client_socket
#     message_return = client_socket('message')
#     ok_message = response_ok()
#     assert message_return[5:20] == 'HTTP/1.1 200 OK'


# step2 tests


# def test_response_message_response():
#     """Testing for ok msg function."""
#     ok_message = response_ok('/URI')
#     assert ok_message[5:20] == 'HTTP/1.1 200 OK'


# def test_okay_response_message():
#     """Manually test ok message output."""
#     from server import response_ok
#     ok_message = response_ok()
#     assert ok_message[5:20] == 'HTTP/1.1 200 OK'


# def test_error_response_message():
#     """Manually test error message output."""
#     from server import response_error
#     error_message = response_error()
#     assert error_message[5:39] == 'HTTP/1.1 500 INTERNAL SERVER ERROR'


# def test_client_receives_ok_response():
#     """Test the server sends okay message back."""
#     from server import response_ok
#     from client import client_socket
#     message_return = client_socket('message')
#     ok_message = response_ok()
#     assert message_return[5:20] == 'HTTP/1.1 200 OK'


# step3 tests


def test_response_message_response():
    """Test function returns file type and size."""
    from server import response_ok
    ok_message = response_ok('sample.txt')
    assert ok_message[5:20] == 'HTTP/1.1 200 OK'


def test_405_error_message_response():
    """Testing for if 405 error is triggered."""
    returned = client_socket('POST /URI HTTP/1.1')
    error_message = response_error('405')
    assert returned == error_message


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
