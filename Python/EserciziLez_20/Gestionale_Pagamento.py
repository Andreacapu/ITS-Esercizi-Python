class Pagamento:
    def __init__(self):
        self.__importo = 0

    def setImporto(self, importo:float):
         self.__importo = importo
    def getImporto(self)-> float:
        return self.__importo
    
    def dettagliPagamento(self)->None:
        # Formatto l'importo con 2 cifre decimali
        print(f"Importo del pagamento: €{self.__importo:.2f}")

class PagamentoContanti(Pagamento):

    def DettagliPagamento(self):
         print(f"Importo del pagamento in contanti: €{self.get():.2f}")

    def inPezziDa(self):
        importo = self.get()
        rimanente = importo

        tagli = [1, 2, 5, 10, 20, 50, 100, 200, 500, 0.5, 0.1, 0.05, 0.02, 0.01]

        for taglio in tagli:
            quantità = int(rimanente // taglio)
            rimanente = round(rimanente - quantità * taglio,2)
        
        if quantità>0:
            tipo = 'banconota' if taglio >= 5 else 'moneta'
            print(f"  {quantita} {tipo}/e da €{taglio:.2f}")

class PagamentoCartaDiCredito(Pagamento):
    
