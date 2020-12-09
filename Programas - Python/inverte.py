
print("Programa que recebe uma sequência de números terminada em 0 e os devolve na ordem inversa.")
print("Digite uma sequência de números terminadas em 0.")

lista=[]
a=1

while a!=0:
    a=int(input(""))
    lista.append(a)

tam = len(lista) - 2
while tam >= 0:
    print(lista[tam])
    tam = tam-1
