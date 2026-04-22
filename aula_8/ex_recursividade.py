# 1 - Cáculo de potência

def pot(n, e):
    if e == 0:
        return 1
    else:
        return n * pot(n ,e - 1)
        
print(pot(2, 4))

# 2 - Contagem Regressiva
 
def regre(n):
    if n == 0:
        return 0
    else:
        print(n)
        return regre(n - 1)
        
regre(3)

# 3 - Inverter String

def str_r(pl):
    if len(pl) <= 1:
        return pl
    return str_r( pl[1:] )+ pl[0]
  
print(str_r("rafa"))