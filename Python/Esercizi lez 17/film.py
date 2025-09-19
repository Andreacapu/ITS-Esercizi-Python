class Film:
    def __init__(self, id:int, title:str):
        if not isinstance(id, int):
            id = None
            print("ID deve essere un numero intero")
        if not isinstance(title, str):
            title = None
            print("Il titolo deve essere una stringa")
        if isinstance (id, int) and isinstance(title, str):
            self.id = id
            self.title = title
    def setID(self, id):
        if not isinstance(id,int):
            id = None
            print("ID deve essere un numero intero")
        else:
            self.id = id
    
    def setTitle(self, title):
        if not isinstance(title, str):
            title = None
            print("Il titolo deve essere una stringa")
        else:
            self.title = title
    
    def getID(self)-> int:
        return self.id
    def getTitle(self):
        return self.title
    
    def isEqual(self, otherFilm)->bool:
        if not isinstance(otherFilm, Film):
            return False
        if self.id is None or otherFilm is None:
            return False
        
        return self.id == otherFilm.id