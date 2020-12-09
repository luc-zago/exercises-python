
print("Este programa lhe informa se um número inteiro positivo possui números adjacentes iguais.")
a=float(input("Digite um número:"))
a=int(a)

b=0
c=0
d=False

while a!=0:
 c=a%10
 a=a//10
 b=a%10
 if b==c:
  d=True

if d:
  print("sim")
else:
  print("não")