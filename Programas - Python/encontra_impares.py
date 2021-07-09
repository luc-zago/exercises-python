def encontra_impares1(lista):
    for index, item in enumerate(lista):
        if item % 2 == 0:
            del(lista[index])
    return lista

def encontra_impares(lista):
    lista1 = lista[:]
    for index, item in enumerate(lista1):
        if item %2 == 0:
            del(lista1[index])
            return encontra_impares(lista1)
    return lista1
