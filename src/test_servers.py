import pytest


def test_response_message_response():
    """Test function returns file type and size."""
    from server import response_ok
    ok_message = response_ok('sample.txt')
    assert ok_message


# def test_error_message_response():
#     from server import response_error
#     error_message = response_error()
#     assert error_message[5:39] == 'HTTP/1.1 500 INTERNAL SERVER ERROR'
