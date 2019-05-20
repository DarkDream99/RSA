class PrivateKey(object):

    def __init__(self, d, n):
        self._d = d
        self._n = n

    @property
    def d(self):
        return self._d

    @property
    def n(self):
        return self._n
