import urllib.parse
import urllib.request
from src.settings import BASE_URI


class Client(object):
    def __init__(self, config_obj, **kwargs):
        self.headers = {
            'User-agent': config_obj.user_agent,
            'Authorization': "Bearer {}".format(config_obj.access_token)
            }

    def make_request(self, uri_extension, data=None, **kwargs):
        uri = "{}{}".format(BASE_URI, uri_extension)
        if data:
            data = urllib.parse.urlencode(data)
            data = data.encode('utf-8')
        request = urllib.request.Request(url=uri, data=data, headers=self.headers, method='GET')
        with urllib.request.urlopen(request) as response:
            return response.read().decode('utf-8')
