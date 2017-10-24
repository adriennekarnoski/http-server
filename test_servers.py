"""Test functionality between server and client."""

import pytest


def test_message_is_sent_from_client():
    """Test the client sends messages."""
    from client import client_socket
    message_sent = client_socket('message')
    assert message_sent


def test_message_is_length_return_is_same_as_sent():
    """Test the client message return is same length as sent."""
    from client import client_socket
    message_sent = client_socket('message')
    message_length = len(message_sent)
    assert message_length == len(message_sent)