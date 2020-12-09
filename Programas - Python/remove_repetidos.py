
#função que remove os números inteiros repetidos de uma lista e os devolve em ordem

def remove_repetidos(n):
    n.sort()
    x=max(n)
    y=min(n)
    while x>=y:
        while n.count(y)>=2:
            del n[n.index(y)]
        y=y+1
    return n
