import urllib
import urllib.parse
import urllib.request
import json

BASE_URI = 'https://erikberg.com'


class Client(object):
    def __init__(self, access_token, user_agent, **kwargs):
        self.headers = {
            'User-agent': user_agent,
            'Authorization': "Bearer {}".format(access_token)
            }

    def make_request(self, uri_extension, data=None, **kwargs):
        full_url = "{}{}.json".format(BASE_URI, uri_extension)
        if data:
            data = urllib.parse.urlencode(data)
            full_url = full_url + '?' + data
        request = urllib.request.Request(url=full_url, headers=self.headers, method='GET')
        with urllib.request.urlopen(request) as response:
            return json.loads(response.read().decode('utf-8'))
