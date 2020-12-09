
print("Este programa soma os digitos de um número inteiro positivo.")
a=int(input("Digite um número inteiro positivo:"))

b=c=0

while a!=0:
 c=a%10
 b=b+c
 a=a//10

print(b)