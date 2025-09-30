import random, math

n = 514_948_966_453
e = 3
c = 204_751_668_535

def is_prime(n):
    if n < 2:
        return False
    small_primes = [2,3,5,7,11,13,17,19,23,29]
    for p in small_primes:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        composite = True
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                composite = False
                break
        if composite:
            return False
    return True

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    while True:
        const = random.randrange(1, n - 1)
        x = random.randrange(2, n - 1)
        y = x
        d = 1
        while d == 1:
            x = (x * x + const) % n
            y = (y * y + const) % n
            y = (y * y + const) % n
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d

def factor_pollard(n):
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    d = pollards_rho(n)
    return factor_pollard(d) + factor_pollard(n // d)

f = sorted(factor_pollard(n))
p, q = f[0], f[1]
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)
length = max((m.bit_length() + 7) // 8, 5)
m_bytes = m.to_bytes(length, "big")
print("m (intero) =", m)
print("bytes:", m_bytes)
for i, b in enumerate(m_bytes):
    print(f"byte[{i}] = {b} -> {chr(b)} (ASCII {b})")
print("stringa:", m_bytes.decode("ascii"))
