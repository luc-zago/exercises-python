
#forma uma nova palavra com as duas últimas letras de uma palavra

def devolve_palavras(n):
    a=len(list(n))
    b=list(n)[a-2]
    c=list(n)[a-1]
    d= b+' '+c
    return d
    
e=input(str("Digite uma palavra:"))

print(devolve_palavras(e))
