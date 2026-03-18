# from arquivo importe a classe

from no import No

class Lista:
    def __init__(self):
        self.inicio = None

    def imprimir(self):
        print(" ---------- ")
        print(" Lista encadeada - Ordem de Crescente")
        if self.inicio is None:
            print(" Não há elementos a serem exibidos.")
        else:
            aux = self.inicio
            while aux:
                print( aux.dado )
                aux = aux.prox
        print(" ---------- ")

    def add(self, valor):
        print(" Lista encadeada - teste de recebimento de elemento")
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = nodo
        
        self.imprimir()

    def remove(self, valor):
        if self.inicio is None:
            print(" Não há elementos a serem exibidos.")
        else:
            print(" Lista encadeada - teste de remoção de elemento")
            removed = False
            if valor == self.inicio.dado:
                self.inicio = self.inicio.prox
                removed = True
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux:
                    if valor == aux.dado:
                        ant.prox = aux.prox
                        removed = True
                        break
                    else:
                        ant = aux
                        aux = aux.prox
            if removed:
                print("\nO elemento", valor, "foi removido.")
            else:
                print("\nO elemento", valor, "não foi encontrado...")    

            self.imprimir()            



