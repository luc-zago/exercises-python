
a=int(input("Digite um número:"))
b=int(input("Digite um número:"))
c=int(input("Digite um número:"))
d=int(input("Digite um número:"))

import math

e=math.sqrt(((a-c)**2)+((b-d)**2))

if e>=10:
 print("longe")

else:
 print("perto")