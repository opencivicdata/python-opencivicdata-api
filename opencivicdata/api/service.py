import requests
from .result import OCDListResult, OCDDictResult


class Service(object):
    """
    """

    def setup(self, apikey=None, host=None):
        self.apikey = apikey if apikey else self._get_apikey()
        self.host = host

        if host is None:
            raise ValueError("Bad Host!")

    def get_url(self, host, *args):
        return "{}/{}/".format(
            host,
            "/".join(args)
        )

    def _query(self, *args, handler=dict, **kwargs):
        params = kwargs
        kwargs['apikey'] = self.apikey

        return handler(
            requests.get(self.get_url(
                    self.host,
                    *args
            ), params=params).json())

    def _get_apikey(self):
        pass
