n = int(input("inserire un numero :"))

if n > 0 and n <= 100:
        sum_pari = 0
        for i in range(1,n +1):#messo per fare la somma fra tutti i numeri pari fino ad n
            if i%2 == 0:
                sum_pari += i
            print(f"il risultato è : {sum_pari}")

elif n == 0 or n < 0:
     sum_dispari = 0
     for i in range(1, abs(n) + 1):#messo per fare la somma fra tutti i numeri dispari fino ad n
            if i > n:
                sum_dispari +=i
            print(f"il risultato è: {sum_dispari}")