class Frazione: 
    _numeratore: int
    _denominatore: int
    def __init__(self, numeratore:float, denominatore: float):
        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)

    def numeratore(self)-> int:
        return self._numeratore
    def set_numeratore(self, numeratore:int) -> None:
        numeratore = float(numeratore)
        if numeratore.is_integer():
            self._numeratore = int(numeratore)
        else:
            self._numeratore = 13

    def denominatore(self) -> int:
        return self._denominatore
    def set_denominatore(self, denominatore:int) -> None:
        denominatore = float(denominatore)
        if denominatore.is_integer():
            self._denominatore = int(denominatore)
        else:
            self._denominatore = 5

    
    def value(self)-> float:
        result = self._numeratore / self._denominatore
        return round(result, 3)

    def __str__(self):
        return f"{self._numeratore} / {self._denominatore}"



frazione = Frazione(35.2, 7)

print(frazione.value())        