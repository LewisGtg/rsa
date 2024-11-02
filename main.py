from sympy import mod_inverse, isprime
import math

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

    # Calcular φ(n) = (p - 1) * (q - 1)
    phi_n = (p - 1) * (q - 1)

    # Calcular d como o inverso modular de e mod φ(n)
    d = mod_inverse(e, phi_n)
    return d

# Exemplo de uso
e = 5  # valor comum de e
n = 14   # um exemplo de n pequeno para fins de teste (com primos p=61, q=53)
try:
    d = find_private_key(e, n)
    print("Chave privada d encontrada:", d)
except ValueError as ve:
    print(ve)