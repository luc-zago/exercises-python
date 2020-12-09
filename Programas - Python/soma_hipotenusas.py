
#Função que recebe um número inteiro 'n' e devolve a soma de todos os inteiros entre 1 e 'n' que são o comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.

def primo4(x):
    f=2
    while x % f!=0 and f <= (x/2):
        f=f+1
    if x%f==0:
        return False
    else:
        if x%4==1 and x!=1:
            return True
        else:
            return False

def e_hipotenusa(n):
    p=n
    while n!=0:
        if primo4(n)==True:
            if p%n==0:
                return True
        n=n-1
    return False

def soma_hipotenusas(n):
    c=0
    while n>0:
        if e_hipotenusa(n)==True:
            c=c+n
        n=n-1
    return c
