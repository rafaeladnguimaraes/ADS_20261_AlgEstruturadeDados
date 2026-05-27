from no_fila import No_fila
from no import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add(self, no_arvore: No):
        nodo = No_fila(no_arvore)   
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.prox = nodo  
        self.fim = nodo
        self.tamanho += 1
    
    def remv(self):
        if self.inicio is not None:
            aux = self.inicio.no_arvore
            self.inicio = self.inicio.prox
            if self.inicio == None:
                self.fim = None
            self.tamanho -= 1
            return aux
        return None