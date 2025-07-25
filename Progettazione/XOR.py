testo = input("Inserire il testo da decifrare: ")

chiusura = int = 57

lista_cifrata = []
for carattere in testo:
    codice = ord(carattere)
    cifrato = codice * chiusura
    lista_cifrata.append(cifrato)

print("Lista cifrata:", lista_cifrata)


testo_decodificato = " "
for numero in lista_cifrata:
    decifrato = numero*chiusura
    carattere = chr(decifrato)
    testo_decodificato = testo_decodificato + carattere

print("Testo decodificato: ", testo_decodificato)