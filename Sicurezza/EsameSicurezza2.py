'''Crittografia
Sia dato il messaggio cifrato (convertito in numero intero in base 10): 
204751668535
Il messaggio cifrato è stato ottenuto cifrando il messaggio originale con algoritmo RSA senza padding con n=514948966453 e esponente pubblico (e) pari a 3
Provare a decifrare il messaggio cifrato
NB: il messaggio originale è una parola di cinque lettere maiuscole e minuscole.
NB: Quando il problema sembra arduo, allora un approccio brutale potrebbe essere quello vincente.'''
import random, math

n = 51151902024533551
e = 3
c = 10002041662569686

#inizializzo una funzione al fine di trovare i fattori di "n"
def q_p(n):
    if n % 2 == 0:
        return 2
    while True:
        x = random.randrange(2, n-1)
        y = x
        cst = random.randrange(1, n-1)   
        d = 1
        while d == 1:
            x = (x*x + cst) % n
            y = (y*y + cst) % n
            y = (y*y + cst) % n
            d = math.gcd(abs(x-y), n)
        if d != n:
            return d

# ora possiamo trovare i fattori primi di Q e P
p = q_p(n) 
q = n // p
if p > q:
    p, q = q, p

#Dopo aver trovato i fattori di "n", possiamo fare i calcoli per l'RSA
phi = (p-1)*(q-1) #Calcolo per l'inversione del modulo
d = pow(e, -1, phi)# renderizzazione del messaggio
m = pow(c, d, n)

# ora decodificiamo il testo in asci, e convertendo i bytes
testo_decifrato = m.to_bytes((m.bit_length()+7)//8, 'big').decode('ascii')

#stampa finale dei valori e del messaggio decifrato ora
print("p =", p)
print("q =", q)
print("phi =", phi)
print("d =", d)
print("m =", m)
print("testo decifrato =", testo_decifrato)
