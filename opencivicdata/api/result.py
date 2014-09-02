"""
This module contains a bunch of simple wrappers for the top level
datastructure returned by the API.

We get a small amount of meta-data back, so storing that without
getting in the way of the response is important.
"""

import functools
import operator


class OCDDebugMixIn(object):
    def print_debug(self):
        debug = self.debug

        connection = debug['connection']
        queries = connection['query']['list']

        print("Made %s queries" % (connection['query']['count']))
        print("")
        print("Total SQL Query time:")

        ql = connection['query']['list']
        print(functools.reduce(operator.add,
                               [float(x['time']) for x in ql]),
              "second(s)")

        print("")
        print("Sorted by time:")
        print("")
        for query in sorted(queries, reverse=True, key=lambda x: float(x['time'])):
            sql = query['sql']
            if len(sql) >= 80:
                sql = sql[:80] + "..."
            print("  %s:   %s" % (query['time'], sql))
        print("")
        print("Prefetched Fields:")
        for field in debug['prefetch_fields']:
            print("  %s" % (field))


class OCDListResult(list, OCDDebugMixIn):
    """
    This is a simple list subclass that contains two extra
    attributes -- ``debug`` and ``meta``.

    ``meta`` is a dictinary containing information regarding
    pagination of data and object counts.

    ``debug`` is a dictinary that's used for debugging the
    API software, and can be regarded as a public facing
    implementation detail. Please don't rely on this.
    """

    def __init__(self, response, next_=None):
        results = response.pop('results')
        meta = response.pop('meta', {})
        debug = response.pop('debug', {})

        self.next_ = next_
        self.meta = meta
        self.debug = debug

        super(OCDListResult, self).__init__(results)

    def has_next(self):
        return self.meta['max_page'] > self.meta['page']

    def next(self):
        if self.has_next() and self.next_:
            return self.next_()



class OCDDictResult(dict, OCDDebugMixIn):
    """
    This is a simple dict subclass that contains an additional
    attribute -- ``debug``. ``debug`` allows you to access
    the API's debug-mode output in a standard way.
    """

    def __init__(self, response):
        debug = response.pop('debug', {})
        self.debug = debug
        super(OCDDictResult, self).__init__(response)
