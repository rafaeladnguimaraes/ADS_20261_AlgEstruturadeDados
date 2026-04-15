from book import Book

class Pile:
    def __init__(self):
        self.top = None
    
    def add(self, book):
        if self.top is not None:
            book.prox = self.top
        self.top = book
        self.imp()
    
    def remove(self):
        if self.top is not None:
            self.top = self.top.prox
        self.imp()

    def imp(self):
        print(" *************** ")
        if self.top is None:
            print(" There are no books in pile.")
        else:
            print("\nBooks pile")
            aux = self.top
            while aux:
                print(aux)
                aux = aux.prox
        print(" *************** ")
    
    def qtBooksAuthor(self, name):
        if self.top is not None:
            cont = 0
            aux = self.top
            while aux:
                if name == aux.author.getName():
                    cont += 1
                aux = aux.prox
            if cont == 0:
                print(name, "doesn't have any books.")
            else:
                print(name, "have ", cont, " books.")
        