import pytest


def test_shorter():
    """."""
    from client import client_socket
    msg = client_socket('12345')
    assert msg == '12345'


def test_longer():
    """."""
    from client import client_socket
    msg = client_socket('12345678910')
    assert msg == '12345678\910'


def test_exact():
    """."""
    from client import client_socket
    msg = client_socket('12345678')
    assert msg == '12345678'

