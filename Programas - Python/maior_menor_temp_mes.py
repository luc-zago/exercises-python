
def maior_menor_temp(n):
    print("A maior temperatura do mês foi",max(n),"graus e a menor foi",min(n),
          "graus.")

print("Programa que informa a maior e a menor temperatura de um mês")
a=int(input("Digite o ano: "))
b=str(input("Digite o mês: "))

mes=["Janeiro","janeiro","Fevereiro","fevereiro","Março","março","Abril","abril",
     "Maio","maio","Junho","junho","Julho","julho","Agosto","agosto","Setembro",
     "setembro","Outubro","outubro","Novembro","novembro","Dezembro","dezembro"]

while b not in mes:
    b=str(input("Mês inválido. Digite o mês: "))

dias=[]
dias.append(float(input("Digite a temperatura do dia 1:")))
dias.append(float(input("Digite a temperatura do dia 2:")))
dias.append(float(input("Digite a temperatura do dia 3:")))
dias.append(float(input("Digite a temperatura do dia 4:")))
dias.append(float(input("Digite a temperatura do dia 5:")))
dias.append(float(input("Digite a temperatura do dia 6:")))
dias.append(float(input("Digite a temperatura do dia 7:")))
dias.append(float(input("Digite a temperatura do dia 8:")))
dias.append(float(input("Digite a temperatura do dia 9:")))
dias.append(float(input("Digite a temperatura do dia 10:")))
dias.append(float(input("Digite a temperatura do dia 11:")))
dias.append(float(input("Digite a temperatura do dia 12:")))
dias.append(float(input("Digite a temperatura do dia 13:")))
dias.append(float(input("Digite a temperatura do dia 14:")))
dias.append(float(input("Digite a temperatura do dia 15:")))
dias.append(float(input("Digite a temperatura do dia 16:")))
dias.append(float(input("Digite a temperatura do dia 17:")))
dias.append(float(input("Digite a temperatura do dia 18:")))
dias.append(float(input("Digite a temperatura do dia 19:")))
dias.append(float(input("Digite a temperatura do dia 20:")))
dias.append(float(input("Digite a temperatura do dia 21:")))
dias.append(float(input("Digite a temperatura do dia 22:")))
dias.append(float(input("Digite a temperatura do dia 23:")))
dias.append(float(input("Digite a temperatura do dia 24:")))
dias.append(float(input("Digite a temperatura do dia 25:")))
dias.append(float(input("Digite a temperatura do dia 26:")))
dias.append(float(input("Digite a temperatura do dia 27:")))
dias.append(float(input("Digite a temperatura do dia 28:")))

if b=="Fevereiro" or b=="fevereiro":
    if a%4!=0:
        maior_menor_temp(dias)
    else:
        dias.append(float(input("Digite a temperatura do dia 29:")))
        maior_menor_temp(dias)

elif b=="Abril" or b=="abril" or b=="Junho" or b=="junho" or b=="Setembro" or b=="setembro" or b=="Novembro" or b=="novembro":
    dias.append(float(input("Digite a temperatura do dia 29:")))
    dias.append(float(input("Digite a temperatura do dia 30:")))
    maior_menor_temp(dias)

else:
    dias.append(float(input("Digite a temperatura do dia 29:")))
    dias.append(float(input("Digite a temperatura do dia 30:")))
    dias.append(float(input("Digite a temperatura do dia 31:")))
    maior_menor_temp(dias)
