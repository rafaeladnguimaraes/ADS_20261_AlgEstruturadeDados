from author import Author

class Book:
    def __init__(self, title, pags, author):
        self.title = title
        self.pags = pags
        self.author = author
        self.prox = None

    def __str__(self):
        txt = "Title: " + self.title + "\n* Pages: " + str(self.pags) + " - " + str(self.author)
        return txt