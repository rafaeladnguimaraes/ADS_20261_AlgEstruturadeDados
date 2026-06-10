def imp_nome(n):
    print("nome: ", n)

nomes = "rafa", "dani", "duda","gabriel"
r_nomes = map(imp_nome, nomes)

list(r_nomes)

print("\n")

def aument(p):
    return round(p * 1.1)

preco = [1.11 , 354.00, 12.55, 10.00]
print("Peços anteriores", preco)
n_preco = map(aument, preco)
print("Preços novos: ", list(n_preco))


def s_val(val):
    total = 0
    for v in val:
        total += v
    return total

values = (2, 1), (3, 4, 6, 1), [1, 2, 3], (0, 3, 10)  

print( list( map(s_val, values)))