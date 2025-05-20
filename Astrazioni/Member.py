
from book import Book
class Member:
    def __init__(self, name:str, member_id:str):
        self.name = name
        self.member_id = member_id
        self.borrow_book: list[Book] = []
        

    def borrow_book(self, book: Book):
        if book in self._borrow_book.append(book)