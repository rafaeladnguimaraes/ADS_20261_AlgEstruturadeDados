from arvore import Arvore

a = Arvore()

a.inserir(a.raiz, 50)
a.inserir(a.raiz, 60)
a.inserir(a.raiz, 40)
a.inserir(a.raiz, 5)
a.imprimirEmOrdem(a.raiz)
print("\n")
a.imprimiPreOrdem(a.raiz)
print("\n")
a.imprimiPosOrdem(a.raiz)
print("\n")
a.imprimirReverso(a.raiz)
