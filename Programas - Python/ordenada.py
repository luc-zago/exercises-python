def ordenada(lista):
    '''Recebe uma lista de inteiros e retorna um 'bool' informando se a lista
    está ordenada ou não'''
    if lista == sorted(lista):
        return True
    else:
        return False
