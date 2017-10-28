"""Testing server response to requests."""
from server import response_error
from client import client_socket
from server import response_ok
from server import parse_request


def test_response_message_response():
    """Testing for ok msg function."""
    ok_message = response_ok((1, 2, 3))
    assert ok_message[:15] == 'HTTP/1.1 200 OK'


def test_405_error_message_response():
    """Testing for if 405 error is triggered."""
    returned = client_socket('POST /URI HTTP/1.1 Host:')
    error_message = response_error('405')
    assert returned == error_message


def test_404_message_response():
    """Testing for if 200 ok is triggered."""
    returned = client_socket('GET /URI HTTP/1.1 Host:')
    error_message = response_error('404')
    assert returned == error_message


def test_505_error_message_response():
    """Testing if 505 error is triggered."""
    returned = client_socket('GET /URI HTTP/1.2 Host:')
    error_message = response_error('505')
    assert returned == error_message


def test_400_error_message_respoonse():
    """Testing if 500 error is triggered."""
    returned = client_socket('GET /URI HTTP/1.1 HO')
    error_message = response_error('400')
    assert returned == error_message


def test_parse_no_get_req():
    """Test parse function returns proper error."""
    try:
        parse_request('POST /URI HTTP/1.1 Host:')
    except ValueError:
        pass


def test_parse_no_httpver_req():
    """Test parse function returns proper error."""
    try:
        parse_request('GET /URI HTTP Host:')
    except ValueError:
        pass


def test_parse_no_host_req():
    """Test parse function returns proper error."""
    try:
        parse_request('GET /URI HTTP/1.1')
    except ValueError:
        pass


def test_file_request():
    """Test if a valid request for file gets return properly."""
    txt = 'This is a very simple text file. Just to show that we can serve it up. It is three lines long.'
    returned = client_socket('GET sample.txt HTTP/1.1 Host:')
    ok_message = response_ok((txt, 95, '.txt'))
    assert returned[:50] == ok_message[:50]


def test_dir_request():
    """Test if a valid request for a dir gets return a proper HTML listing."""
    listing = ['JPEG_example.jpg', 'Sample_Scene_Balls.jpg', 'sample_1.png']
    returned = client_socket('GET images/ HTTP/1.1 Host:')
    ok_message = response_ok((listing, 3, 'HTML LISTING'))
    assert returned == ok_message
