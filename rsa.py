from math import gcd
from random import randint
# Programa para gerar chaves rsa

p = 2
q = 7

n = p * q
t = (p-1)*(q-1)

# Achar "e" e "q" tal que (e*q) mod t = 1
# "e" precisa ser menor que t e precisa ser coprimo com t e n
e = -1
d = -1

e_candidates = []
for i in range(2, t):
    if (gcd(t,i) == 1 and gcd(n,i) == 1):
        e_candidates.append(i)

e_index = randint(0, len(e_candidates) - 1)
d_candidates = []
for i in range(1, 20):
    if ((i * e_candidates[e_index]) % t == 1):
        d_candidates.append(i)

d_index = randint(0, len(d_candidates) - 1)

public_key = (e_candidates[e_index], n)
private_key = (d_candidates[d_index], n)

print(f"public_key = {public_key}, private_key = {private_key}")
