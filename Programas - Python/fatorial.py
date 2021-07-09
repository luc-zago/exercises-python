
# print("Calcula o fatorial de um número.")
# f = int(input("Digite um número inteiro não negativo: "))

# c = 1
# fat = 1

# while c <= f:
# fat = fat * c
# c = 1 + c

# print(fat)

def fatorial(n):
    if n < 1:
        return 1
    else:
        return n * fatorial(n - 1)
