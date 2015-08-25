class Config(object):
    def __init__(self, access_token, user_agent, **kwargs):
        self.access_token = access_token
        self.user_agent = user_agent
        self.response_format = 'json'
