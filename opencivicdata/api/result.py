

class OCDListResult(list):
    """
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
    """

    def __init__(self, response):
        debug = response.pop('debug', {})
        self.debug = debug
        super(OCDDictResult, self).__init__(response)
