#settaggio condizioni
reddito = int(input("inserire reddito: "))
media = int(input("inserire media: "))

#settaggio match statement (il "_" serve a fare il match con ogni valore, con l'if che si attiva solo se la condione sia vera)
match reddito:
        case _ if reddito < 20000:
            match media:
                case _ if media > 27:
                    print("borsa di studio assegnata")
                case _:
                      print("borsa di studio non assegnata: media inferiore e/o reddito elevato")
