# coding: iso-8859-1 -*-

x=input("Por favor, entre com o n�mero de segundos que deseja converter:")
y=int(x)

a=y//86400
sobra=y%86400
b=sobra//3600
sobra2=sobra%3600
c=sobra2//60
d=sobra2%60

print(a,"dias", b,"horas",c,"minutos e",d,"segundos.")
