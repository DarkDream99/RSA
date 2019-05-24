import time
import math

from rsa.key_generator import key_generator
from euclid import euclid


current_milli_time = lambda: int(round(time.time() * 1000))


start = current_milli_time()
# generate keys
rsa_key_generator = key_generator.KeyGenerator()
priv_key, pub_key = rsa_key_generator.generate()
generate_time = current_milli_time() - start

start = current_milli_time()
# HACK PRIVATE KEY
# factorize module n
factor_a = factor_b = -1
for factor in range(2, round(math.sqrt(pub_key.n))):
    print(f'check factor: {factor}')
    if pub_key.n % factor == 0:
        factor_a = factor
        factor_b = pub_key.n // factor
        break

# euler function
fi_n = (factor_a - 1) * (factor_b - 1)

# calculate d
gcd, u, v = euclid.extend_euclid(pub_key.e, fi_n)
d = u

if d < 0:
    d += pub_key.n

hack_time = current_milli_time() - start

# PRINT RESULTS TO CHECK
print(pub_key)
print(priv_key)

print(f"Hacked value of d: {d}")

print(f"generate_time: {generate_time}")
print(f"hack time: {hack_time}")
