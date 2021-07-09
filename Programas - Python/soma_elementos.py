
#soma números inteiros de uma lista

def soma_elementos(n):
    x=(len(n))-1
    y=1
    z=n[0]
    while x>=y:
        z=z+n[y]
        y=y+1
    return z

def soma_lista1(lista, soma=0, index=None):
    if index == None:
        index = len(lista) - 1
    soma = soma + lista[index]
    index = index - 1
    if index == -1:
        return soma
    return soma_lista(lista, soma, index)

def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    lista2 = lista[:len(lista) - 1]
    lista2[len(lista2) -1] += lista[len(lista) - 1]
    return soma_lista(lista2)
