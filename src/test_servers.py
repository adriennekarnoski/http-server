"""Test functionality between server and client."""


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
    from client import client_socket
    message_return = client_socket('message')
    assert message_return[5:20] == 'HTTP/1.1 200 OK'
