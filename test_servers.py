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



# It's still looking at the tests you have commented out for your echo step
# ----------------------------------------------------------
#  SyntaxError: Non-ASCII character '\xc3' in file /Users/bonana/401TA/adrienne_karnoski/http-server/src/test_servers.py on line 39, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
# ------------------------------------------------------------
# When I comment it out it's will run your tests with pytest, but your tests are not passing completely.