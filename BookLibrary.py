class Lib:
    def __init__(self):
        self.book_list = list()

    def __len__(self):
        return len(self.book_list)

    def add_book(self, book):
        if book not in self.book_list:
            self.book_list.append(book)

    def remove_book(self, book):
        if isinstance(book, Book):
            if book in self.book_list:
                self.book_list.remove(book)
        elif isinstance(book, int):
            if self.book_list[book] != IndexError:
                del self.book_list[book]

    def __add__(self, other):
        self.add_book(other)
        return self

    def __iadd__(self, other):
        self.add_book(other)
        return self

    def __sub__(self, other):
        self.remove_book(other)
        return self

    def __isub__(self, other):
        self.remove_book(other)
        return self


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
