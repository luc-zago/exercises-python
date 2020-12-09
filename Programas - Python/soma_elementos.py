
#soma números inteiros de uma lista

def soma_elementos(n):
    x=(len(n))-1
    y=1
    z=n[0]
    while x>=y:
        z=z+n[y]
        y=y+1
    return z
