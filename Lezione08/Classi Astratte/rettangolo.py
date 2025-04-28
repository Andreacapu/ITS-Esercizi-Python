from formagenerica import FormaGenerica

class Rettangolo(FormaGenerica):

    def __init__(self):
        super().__init__()

        self.setShape("rettangolo")
    
    def draw(self) -> None:
        print(f"\n{self.getShape()}\n")

        #outer for

        for i in range(5):

            #inner for
            for j in range(5*2):

                #lato a 3 lato b rettangolo
                if i == 0 or i == 5-1:
                    print("*", end=" ")
                #lato c e lato d del rettangolo
                elif j == 0 or j ==(5*2)-1:
                    print("*", end=" ")
                #stampare spazi bianchi
                else:
                    print(" ", end = " ")

            print("\n", end = "")