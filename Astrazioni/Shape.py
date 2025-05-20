class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """Calcola l'area della figura"""
        raise NotImplementedError("Metodo astratto - deve essere implementato nelle sottoclassi")
    
    def perimeter(self):
        """Calcola il perimetro della figura"""
        raise NotImplementedError("Metodo astratto - deve essere implementato nelle sottoclassi")
    
    def __str__(self):
        return f"Figura: {self.name}"