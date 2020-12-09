
#Função que recebe como argumento um número 'n' inteiro 2>= e devolve a quantidade de primos existentes entre 2 e 'n'.

def n_primos(n):
    p=2
    x=0
    y=1
    if n<=1:
        return 0
    if n==p:
        return 1
    while n>1:
        while n % p!=0 and p <= (n/2):
            p=p+1
        if n%p==0:
            x=False
        else:
            x=True
        if x==True:
            y=y+1
        p=2
        n=n-1
    return y
