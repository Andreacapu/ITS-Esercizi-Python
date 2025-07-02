adenina = "A"
citosina = "C"
guanina = "G"
timinia = "T"
def isDNA():
    stringa1 = input("Inserire la prima sequenza: ").upper()
    stringa2 = input("Inserire la seconda sequenza: ").upper()
    nucleotidi_validi = {"A","C","G","T"}
    if all (c in nucleotidi_validi for c in stringa1) and all(c in nucleotidi_validi for c in stringa2):
        return True, stringa1, stringa2
    else:
        return False, None, None

valido, sequenza1, sequenza2 = isDNA

if valido:
    DNA = {"sequenza1": sequenza1, "sequenza2": sequenza2}
    print("Sequenza valida")
    print("Ecco la sequenza:",DNA)
else:
    print("Sequenza invalida")