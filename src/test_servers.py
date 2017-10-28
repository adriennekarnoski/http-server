"""Testing server response to requests."""


def test_response_message_response():
    """Test if ok message can be formed."""
    from server import response_ok
    ok_message = response_ok()
    assert ok_message[5:20] == 'HTTP/1.1 200 OK'


def test_error_message_response():
    """Test if error message can be formed."""
    from server import response_error
    error_message = response_error()
    assert error_message[5:39] == 'HTTP/1.1 500 INTERNAL SERVER ERROR'


def test_client_response():
    """Test if a ok response can be send back."""
    from server import response_ok
    from client import client_socket
    returned = client_socket('message testing')
    ok_message = response_ok()
    assert returned == ok_message
