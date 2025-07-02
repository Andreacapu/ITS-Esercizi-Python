class MovieCatalog:
    catalog: dict[str, list[str]]#attributo di istanza

    def __init__(self):
        self.catalog: dict[str, list[str]] = {}
    
    def add_movie(self, director_name:str, movies:list[str]):
        if director_name not in self.catalog:#controllo che non ci sial la chiave nel dizionario
            self.catalog[director_name] = movies#crea un nuovo record con chiave valore movie
        else:
            for movie in movies:
                if movie not in self.catalog[director_name]:
                    self.catalog[director_name].append(movie)#


    def remove_movie(self, director_name:str, movie_name:str)-> None:
        if movie_name in self.catalog[director_name] and movie_name in self.cataloge
            self.catalog[director_name].remove(movie_name)
            if not self.catalog[director_name]:#check se la lista è vuota
                del self.catalog[director_name]
    
   
    def list_directors(self) -> list[str]:
        return list(self.catalog.keys())
    
    def search_movie_by_director(self, director_name:str) -> dict[str, list[str]] | str:
        if director_name in self.catalog:
            return self.catalog[director_name]
        else:
            return "il regista non è nel catalogo"
    
    def search_movies_by_title(self, title:str):
        result: dict[str, list[str]] = {}

        for director, movies in self.catalog.items():
            matching_movies: list[str] = []

            for movie in movies:
                if movie.lower() == title.lower():
                    matching_movies.append(movie)
            
            if matching_movies:
                result[director] = matching_movies#match registra con il film
        
        if result:
            return result
        else:
            return "nessun film trovato"
        
catalog = MovieCatalog()
#qua si aggiunge catalog.add_movie, catalog.remove_movie, catalog.list_director
#catalog.get_movie_by_director, catalog.search_movies_by_title

'''
class Media:
    def __init__(self, title:str, year:int) -> None:
        self.title = title
        self.year = year

    def get_info(self) -> str:
        return f"{self.title} ({self.year})

class Movie(Media):
    def __init__(self, title:str, year:int, duration:int):
        super(). __init__(title, year)
        self.duration = duration
    
    def get_info(self) -> str:
        return f"[FILM] {super().get_info()} - Durata: {self.duration}#ovveride

class SerieTV(Media):
    def __init__(self, title:str, year:int, seasons:int)
    super(). __init__(title, year)
    self.seasons = seasons

    def get_info(self) -> str:
    return f"[SERIETV] {super().get_info()} - Seasons: {self.seasons}

    
        

'''
        