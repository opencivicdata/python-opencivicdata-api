import requests
from .result import OCDListResult, OCDDictResult


class Service(object):
    """
    Helper methods for a given API Implementation.
    """

    def setup(self, apikey=None, host=None):
        """
        Configure the Service object's bits.

        The reason this isn't in a constructor is that we can
        continue to reload/change config during runtime without
        trying to manually invoke the superclass constructor.
        As such, we're explicitly exposing a setup method to
        configure the API Key and API Host.
        """
        self.apikey = apikey if apikey else self._get_apikey()
        self.host = host

        if host is None:
            raise ValueError("Bad Host!")

    def get_url(self, host, *args):
        """
        Construct the URL to query.
        """
        return "{}/{}/".format(
            host,
            "/".join(args)
        )

    def _query(self, method, *args, handler=dict, **kwargs):
        """
        Query the API given a path (*args), with params (**kwargs).

        The JSON result will be passed directly into handler
        and returned. This allows for things like ``OCDListResult``
        or ``OCDDictResult`` to take control of the response.
        """

        params = kwargs
        kwargs['apikey'] = self.apikey

        return handler(
            requests.request(
                method,
                self.get_url(
                    self.host,
                    *args
            ), params=params).json()
        )

    def _get_apikey(self):
        """
        Look up the OCD API Key
        """
        pass
