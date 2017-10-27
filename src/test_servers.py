"""Test functionality between server and client."""

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
def test_okay_response_message():
    """Manually test ok message output."""
    from server import response_ok
    ok_message = response_ok()
    assert ok_message[5:20] == 'HTTP/1.1 200 OK'


def test_error_response_message():
    """Manually test error message output."""
    from server import response_error
    error_message = response_error()
    assert error_message[5:39] == 'HTTP/1.1 500 INTERNAL SERVER ERROR'


def test_client_receives_ok_response():
    """Test the server sends okay message back."""
    from server import response_ok
    from client import client_socket
    message_return = client_socket('message')
    ok_message = response_ok()
    assert message_return[5:20] == 'HTTP/1.1 200 OK'
