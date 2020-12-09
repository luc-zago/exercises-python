
def fatorial(f):
    if f<0:
        return 0
    c=1
    fat=1
    while c<=f:
        fat=fat*c
        c=1+c
    return fat

def n_binomial(n, k):
    while n<k:
        print("k tem que ser menor do que n.")
        k=int(input("Digite um novo valor para k:"))
    return (fatorial(n))/(fatorial(k)*(fatorial(n-k)))

def testa_n_binomial():
    if n_binomial(0,0)==1:
        print("Funciona para 0 e 0")
    else:
        print("Não funciona para 0 e 0")
    if n_binomial(1,0)==1:
        print("Funciona para 1 e 0")
    else:
        print("Não funciona para 1 e 0")
    if n_binomial(2,0)==1:
        print("Funciona para 2 e 0")
    else:
        print("Não funciona para 2 e 0")
    if n_binomial(3,0)==1:
        print("Funciona para 3 e 0")
    else:
        print("Não funciona para 3 e 0")
    if n_binomial(4,0)==1:
        print("Funciona para 4 e 0")
    else:
        print("Não funciona para 4 e 0")
    if n_binomial(5,0)==1:
        print("Funciona para 5 e 0")
    else:
        print("Não funciona para 5 e 0")
   
def soma(x,y):
    return x+y
