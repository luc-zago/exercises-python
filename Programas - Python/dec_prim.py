
print("Programa que imprime a decomposição em fatores primos de um número inteiro maior que 1.")

a=2
fat=2
m=0

a=int(input("Entre um número inteiro maior que 1: "))

while a>1:
    while a%fat==0:
        m=m+1
        a=a/fat
    if m>0:
        print("Fator",fat,"multiplicidade = ",m)
    fat=fat+1
    m=0
    if a==1:
        a=int(input("Entre um número inteiro maior que 1: "))
        fat=2
