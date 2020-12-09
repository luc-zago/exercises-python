
def fatorial(a):
    c=1
    fat=1
    while c<=a:
        fat=fat*c
        c=1+c
    return fat

print("Programa que lhe informa os fatoriais de uma sequência de números.")

a=1

a=float(input("Digite uma sequência de números positivos: "))

while a>=0:
    print (fatorial(a))
    a=float(input("Digite uma sequência de números positivos: "))
