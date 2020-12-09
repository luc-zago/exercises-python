
print("Programa que lhe informa os primeiros 'n' ímpares positivos naturais.")
a=int(input("Digite um valor para n:"))

while a<=0:
 print("'n' deve ser um número inteiro positivo.")
 a=int(input("Digite um valor para n:"))

b=0

i=1
print(i)

while (b+1)<a:
 i=i+2
 b=b+1
 print(i)