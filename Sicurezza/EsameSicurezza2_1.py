import random
import math

# area dati
n = 514_948_966_453
e = 3
c = 204_751_668_535

def is_prime(n: int) -> bool:
#ricerca primarietà se probabilemte primo ritorna True, altrimenti false

    if n < 2:
        return False
    ricerca = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in ricerca:
        if n % p == 0:
            return n == p

    # decomposizione n-1 = 2^s * d
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    # basi affidabili per valori up to 64-bit-ish
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
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

def trova_fattore(n: int) -> int:
   #ricerca fattoriale non banale
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    while True:
        const = random.randrange(1, n - 1)# troviamo il coefficiente costante non nullo
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

def fattori(n: int) -> list:
#test di primarietà
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    d = trova_fattore(n)
    return fattori(d) + fattori(n // d)

# esecuzione calcoli per trovare i fattori
f = sorted(fattori(n))
print("Fattori individuati:", f)
p, q = f

# calcolo del phi
phi = (p - 1) * (q - 1)

# calcolo della chiave privata d, usando pow per l'inverso modulare (Python 3.8+)
d = pow(e, -1, phi)
print("d =", d)

# Decifratura del messaggio mediante l'uso dell'esponente privato, ossia m = c^d mod n.
# in questo modo ci ritorna la versione numerica del messaggio
m = pow(c, d, n)
print("Messaggio numerico:", m)

# Conversione del messaggio, siccome la traccia indica che il messiggio è lungo 5 caratteri, ergo 5 bytes,
# trasformo quindi l'intero in una sequenza di bytes. Infine, usando .decode, rendiamo la stringa leggibile
Messaggio = m.to_bytes(5, "big").decode("ascii")

# stampa finale del messaggio, oramai decifrato
print("Messaggio Decifrato:", Messaggio)


