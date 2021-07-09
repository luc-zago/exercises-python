
def menor_nome(array):
    menor = array[0]
    for nome in array:
        novo_nome = nome.strip()
        if (len(novo_nome) < len(menor)):
            menor = novo_nome
    return menor.capitalize()
