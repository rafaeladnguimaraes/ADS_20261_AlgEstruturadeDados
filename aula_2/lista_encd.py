# from arquivo importe a classe

from no import No

class Lista:
    def __init__(self):
        self.inicio = None

    def imprimir(self):
        print(" ---------- ")
        print(" Lista encadeada - Ordem de Chegada")
        if self.inicio is None:
            print(" Não há elementos a serem exibidos.")
        else:
            aux = self.inicio
            while aux:
                print( aux.dado )
                aux = aux.prox

    def add(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = nodo
        
        self.imprimir()
