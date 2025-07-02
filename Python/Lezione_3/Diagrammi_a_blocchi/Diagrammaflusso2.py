numero_maggiore:float = float(input("inserire quattro numeri: "))

for numero_maggiore in range (3):
      n= float(input("inserisci un numero: "))
      if n > numero_maggiore:
        numero_maggiore = n
      print (f"il numero maggiore della sequenza è {numero_maggiore}")