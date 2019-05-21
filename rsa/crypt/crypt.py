from typing import List

from rsa.power import power
from rsa.key_generator.public_key import PublicKey


class Crypt(object):

    def __init__(self, public_key: PublicKey):
        self._public_key = public_key

    def crypt(self, dec_bytes: List[int]) -> List[int]:
        crypted_dec_bytes = []
        for dec_byte in dec_bytes:
            crypted_dec_bytes.append(power.power_by_mod(
                dec_byte,
                self._public_key.e,
                self._public_key.n
            ))
        return crypted_dec_bytes

