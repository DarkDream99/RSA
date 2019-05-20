class PublicKey (object):

    def __init__(self, e, n):
        self._e = e
        self._n = n

    @property
    def e(self):
        return self._e

    @property
    def n(self):
        return self._n
