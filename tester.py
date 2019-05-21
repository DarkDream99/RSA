from rsa.crypt.crypt import Crypt
from rsa.decrypt.decrypt import Decrypt
from rsa.key_generator.key_generator import KeyGenerator

read_bytes = []

with open("files/input.txt", 'rb') as fin:
    for byte in fin:
        read_bytes.append(byte)

    read_bytes = b''.join(read_bytes)

dec_bytes = []
for byte in read_bytes:
    dec_bytes.append(int(byte))
print(read_bytes)
print(dec_bytes)


key_generator = KeyGenerator()
priv_key, pub_key = key_generator.generate()
crypter = Crypt(pub_key)
crypted_bytes = crypter.crypt(dec_bytes)
print(crypted_bytes)


decrypter = Decrypt(priv_key)
print(decrypter.decrypt(crypted_bytes))
