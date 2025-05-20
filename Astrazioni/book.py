from typing import Self#da indicazione di creare l'istanza dell'oggetto a cui lavoro, quale dovrà essererilasciato come output
class Book:
    def __init__(self, title:str, autor: str, isbn: str):
        self.title  = title
        self.autor = autor
        self.isbn = isbn
    def __str__(self):
        return f"Title={self.title}: Author={self.autor}; ISBN={self.isbn}"
    
    @classmethod
    def from_string(cls, repr_str: str):
        sub_strs = repr_str.split(",")
        return cls(sub_strs[0], sub_strs[1], sub_strs[2])