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

    def __str__(self):
        return f"RSA Private Key:" \
               f"\n\td: {self.d}" \
               f"\n\tn: {self.n}"

