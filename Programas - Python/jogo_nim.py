
print("Bem vindo ao jogo do NIM! Escolha:")
print(" ")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

def computador_escolhe_jogada(n,m):
    d=m+1
    e=n
    while e%d!=0:
        e=e-1
    f=n-e
    if f==0:
        if m==1:
            print(" ")
            print("O computador tirou uma peça.")
        else:
            print(" ")
            print("O computador tirou",m,"peças.")
        return m
    elif f==1:
        print(" ")
        print("O computador tirou uma peça.")
    else:
        print(" ")
        print("O computador tirou",f,"peças.")
    return f

def usuario_escolhe_jogada(n,m):
    print(" ")
    p=int(input("Quantas peças você vai tirar? "))
    while p>m or p<=0 or p>n:
        print(" ")
        print("Oops! Jogada inválida! Tente de novo.")
        print(" ")
        p=int(input("Quantas peças você vai tirar? "))
    if p==1:
        print("Você tirou uma peça.")
    else:
        print("Você tirou",p,"peças.")
    return p

def partida():
    n=int(input("Quantas peças? "))
    nmz(n)
    m=int(input("Limite de peças por jogada? "))
    mmz(m)
    if n%(m+1)==0:
        print(" ")
        print("Você começa!")
        while n!=0:
            n=n-(usuario_escolhe_jogada(n,m))
            if n!=0:
                tabuleiro(n)
                n=n-(computador_escolhe_jogada(n,m))
                if n==0:
                    print("Fim de jogo! O computador ganhou!")
                    return True
                else:
                    tabuleiro(n)
            else:
                print("Fim do jogo! Você ganhou!")
                return False
    else:
        print(" ")
        print("Comuputador começa!")
        while n!=0:
            n=n-(computador_escolhe_jogada(n,m))
            if n!=0:
                tabuleiro(n)
                n=n-(usuario_escolhe_jogada(n,m))
                if n==0:
                    print("Fim de jogo! Você ganhou!")
                    return False
                else:
                    tabuleiro(n)
            else:
                print("Fim do jogo! O computador ganhou!")
                return True

def campeonato():
    c=0
    y=0
    print(" ")
    print("**** Rodada 1 ****")
    print(" ")
    if partida()==True:
        c=c+1
    else:
        y=y+1
    print(" ")
    print("**** Rodada 2 ****")
    print(" ")
    if partida()==True:
        c=c+1
    else:
        y=y+1
    print(" ")
    print("**** Rodada 3 ****")
    print(" ")
    if partida()==True:
        c=c+1
    else:
        y=y+1
    print(" ")
    print("*** Final do campeonato! ***")
    print(" ")
    print("Placar: Você ",y," X ",c," Computador")

def tabuleiro(n):
    if n==1:
        print("Agora resta apenas uma peça no tabuleiro.")
    elif n==0:
        n=0
    else:
        print("Agora restam",n,"peças no tabuleiro.")
def nmz(n):
    while n<0:
        print("O número de peças deve ser maior que 0")
        n=int(input("Quantas peças? "))
def mmz(m):
    while m<0:
        print("O limite de peças por jogada deve ser maior que 0")
        m=int(input("Limite de peças por jogada? "))

print(" ")
a=int(input("Deseja jogar partida ou campeonato? "))
if a==1:
    print(" ")
    print("Você escolheu uma partida!")
    partida()
elif a==2:
    print(" ")
    print("Você escolheu um campeonato!")
    campeonato()
