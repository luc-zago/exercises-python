
#recebe uma palavra e devolve um número

def percentual(n):
    if n=="Terrible" and "Poor":
        return 3
    elif n=="Good" and "Great":
        return 10
    elif n=="Excellent":
        return 20
    else:
        return 0

a=str(input("Digite o rating:"))

print(percentual(a))
