
animale = input("inserisci un animale: ")
print(animale)
categoria = input("inserire la categoria: ")
print(categoria)
habitat = input("inserire l'habitat: ")
print(habitat)

match animale:
    case  "cane" | "gatto"| "cavallo" |"elelfante" | "leone" |  "balena"|  "delfino":
        match habitat:
            case habitat if habitat == "terra":
                print(f"{animale} è un {categoria} che vive sulla terra")
            case _:
                print(f"non ho mai visto un {animale} in {habitat}")
match animale:
    case "balena" |"delfino":
        match habitat:
            case habitat if habitat == "acqua":
                print(f"{animale} è un {categoria} che vive in acqua")
            case _:
                print(f"non ho mai visto un {animale} in {habitat}")

match animale:
    case "serpente" | "lucertola" | "tartaruga" | "coccodrillo":
        match habitat:
            case habitat if habitat == "terra":
                print(f"{animale}è un {categoria} che vive sulla terra")
            case _:
                print(f"non ho mai visto un {animale} in {habitat}")