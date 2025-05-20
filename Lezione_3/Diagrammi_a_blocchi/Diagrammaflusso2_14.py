punteggio = 0
D_1 = int(input("Inserire il valore di D1: "))
D_2 = int(input("Inserire il valore di D2: "))

if (D_1 > 0 and D_1 <=6) and (D_2 > 0 and D_2 <= 6):
   sum = D_1 + D_2

if D_1%2 == 0 and D_2%2 == 0 and sum > 8:
   punteggio = 100

elif 