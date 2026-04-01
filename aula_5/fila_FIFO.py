# from arquivo importe a classe
from no import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def imprimir(self):
        print(" ---------- ")
        print(" Fila - FIFO")
        if self.inicio is None:
            print(" Não há elementos a serem exibidos.")
        else:
            aux = self.inicio
            txt = ""
            while aux:
                txt += aux.dado + " - "
                aux = aux.prox
            print( txt )
        print(" ---------- ")

    def add(self, valor):
        print(" Fila - FIFO - teste de recebimento de elemento")
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.prox = nodo
        self.fim = nodo    

        self.imprimir()

    def remove(self):
        if self.inicio is not None:
            self.inicio = self.inicio.prox
            print(" Não há elementos a serem exibidos.")
            if self.inicio is None:
                print(" Fila - FIFO - teste de remoção de elemento")
                self.fim = None  

        self.imprimir()            



