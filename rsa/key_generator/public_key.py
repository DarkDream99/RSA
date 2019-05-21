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

    def __str__(self):
        return f"RSA Public Key:" \
               f"\n\te: {self.e}" \
               f"\n\tn: {self.n}"
