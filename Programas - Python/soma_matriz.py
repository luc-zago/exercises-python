
def verifica_dimensoes(m1, m2):
    '''verifica se duas matrizes possuem as mesmas dimensoes'''

    mesmas_dimensoes = False
    
    if (len(m1) == len(m2)):
        verifica_colunas = 0
        index = -1
        for linha in m1:
            index += 1
            if (len(m1[index]) == len(m2[index])):
                verifica_colunas += 1
        if (len(m1) == verifica_colunas):
            mesmas_dimensoes = True

    return mesmas_dimensoes
    
def soma_matrizes(m1, m2):
    '''função que recebe duas matrizes e as compara. Caso elas possuam as
    mesmas dimensões, devolve a soma das duas matrizes. Caso contrário, devolve
    false'''

    mesmas_dimensoes = verifica_dimensoes(m1, m2)
    
    if (mesmas_dimensoes):
        soma = m1.copy()
        index = -1
        for linha in soma:
            index += 1
            index2 = -1
            for item in linha:
                index2 += 1
                soma[index][index2] += m2[index][index2]
        return soma

    else: return mesmas_dimensoes
