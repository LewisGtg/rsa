from sympy import mod_inverse, isprime
import math
import sys

def factorize_n(n):
    # Procurar fatores de n
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            p = i
            q = n // i
            if isprime(p) and isprime(q):
                return p, q
    return None, None

def find_private_key(e, n):
    # Fatorar n para encontrar p e q
    p, q = factorize_n(n)
    if p is None or q is None:
        raise ValueError("Não foi possível fatorar n para obter p e q.")

    phi_n = (p - 1) * (q - 1)

    d = mod_inverse(e, phi_n)
    return d

if (len(sys.argv) < 4):
    print("Usage: python3 main.py <file_path> <e> <n>")
    exit()

e = int(sys.argv[2])
n = int(sys.argv[3])

print(f"Procurando chave privada para e = {e} e n = {n}")

try:
    d = find_private_key(e, n)
    print(f"Chave privada encontrada PR = ({d}, {n})")
except ValueError as ve:
    print(ve)