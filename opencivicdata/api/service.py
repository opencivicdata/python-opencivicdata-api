import requests


class Service(object):
    """
    """

    def __init__(self, apikey=None, host=None):
        self.apikey = apikey if apikey else self._get_apikey()
        self.host = host

        if host is None:
            raise ValueError("Bad Host!")


    def _get_apikey(self):
        pass

    def get_url(self, host, *args):
        return "{}/{}/".format(
            host,
            "/".join(args)
        )

    def query(self, *args, **kwargs):
        params = kwargs
        kwargs['apikey'] = self.apikey

        return requests.get(self.get_url(
            self.host,
            *args
        ), params=params).json()
