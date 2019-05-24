from euclid import euclid
from rsa.crypt.crypt import Crypt
from rsa.key_generator.key_generator import KeyGenerator
from rsa.power import power

alice_text = "hello. I like jilly"

alice_bytes = bytes(alice_text, encoding='utf-8')
alice_bytes = [int(byte) for byte in alice_bytes]
print(f"Alice bytes: {alice_bytes}")

# Create keys
# alice_priv_key, alice_pub_key = KeyGenerator.generate()
bob_priv_key, bob_pub_key = KeyGenerator.generate()
print(f"Bob priv key: {bob_priv_key}")
print(f"Bob pub key: {bob_pub_key}")

# Crypt message by alice
bob_crypter = Crypt(bob_pub_key)
crypted_alice_bytes = bob_crypter.crypt(alice_bytes)
print(f"Crypted alice bytes: {crypted_alice_bytes}")


# Start hacking
# Have: m ^ e -> c, where e - public Bob's exponent

# Hacker side
r = [10] * len(alice_bytes)
x = []
for ri in r:
    x.append(
        power.power_by_mod(ri, bob_pub_key.e, bob_pub_key.n)
    )
print(f"R: {r}")

y = []
for ind in range(len(crypted_alice_bytes)):
    y.append(
        (x[ind] * crypted_alice_bytes[ind]) % bob_pub_key.n
    )
print(f"Y: {y}")

t = []
for ri in r:
    gcd, u, v = euclid.extend_euclid(ri, bob_pub_key.n)
    t.append(u)
print(f"T: {t}")

# Bob side
# Create digital signature
u = []
for yi in y:
    u.append(
        power.power_by_mod(yi, bob_priv_key.d, bob_priv_key.n)
    )

# Hacker side
res_bytes = []
for ind in range(len(u)):
    res_bytes.append(
        (t[ind] * u[ind]) % bob_pub_key.n
    )
print(f"Result bytes: {res_bytes}")
