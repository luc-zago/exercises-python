
def fatorial(f):
    c=1
    fat=1
    while c<=f:
        fat=fat*c
        c=1+c
    return fat

def test_fatorial():
    assert fatorial(0)==1
    assert fatorial(1)==1
    assert fatorial(5)==120

def n_binomial(n, k):
    while n<k:
        print("k tem que ser menor do que n.")
        k=int(input("Digite um novo valor para k:"))
    return (fatorial(n))/(fatorial(k)*(fatorial(n-k)))

def test_n_binomial():
    assert n_binomial(0,0)==1
    assert n_binomial(1,0)==1
    assert n_binomial(2,0)==1
    assert n_binomial(3,0)==1
    assert n_binomial(4,0)==1
    assert n_binomial(5,0)==1
       
def soma(x,y):
    return x+y
