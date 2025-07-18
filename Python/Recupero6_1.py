def recursivePalindrome(parola):
    parola = parola.replace(" ", "").lower()
    inizio = 0
    fine = len(parola)-1

    while inizio < fine:
        if parola[inizio]!= parola[fine]:
            return False
        
        inizio +=1
        fine -=1
    return True

test_parola = str(input("Digita la parola: "))

if recursivePalindrome(test_parola):
    print(f"{test_parola} è palindorma")
else:
    print(f"{test_parola} non è palindroma")

