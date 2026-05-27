from no import No
from fila import Fila

class Arvore:
    def __init__(self):
        self.raiz = None


    def inserir(self, raiz: No, valor):                
        if raiz is None:
            nodo = No(valor)
            
            if self.raiz is None:
                self.raiz = nodo
            return nodo
        
        if valor <= raiz.dado:
            raiz.esq = self.inserir(raiz.esq, valor)

        if valor > raiz.dado:
            raiz.dir = self.inserir(raiz.dir, valor)

        return raiz
            
    def imprimirEmOrdem(self, raiz: No):
        if raiz is not None:
            self.imprimirEmOrdem(raiz.esq)
            print(raiz.dado, end = " - ") 
            self.imprimirEmOrdem(raiz.dir)


    def imprimiPreOrdem(self, raiz: No):
        if raiz is not None:
            print(raiz.dado, end = " - ")
            self.imprimiPreOrdem(raiz.esq)
            self.imprimiPreOrdem(raiz.dir)


    def imprimiPosOrdem(self, raiz: No):
        if raiz is not None:
            self.imprimiPosOrdem(raiz.esq)
            self.imprimiPosOrdem(raiz.dir)
            print(raiz.dado, end = " - ")


    def imprimirReverso(self, raiz: No):
        if raiz is not None:
            self.imprimirReverso(raiz.dir)
            print(raiz.dado, end = " - ") 
            self.imprimirReverso(raiz.esq)

    def imprimirEmNivel(self, raiz: No):

