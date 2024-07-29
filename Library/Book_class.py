

class Book_class:
    def __init__(self, title, author, pages, category, logclass):
        self.title = title
        self.author = author
        self.pages = pages
        self.category = category

    def __str__(self):
        return f"{self.title} by {self.author}\
         ({self.pages} pages, {self.category})"

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_pages(self, pages):
        self.pages = pages

    def set_category(self, category):
        self.category = category

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_pages(self):
        return self.pages

    def get_category(self):
        return self.category
