from typing import List

from rsa.power import power
from rsa.key_generator.private_key import PrivateKey


class Decrypt(object):

    def __init__(self, private_key: PrivateKey):
        self._private_key = private_key

    def decrypt(self, crypt_dec_bytes: List[int]) -> List[int]:
        decrypt_dec_bytes = []
        for crypt_dec_byte in crypt_dec_bytes:
            decrypt_dec_bytes.append(power.power_by_mod(
                crypt_dec_byte,
                self._private_key.d,
                self._private_key.n
            ))
        return decrypt_dec_bytes
