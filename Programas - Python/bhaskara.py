
print("Esse programa lhe informa as raízes reais de uma equação quadrática.")

a=float(input("Entre o valor de a:"))
b=float(input("Entre o valor de b:"))
c=float(input("Entre o valor de c:"))

while a==0:
 print("Quando 'a' é igual a 0, a equação deixa de ser quadrática e torna-se linear.")
 a=int(input("Entre um novo valor de a:"))

d=b**2-4*a*c

import math

if d==0:
 e=-b/(2*a)
 print("a raiz desta equação é",e)

if d>0:
 e=(-b+math.sqrt(d))/(2*a)
 f=(-b-math.sqrt(d))/(2*a)

 if e<f:
  print("as raízes da equação são",e,"e",f)

 else:
  print("as raízes da equação são",f,"e",e)

if d<0:
 print("esta equação não possui raízes reais")