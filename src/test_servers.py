
def test_shorter():
    """Test for shorter than buffer length msg is echo back."""
    from client import client_socket
    msg = client_socket('12345')
    assert msg == '12345*'


def test_longer():
    """Test for longer than buffer length msg is echoed back."""
    from client import client_socket
    msg = client_socket('12345678910')
    assert msg == '12345678910*'


def test_exact():
    """Test for exact buffer length msg is echoed back."""
    from client import client_socket
    msg = client_socket('12345678')
    assert msg == '12345678*'

