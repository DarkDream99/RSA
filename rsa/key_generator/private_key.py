class PrivateKey(object):

    def __init__(self, d):
        self._d = d

    @property
    def d(self):
        return self._d
