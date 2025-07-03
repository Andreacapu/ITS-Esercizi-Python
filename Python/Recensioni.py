class Media:
    def __init__(self, title:str):
        self.setTitle(title)
        self.reviews = []
    def setTitle(self, title:str):
        self.__title = title
    def getTitle(self, title:str)->str:
        return self.__title
    def setReviews(self, vote:int):
        match vote:
            case 1 | 2| 3 | 4| 5:
                self.reviews.append(vote)
            case _:
                print(f"Errore! {vote} non valido, inserire un voto fra 1 e 5.")
    def getReviews(self, vote:int) -> str:
        match vote:

            case 1: return "Terribile"
            case 2: return "Brutto"
            case 3: return  "Normale"
            case 4: return "Buono"
            case 5: return "Grandioso"

class Film(Media):
    def __init__(self, title, rate:str, valutazione:float, media:float, percentage:float):
        super().__init__(title)
    def set_title(self,title:str):
        self.__title = title
    def get_title(self, title.str)->str:
        return title
    def add_valutazione(self, valutazione:float):
        