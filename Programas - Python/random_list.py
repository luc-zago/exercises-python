from random import randrange

def lista_grande(inteiro):
    lista = []
    for i in range(inteiro):
        lista.append(randrange(101))
    return lista
