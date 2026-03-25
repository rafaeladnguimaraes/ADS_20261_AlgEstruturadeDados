# from arquivo importe a classe
from no import No
class Lista2x:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def imprimir(self):
        print(" ************************ ")
        print(" LISTA DUPLAMENTE ENCADEADA - ORDEM DE CHEGADA")
        if self.inicio is None:
            print(" Não há elementos a serem exibidos.")
        else:
            aux = self.inicio
            while aux:
                print( aux.dado )
                aux = aux.proxi
        print(" ************************  ")
# ****************************************

    def imprimir_r(self):
        print(" ************************ ")
        print(" LISTA DUPLAMENTE ENCADEADA - ORDEM DE CHEGADA DO AVESSO")
        if self.inicio is None:
            print(" Não há elementos a serem exibidos.")
        else:
            aux = self.fim
            while aux:
                print( aux.dado )
                aux = aux.anter
        print(" ************************  ")
# ****************************************
    def add(self, valor):
        print(" Teste de recebimento de elemento")     
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.proxi = nodo
            nodo.anter = self.fim
        self.fim = nodo
        self.imprimir()

# ****************************************
    def remove(self, valor):
        print(" Teste de remoção de elemento") 
        if self.inicio is None:
            print(" Não há elementos a serem exibidos.")
        else:
            print(" Teste de remoção de elemento")
            removed = False
            if valor == self.inicio.dado:
                self.inicio = self.inicio.proxi
                removed = True
            else:
                ant = self.inicio
                aux = self.inicio.proxi
                while aux:
                    if valor == aux.dado:
                        ant.proxi = aux.proxi
                        removed = True
                        break
                    else:
                        ant = aux
                        aux = aux.proxi
            if removed:
                print("\nO elemento", valor, "foi removido.")
            else:
                print("\nO elemento", valor, "não foi encontrado...") 
        self.imprimir()            



