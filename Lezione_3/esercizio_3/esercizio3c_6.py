animale: str = input("Inserisci un animale: ")
print(animale)
categoria: str = input("Inserire la categoria: ")
print(categoria)
habitat: str = input("Inserire l'habitat: ")
print(habitat)

if animale in ["cane", "gatto", "cavallo", "elefante", "leone"]:
    if habitat == "terra":
        print(f"{animale} è un {categoria} che vive sulla terra")
    else:
        print(f"Non ho mai visto un {animale} in {habitat}")
elif animale in ["balena", "delfino"]:
    if habitat == "acqua":
        print(f"{animale} è un {categoria} che vive in acqua")
    else:
        print(f"Non ho mai visto un {animale} in {habitat}")
elif animale in ["serpente", "lucertola", "tartaruga", "coccodrillo"]:
    if habitat == "terra":
        print(f"{animale} è un {categoria} che vive sulla terra")
    else:
        print(f"Non ho mai visto un {animale} in {habitat}")
else:
    print(f"Non conosco l'animale {animale} o l'habitat {habitat} non è valido.")