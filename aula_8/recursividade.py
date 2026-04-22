def fat(n):
    if n==1:
        return 1
    else:
        return n * fat(n-1)
        
print(fat(5))

def somarate(n):
    if n==1:
        return 1
    else:
        return n + somarate(n-1)
        
print(somarate(3))