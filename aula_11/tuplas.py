carros = "Fusca", "Uno", "Celta", "Logan"

print(carros[-2])
print(carros[0:])
print(f"{carros[-3:-1]}\n")

def calcular(x, y):
    return x+y, x-y, x*y, x/y
re = calcular(5,7)
for i in re:
    print("Resultado: ", i)

a, b, c, d = calcular(3,10)
print("+ :", a)
print("- :", b)
print("* :", c)
print("/ :", d)