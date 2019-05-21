from typing import Tuple

from euclid import euclid
from rsa.key_generator.public_key import PublicKey
from rsa.key_generator.private_key import PrivateKey


class KeyGenerator(object):

    def __init__(self):
        p = 999979
        q = 999983
        self._n = p * q
        self._euler_func = (p - 1) * (q - 1)

    def generate(self) -> Tuple[PrivateKey, PublicKey]:
        e = 13   # Ferma numbers
        gcd, u, v = euclid.extend_euclid(e, self._euler_func)
        d = u

        while d < 0:
            d += self._n

        private_key = PrivateKey(d, self._n)
        public_key = PublicKey(e, self._n)

        return private_key, public_key


if __name__ == "__main__":
    key_generator = KeyGenerator()
    priv_key, pub_key = key_generator.generate()
    print(priv_key)
    print(pub_key)
