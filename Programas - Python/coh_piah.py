
import re

def le_assinatura():

    #função le os valores dos traços linguísticos do modelo e devolve uma assinatura a ser comparada com os textos fornecido
    
    print ("Bem vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a tazão Hapaz Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho médio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto= input("Digite o texto" + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentenças(texto):
    
    #função recebe texto e devolve uma lista das sentenças dentro do texto

    sentenças = re.split(r'[.!?]+', texto)
    if sentenças[-1] == '':
        del sentenças[-1]
    return sentenças

def separa_frases(sentença):

    #função recebe uma sentença e devolve uma lista das frases dentro da sentença

    return re.split(r'[,:;]+', sentença)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas listas de traços de assinaturas de texto e devolve o grau de similaridade nas assinaturas.'''
    # Minha implementação
    # O grau de similaridade é cálculado pela fórmula:
    # S(a,b) = (E²³i=1 ||fia - fib||)/6
    # S(a,b) é o grau de similaridade entre 'a' e 'b'
    # fi é o valor de cada traço linguístico [wal, ttl, hlr, sal, sac, pal]
    # ou seja, tem que fazer uma operação para cada traço linguístico
    # fib são os traços [wal, ttl, hlr, sal, sac, pal] passados como parâmetro
    # fia são os traços calculadas pela função 'calcula_assinatura'
    # ||fia - fib|| pode ser resolvido com a função 'abs' ex: abs(fia - fib)
    # Após calcular todos os traços linguísticos, eles são somados E²³i=1
    # E finalmente, divididos por 6
    # Quanto mais similar um texto for, menor será a S(a,b)
    # função recebe duas listas
    soma = 0
    index = 0
    for traço in as_a:
        soma += abs(traço - as_b[index])
        index += 1
    similaridade = soma / 6
    return similaridade
    pass

def calcula_assinatura(texto):
    '''Funcao que recebe um texto e devolve a assinatura do texto.'''
    # Minha implementação
    # a assinatura é formado por seis elementos:
    # 1. Tamanho médio de palavra (word average length - wal);
    # 2. Relação Type-Token (type token ratio - ttl);
    # 3. Razão Hapax Legomana (hapax legomana ratio - hlr);
    # 4. Tamanho médio de sentença (sentence average length - sal);
    # 5. Complexidade média da sentença (sentence average complexity - sac);
    # 6. Tamanho médio da frase (phrase average length - pal);
    
    # wal é calculada pela soma dos tamanhos das palavras dividido pelo número
    # total de palavras.
    lista_frases = [];
    sentenças = separa_sentenças(texto)
    for sentença in sentenças:
        lista_frases += separa_frases(sentença)
    lista_palavras = []
    for frase in lista_frases:
        lista_palavras += separa_palavras(frase)
    n_palavras = len(lista_palavras)
    soma = 0;
    for palavra in lista_palavras:
        # palavra = re.sub('\W+', '', palavra)
        soma += len(palavra)
    wal = soma / n_palavras

    # ttl é o número de palavras diferentes dividido pelo número total de palavras
    ttl = n_palavras_diferentes(lista_palavras) / n_palavras

    # hlr é o número de palavras que aparecem uma única vez dividido pelo número
    # total de palavras
    hlr = n_palavras_unicas(lista_palavras) / n_palavras

    # sal é a soma dos números de caracteres em todas as sentenças dividido pelo
    # número de sentenças
    caracteres_sentença = 0
    for sentença in sentenças:
        caracteres_sentença += len(sentença)
    sal = caracteres_sentença / len(sentenças)

    # sac é o número total de frases dividido pelo número de sentenças
    lista_frases = []
    for sentença in sentenças:
        lista_frases += separa_frases(sentença)
    sac = len(lista_frases) / len(sentenças)

    # pal é a soma do número de caracteres em cada frase dividida pelo número de
    # frases no texto
    caracteres_frases = 0
    for frase in lista_frases:
        caracteres_frases += len(frase)
    pal = caracteres_frases / len(lista_frases)
    return [wal, ttl, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e retorna o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    # Minha implementação
    lista_comparação_assinaturas = []
    for texto in textos:
        ass_a = calcula_assinatura(texto)
        lista_comparação_assinaturas.append(compara_assinatura(ass_a, ass_cp))
    menor = lista_comparação_assinaturas[0]
    for número in lista_comparação_assinaturas:
        if número < menor:
            menor = número
    index = lista_comparação_assinaturas.index(menor) +1
    # f'O autor do texto {index} está infectado com COH-PIAH'
    return index
    pass
