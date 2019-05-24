import random

from typing import Tuple

from euclid import euclid
from rsa.key_generator.public_key import PublicKey
from rsa.key_generator.private_key import PrivateKey


class KeyGenerator(object):

    @staticmethod
    def generate() -> Tuple[PrivateKey, PublicKey]:
        z = random.choice([(9999999967, 9999999943), (999979, 999983), (991, 997)])
        p, q = z[0], z[1]
        print(p, q)
        n = p * q
        euler_func = (p - 1) * (q - 1)

        e = 13   # Ferma numbers
        gcd, u, v = euclid.extend_euclid(e, euler_func)
        d = u

        while d < 0:
            d += n

        private_key = PrivateKey(d, n)
        public_key = PublicKey(e, n)

        return private_key, public_key


if __name__ == "__main__":
    key_generator = KeyGenerator()
    priv_key, pub_key = key_generator.generate()
    print(priv_key)
    print(pub_key)
