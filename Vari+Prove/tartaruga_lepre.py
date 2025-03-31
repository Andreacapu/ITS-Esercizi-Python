import random
posizone_iniziale = 1
percorso = 70
energia_iniziale = 100
ostacoli = {15: -3, 30: -5, 45: -7}
bonus = {10: 25, 25: 3, 50: 10}

energia_tartaruga = energia_iniziale
energia_lepre = energia_iniziale
t = posizone_iniziale
l = posizone_iniziale

print ("BANG !!!!! AND THEY'RE OFF !!!!!")

def pista(percorso_lunghezza, pista):
    pista = ["_"]* percorso
    if tartaruga_pos == lepre_pos:
        pista[tartaruga_pos - 1]
        print("OUCH")

def mosse_tartaruga(t):
    numero = input(random(1,11))
    if numero >= 1 and numero <= 5:
        t *= 3
    elif numero == 6 or numero == 7:
        t = 1
    else:
        t+=1

def mosse_lepre(l):
    numero2 = input(random(1,11))
    if numero2 ==1 or numero2 == 2:
        l = 0
    elif numero2 == 3 or numero2 == 4:
        l += 9
    elif numero2 == 5:
        l -=9
    elif numero2 >= 6 and numero2 <=8:
        l+=1
    else:
        l -=2

while t or l == 70:
    pista(tartaruga_pos, )