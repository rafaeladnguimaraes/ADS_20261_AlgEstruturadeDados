from author import Author
from book import Book
from books_LIFO import Pile

pile = Pile()
pile.imp()

a1 = Author("Ranson Riggs", 1979)
a2 = Author("Lemony Snicket", 1970)
b1 = Book("O Lar da Sra. Peregrine", 400, a1)
b2 = Book("O mau começo", 200, a2)
b3 = Book("O fim", 200, a2)
b4 = Book("Cidade dos Etéreos", 400, a1)

pile.add(b1)
pile.add(b2)
pile.qtBooksAuthor(a2)
pile.add(b3)
pile.add(b4)
pile.qtBooksAuthor("Rafa")
pile.qtBooksAuthor("Lemony Snicket")

pile.remove()
