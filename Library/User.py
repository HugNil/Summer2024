from Logger import Logger


class User:
    def __init__(self):
        self.userID = 'N/A'
        self.name = 'N/A'
        self.books_borrowed = []
        self.logclass = Logger()

    def borrow_book(self, book):
        self.books_borrowed.append(book)
        self.logclass.log('{book} successfully borrowed by {self.name}')

    def return_book(self, book):
        self.books_borrowed.remove(book)
        self.logclass.log('{book} successfully returned by {self.name}')

    def display_books(self):
        for book in self.books_borrowed:
            print(book)

    def get_userID(self):
        return self.userID

    def get_name(self):
        return self.name

    def get_books_borrowed(self):
        return self.books_borrowed

    def set_userID(self, userID):
        self.userID = userID

    def set_name(self, name):
        self.name = name

    def reset_books_borrowed(self):
        self.books_borrowed = []
