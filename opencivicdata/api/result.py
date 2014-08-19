"""
This module contains a bunch of simple wrappers for the top level
datastructure returned by the API.

We get a small amount of meta-data back, so storing that without
getting in the way of the response is important.
"""


class OCDListResult(list):
    """
    This is a simple list subclass that contains two extra
    attributes -- ``debug`` and ``meta``.

    ``meta`` is a dictinary containing information regarding
    pagination of data and object counts.

    ``debug`` is a dictinary that's used for debugging the
    API software, and can be regarded as a public facing
    implementation detail. Please don't rely on this.
    """

    def __init__(self, response):
        results = response.pop('results')
        meta = response.pop('meta', {})
        debug = response.pop('debug', {})

        self.meta = meta
        self.debug = debug

        super(OCDListResult, self).__init__(results)


class OCDDictResult(dict):
    """
    This is a simple dict subclass that contains an additional
    attribute -- ``debug``. ``debug`` allows you to access
    the API's debug-mode output in a standard way.
    """

    def __init__(self, response):
        debug = response.pop('debug', {})
        self.debug = debug
        super(OCDDictResult, self).__init__(response)
