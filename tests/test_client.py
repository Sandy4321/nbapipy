import os.path
import unittest
from urllib.parse import urlparse

from nbapipy.client import Client


def fake_urlopen(url):
    """
    A stub urlopen() implementation that load json responses from
    the filesystem.
    """
    # Map path from url to a file
    parsed_url = urlparse(url)
    resource_file = os.path.normpath('tests/resources%s' % parsed_url.path)
    # Must return a file-like object
    return open(resource_file, mode='rb')


class ClientTestCase(unittest.TestCase):
    """Test case for the nbapipy methods."""

    def setUp(self):
        self.client = Client(user_agent='raul.emmanuel.gil@gmail.com',
                             access_token='28b20ac0-57f5-41ff-a1c3-12f037ec251e')

    def test_request(self):
        """Test a simple request."""
        user = '/me'
        response = self.client.make_request(user)
        self.assertIn('first_name', response)
        self.assertEqual(response['first_name'], 'Raul')
        self.assertEquals(response['last_name'], 'Gil')

    def test_events(self):
        events = '/events'
        response = self.client.make_request(events, data={'sport': 'nba', 'date': '20130131'})
        for event in response['event']:
            self.assertEquals(event['sport'], 'NBA')
            self.assertNotEquals(event['sport'], 'MLB')
