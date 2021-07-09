def busca(lista, item):
    for index, elemento in enumerate(lista):
        if item == elemento:
            return index
    return False
